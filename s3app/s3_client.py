import boto3
from variables import *
from disable_ssl_warning import *

s3 = boto3.client(
  service_name = "s3",
  verify = False, 
  endpoint_url = "https://" + endpoint_url,
  aws_access_key_id = access_key,
  aws_secret_access_key = secret_key
)
