# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/requests.ipynb (unless otherwise specified).

__all__ = ['CLOUDERA_USER', 'CLOUDERA_PASS', 'CLOUDERA_CLUSTER', 'CLOUDERA_NIFI_REST', 'NIFI_API_URL',
           'NIFI_API_PROCESSORS', 'NIFI_API_CONNECTIONS', 'NIFI_API_FLOWFILE_QUEUES', 'CLOUDERA_CREDENTIALS',
           'get_processor', 'update_processor', 'get_connection', 'list_flowfile_queues', 'get_flowfile_queues']

# Cell
import requests
from os import environ

# Cell
CLOUDERA_USER = environ['CLOUDERA_USER']
CLOUDERA_PASS = environ['CLOUDERA_PASS']
CLOUDERA_CLUSTER = environ['CLOUDERA_CLUSTER']
CLOUDERA_NIFI_REST = environ['CLOUDERA_NIFI_REST']

# Cell
NIFI_API_URL = CLOUDERA_CLUSTER + CLOUDERA_NIFI_REST

# Cell
NIFI_API_PROCESSORS = NIFI_API_URL + "processors/"
NIFI_API_CONNECTIONS = NIFI_API_URL + "connections/"
NIFI_API_FLOWFILE_QUEUES = NIFI_API_URL + "flowfile-queues/"

# Cell
CLOUDERA_CREDENTIALS = (CLOUDERA_USER, CLOUDERA_PASS)

# Cell

##Processors

def get_processor(processor_id):
    url = NIFI_API_PROCESSORS + processor_id
    res = requests.get(url, auth=CLOUDERA_CREDENTIALS)
    return custom_response(res)

def update_processor(processor_id):
    url = NIFI_API_PROCESSORS + processor_id
    res = requests.put(url, auth=CLOUDERA_CREDENTIALS)
    return custom_response(res)


def get_connection(connection_id):
    url = NIFI_API_CONNECTIONS + connection_id
    res = requests.get(url, auth=CLOUDERA_CREDENTIALS)
    return custom_response(res)


def list_flowfile_queues(connection_id):
    url = NIFI_API_FLOWFILE_QUEUES + f"{connection_id}/listing-requests"
    res = requests.post(url, auth=CLOUDERA_CREDENTIALS)
    return custom_response(res)


def get_flowfile_queues(connection_id, listing_request_id):
    url = NIFI_API_FLOWFILE_QUEUES + f"{connection_id}/listing-requests/{listing_request_id}"
    res = requests.get(url, auth=CLOUDERA_CREDENTIALS)
    return custom_response(res)