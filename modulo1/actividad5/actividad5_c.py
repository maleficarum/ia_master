# Diccionario con información detallada de una canción de Black Metal
black_metal_songs = {
    "cancion1": {
        "artista": "Immortal",
        "album": "At the Heart of Winter",
        "duracion_segundos": 352,
        "duracion_formato": "5:52",
        "genero": "Melodic Black Metal",
        "año": 1999,
        "pais": "Noruega",
        "discografica": "Osmose Productions",
        "compositor": "Abbath",
        "calificacion": 9.5
    },
    "cancion2": {
        "artista": "Mayhem",
        "album": "De Mysteriis Dom Sathanas",
        "duracion_segundos": 442,
        "duracion_formato": "7:22",
        "genero": "Norwegian Black Metal",
        "año": 1994,
        "pais": "Noruega",
        "discografica": "Deathlike Silence Productions",
        "compositor": "Euronymous",
        "calificacion": 9.8
    },
    "cancion3": {
        "artista": "Burzum",
        "album": "Filosofem",
        "duracion_segundos": 1514,
        "duracion_formato": "25:14",
        "genero": "Ambient Black Metal",
        "año": 1996,
        "pais": "Noruega",
        "discografica": "Misanthropy Records",
        "compositor": "Varg Vikernes",
        "calificacion": 9.2
    },
    "cancion4": {
        "artista": "Darkthrone",
        "album": "Transilvanian Hunger",
        "duracion_segundos": 367,
        "duracion_formato": "6:07",
        "genero": "Raw Black Metal",
        "año": 1994,
        "pais": "Noruega",
        "discografica": "Peaceville Records",
        "compositor": "Fenriz",
        "calificacion": 9.7
    },
    "cancion5": {
        "artista": "Emperor",
        "album": "In the Nightside Eclipse",
        "duracion_segundos": 522,
        "duracion_formato": "8:42",
        "genero": "Symphonic Black Metal",
        "año": 1994,
        "pais": "Noruega",
        "discografica": "Candlelight Records",
        "compositor": "Ihsahn",
        "calificacion": 9.6
    },
    "cancion6": {
        "artista": "Satyricon",
        "album": "Nemesis Divina",
        "duracion_segundos": 390,
        "duracion_formato": "6:30",
        "genero": "Norwegian Black Metal",
        "año": 1996,
        "pais": "Noruega",
        "discografica": "Moonfog Productions",
        "compositor": "Sigurd Wongraven",
        "calificacion": 9.0
    },
    "cancion7": {
        "artista": "Gorgoroth",
        "album": "Under the Sign of Hell",
        "duracion_segundos": 375,
        "duracion_formato": "6:15",
        "genero": "Raw Black Metal",
        "año": 1997,
        "pais": "Noruega",
        "discografica": "Malicious Records",
        "compositor": "Infernus",
        "calificacion": 8.8
    },
    "cancion8": {
        "artista": "Marduk",
        "album": "Panzer Division Marduk",
        "duracion_segundos": 140,
        "duracion_formato": "2:20",
        "genero": "War Black Metal",
        "año": 1999,
        "pais": "Suecia",
        "discografica": "Osmose Productions",
        "compositor": "Morgan Steinmeyer Håkansson",
        "calificacion": 9.1
    },
    "cancion9": {
        "artista": "Dimmu Borgir",
        "album": "Enthrone Darkness Triumphant",
        "duracion_segundos": 350,
        "duracion_formato": "5:50",
        "genero": "Symphonic Black Metal",
        "año": 1997,
        "pais": "Noruega",
        "discografica": "Nuclear Blast",
        "compositor": "Shagrath",
        "calificacion": 9.3
    },
    "cancion10": {
        "artista": "Behemoth",
        "album": "Satanica",
        "duracion_segundos": 221,
        "duracion_formato": "3:41",
        "genero": "Blackened Death Metal",
        "año": 1999,
        "pais": "Polonia",
        "discografica": "Avantgarde Music",
        "compositor": "Nergal",
        "calificacion": 9.4
    }
}

print("🎸 BLACK METAL SONGS COLLECTION 🎸")
print("=" * 60)
print(f"Total de canciones: {len(black_metal_songs)}")
print("=" * 60)

# Desplegar información de cada canción
for cancion_id, info in black_metal_songs.items():
    print(f"\n⚔️  {cancion_id.upper()} - {info['artista']} - {info['album']} ⚔️")
    print("-" * 60)
    
    # Desplegar keys y values
    print(f"Llaves : {list(info.keys())}")
    print(f"Valores : {list(info.values())}")
    
    print("Items:")
    items_mostrar = ['artista', 'album', 'duracion_formato', 'año', 'genero', 'pais', 'calificacion']
    for key in items_mostrar:
        print(f"   • {key}: {info[key]}")
    
    print(f"   • Tupla completa del artista: {('artista', info['artista'])}")

print("\nEstadisticas :")
print("-" * 60)

# Artistas únicos
artistas = set(info['artista'] for info in black_metal_songs.values())
print(f"Artistas únicos: {len(artistas)} - {sorted(artistas)}")

# Países representados
paises = set(info['pais'] for info in black_metal_songs.values())
print(f"Países: {paises}")

# Promedio de calificaciones
promedio_calif = sum(info['calificacion'] for info in black_metal_songs.values()) / len(black_metal_songs)
print(f"Calificación promedio: {promedio_calif:.2f}")

# Canción más larga
cancion_mas_larga = max(black_metal_songs.values(), key=lambda x: x['duracion_segundos'])
print(f"Canción más larga: {cancion_mas_larga['artista']} - {cancion_mas_larga['album']} ({cancion_mas_larga['duracion_formato']})")

# Canción mejor calificada
mejor_calificada = max(black_metal_songs.values(), key=lambda x: x['calificacion'])
print(f"Mejor calificada: {mejor_calificada['artista']} - {mejor_calificada['album']} ({mejor_calificada['calificacion']})")