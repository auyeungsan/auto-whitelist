# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import hashlib
import aws
# python3 -m pip install boto3


# python3 -m pip install numpy
# import numpy as np
# import os
# import logging
# import sys

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


# import A ip list
ip_a = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5', '172.16.0.1', '172.16.0.2',
        '172.16.0.3']
array_sort(ip_a)
# print("current ip list :", array_sort(ip_a))
write_file("test.txt", array_sort(ip_a))

# import B ip list
ip_b = ['172.16.0.1', '172.16.0.2', '192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5']
array_sort(ip_b)
# print("current ip list :", array_sort(ip_b))
write_file("test2.txt", array_sort(ip_b))

# test.txt hash key
digest_a = hash_file(read_file("test.txt"))
# print(digest_a)

# test2.txt hash key
digest_b = hash_file(read_file("test2.txt"))
# print(digest_b)


if digest_b == digest_a:
    print("相等")
else:
    print("不相等")
