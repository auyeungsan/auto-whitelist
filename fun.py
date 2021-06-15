# python3 -m pip install boto3
import hashlib

# python3 -m pip install requests
import requests


# python3 -m pip install numpy
# import numpy as np
# import os
# import logging
# import sys

# Retrieve the list of existing buckets


def write_file(file_name, n_array):
    with open(file_name, 'w') as file:
        for item in n_array:
            file.write("%s\n" % item)
    file.close()


def read_file(file_name):
    file = open(file_name, "rb")
    content = file.read()
    file.close()
    return content


def hash_file(content):
    md5_hash = hashlib.md5()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest


def array_sort(n_array):
    n_array.sort(reverse=True)
    return n_array


def api_request(url):
    response = requests.get(url)
    return response
