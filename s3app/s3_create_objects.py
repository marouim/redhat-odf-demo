#
# Script de test Object S3
# Génère 10 objets JSON qui sont téléversés vers un Bucket S3
# 
from s3_client import s3
import sys
import json
from variables import bucket

object_name = "test156"
number_of_files = 10
object_name_prefix = "myfiles2"

f = open("content.txt", "r")
content = f.read()

for i in range(number_of_files):
  object_name = object_name_prefix + str(i)
  object_content = {
    "name": object_name,
    "id": str(i),
    "meta": object_name_prefix,
    "content": content
  }
  
  metadata = {
    "purpose": "demo",
    "color": "blue",
    "model": "json"
  }

  print("Upload object " + object_name)
  s3.put_object(
    Bucket=bucket, 
    Key=object_name, 
    Metadata=metadata, 
    Body=json.dumps(object_content)
  )
