import json
import readchar
import yaml
import shutil
import boto3
from variables import *
from disable_ssl_warning import *
from s3_functions import *


def main_menu():

    print("== S3 actions ==========================================================")
    print("[l] List | [b] Bulk create objects | [q] Quit")

    choice = readchar.readchar()

    if choice == "l":
        list_objects(bucket)
    elif choice == "b":
        bulk_create(bucket)
    elif choice == "q":
        quit()

def quit():
    print("Quit")
    exit(0)

if __name__ == '__main__':
    while True:
        main_menu()