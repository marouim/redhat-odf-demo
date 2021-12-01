import os

# Default values
endpoint_url = "https://s3-openshift-storage.apps.rhcasalab.sandbox1385.opentlc.com"
access_key = "oTeCpVd5EwL2O9gcreMX"
secret_key = "bVyMLlSiXldVwuwefK+4OYTDQhwD9xfVj5MgpWBJ"
bucket = "test2-5f5cd560-9506-4113-914b-2465f622f4ed"

if os.environ.get("BUCKET_HOST"):
    print("BUCKET_HOST defined from environment variable")
    endpoint_url = os.environ.get("BUCKET_HOST")
if os.environ.get("BUCKET_NAME"):
    bucket = os.environ.get("BUCKET_NAME")
if os.environ.get("AWS_ACCESS_KEY_ID"):
    access_key = os.environ.get("AWS_ACCESS_KEY_ID")
if os.environ.get("AWS_SECRET_ACCESS_KEY"):
    secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
