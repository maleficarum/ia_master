import os, types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

cos_client = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='<MASKED_TOKEN>',
    ibm_auth_endpoint="https://iam.cloud.ibm.com/identity/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.direct.us-south.cloud-object-storage.appdomain.cloud')

bucket = 'factoryreset-donotdelete-pr-51kc45qih7esw1'
object_key = 'historico_reparaciones.csv'

body = cos_client.get_object(Bucket=bucket,Key=object_key)['Body']

if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )

df_1 = pd.read_csv(body)
df_1.head(10)
SERIE	ITEM	MOVEMENT_DATE	WH_ID	SCRAP_CODE
0	1154NJ698400002	28928	2024-01-01 00:00:00	400	NaN
1	1154NJ698400072	28928	2024-02-01 00:00:00	400	NaN
2	1154NJ698400128	28928	2024-07-01 00:00:00	400	NaN
3	1154NJ698400240	28928	2024-02-01 00:00:00	400	NaN
4	1154NJ698400343	28928	2024-04-01 00:00:00	400	NaN
5	1154NJ698400422	28928	2024-05-01 00:00:00	400	NaN
6	1154NJ698400445	28928	2024-10-02 09:59:08	2	NaN
7	1154NJ698400452	28928	2024-02-01 00:00:00	400	NaN
8	1154NJ698400483	28928	2024-01-01 00:00:00	400	NaN
9	1154NJ698400610	28928	2024-01-01 00:00:00	400	NaN
 