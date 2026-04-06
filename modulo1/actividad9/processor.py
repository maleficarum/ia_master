import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import regularizers
import os

DATASET_PATH = "assets"
MODEL_PATH = 'best_model.keras'

def load_assets():
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        DATASET_PATH,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(224, 224),
        batch_size=32
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        DATASET_PATH,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(224, 224),
        batch_size=32
    )

    return train_ds, val_ds

def normalize(train_ds, val_ds):
    normalization_layer = layers.Rescaling(1./255)
    train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))
    return train_ds, val_ds

def optimize_dataset(train_ds, val_ds):
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    return train_ds, val_ds

def create_new_model():
    """Crea un nuevo modelo desde cero"""
    print("Creando modelo nuevo...")
    
    data_augmentation = keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.2),
        layers.RandomContrast(0.2),
        layers.RandomBrightness(0.2),
    ])
    
    base_model = MobileNetV2(
        input_shape=(224, 224, 3),
        include_top=False,
        weights='imagenet'
    )
    base_model.trainable = False
    
    model = keras.Sequential([
        data_augmentation,
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.BatchNormalization(),
        layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.0005)),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.0005)),
        layers.Dropout(0.3),
        layers.Dense(24, activation='softmax')
    ])
    
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def train_new_model(model, train_ds, val_ds):
    """Entrena un modelo nuevo por primera vez"""
    print("\nEntrenando modelo por primera vez")
    
    checkpoint = keras.callbacks.ModelCheckpoint(
        MODEL_PATH,
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    )
    
    reduce_lr = keras.callbacks.ReduceLROnPlateau(
        monitor='val_accuracy',
        factor=0.5,
        patience=3,
        min_lr=0.00001,
        verbose=1
    )
    
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=20,
        callbacks=[reduce_lr, checkpoint],
        verbose=1
    )
    
    test_loss, test_acc = model.evaluate(val_ds, verbose=0)
    print(f"\nPrecisión después de fase 1: {test_acc:.2%}")
    
    return model, history

def fine_tune_model(model, train_ds, val_ds):
    """Descongela y hace fine-tuning"""
    print("\nFase 2 - Fine-tuning (descongelando capas)")
    
    # Descongelar la base
    model.layers[1].trainable = True
    
    for i, layer in enumerate(model.layers[1].layers):
        if i < 100:
            layer.trainable = False
    
    # Recompilar con learning rate más bajo
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.0001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    checkpoint = keras.callbacks.ModelCheckpoint(
        MODEL_PATH,
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    )
    
    reduce_lr = keras.callbacks.ReduceLROnPlateau(
        monitor='val_accuracy',
        factor=0.5,
        patience=3,
        min_lr=0.000001,
        verbose=1
    )
    
    early_stopping = keras.callbacks.EarlyStopping(
        monitor='val_accuracy',
        patience=5,
        restore_best_weights=True,
        verbose=1
    )
    
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=30,
        callbacks=[reduce_lr, early_stopping, checkpoint],
        verbose=1
    )
    
    test_loss, test_acc = model.evaluate(val_ds, verbose=0)
    print(f"\nPrecisión después de fine-tuning: {test_acc:.2%}")
    
    return model, history

def continue_training():
    """Continúa entrenando o crea modelo nuevo"""
    
    if not os.path.exists(MODEL_PATH):
        print(f"No se encuentra {MODEL_PATH}")
        model = create_new_model()
        model.summary()
        model, history = train_new_model(model, train_ds, val_ds)
        # Después del primer entrenamiento, hacer fine-tuning
        model, history2 = fine_tune_model(model, train_ds, val_ds)
        return model, history2
    
    # Si existe, intentar más fine-tuning
    print(f"Cargando modelo existente: {MODEL_PATH}")
    model = keras.models.load_model(MODEL_PATH)
    
    test_loss, test_acc = model.evaluate(val_ds, verbose=0)
    print(f"Precisión actual: {test_acc:.2%}")
    
    # Si la precisión es baja (<80%), hacer fine-tuning más agresivo
    if test_acc < 0.80:
        print("\nPrecisión baja. Realizando fine-tuning más agresivo.")
        
        model.layers[1].trainable = True
        for layer in model.layers[1].layers[:80]:
            layer.trainable = False
        
        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.00005),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
    else:
        print("\nFine-tuning adicional.")
        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.00001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
    
    checkpoint = keras.callbacks.ModelCheckpoint(
        MODEL_PATH,
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    )
    
    reduce_lr = keras.callbacks.ReduceLROnPlateau(
        monitor='val_accuracy',
        factor=0.5,
        patience=3,
        min_lr=0.0000001,
        verbose=1
    )
    
    early_stopping = keras.callbacks.EarlyStopping(
        monitor='val_accuracy',
        patience=6,
        restore_best_weights=True,
        verbose=1
    )
    
    print(f"\nContinuando entrenamiento...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=20,
        callbacks=[reduce_lr, early_stopping, checkpoint],
        verbose=1
    )
    
    final_loss, final_acc = model.evaluate(val_ds, verbose=0)
    improvement = final_acc - test_acc
    print(f"\nResultados:")
    print(f"   Precisión antes: {test_acc:.2%}")
    print(f"   Precisión después: {final_acc:.2%}")
    print(f"   Mejora: {improvement:.2%}")
    
    if final_acc >= 0.95:
        print("Alcanzado el 95% de precisión")
    else:
        print(f"Faltan {(0.95 - final_acc):.2%} para llegar al 95%")
    
    return model, history

# ============ EJECUCIÓN ============

print("Cargando datasets...")
train_ds, val_ds = load_assets()

class_names = train_ds.class_names
print(f"Clases encontradas: {len(class_names)} clases")

print("Normalizando datos...")
train_ds, val_ds = normalize(train_ds, val_ds)

print("Optimizando datasets...")
train_ds, val_ds = optimize_dataset(train_ds, val_ds)

model, history = continue_training()