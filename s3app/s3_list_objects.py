#
# Script de test Object S3
# Génère 10 objets JSON qui sont téléversés vers un Bucket S3
# 
from s3_client import s3
import sys
import json
from variables import bucket


response = s3.list_objects(
    Bucket=bucket,
)

print("\n<> Liste des objets stockés dans le bucket " + bucket + "\n")
for r in response["Contents"]:
    print(r)

# obj = s3.get_object(Bucket=bucket, Key='myfiles20')

# print("\n<> Metadata associé à myfiles20\n")
# print(obj["Metadata"])
# print("\n<> Contenu de myfiles20\n")
# print(obj["Body"].read().decode('utf-8'))