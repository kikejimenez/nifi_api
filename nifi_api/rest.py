# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_rest.ipynb (unless otherwise specified).

__all__ = ['Processor', 'Connection', 'Flowfile']

# Cell
import requests
import nifi_api as na
from .endpoints import *
from .tools import custom_response
import json

# Cell
class Processor:

    nifi_api = NIFI_API_PROCESSORS

    @classmethod
    def get(cls, processor_id):
        url = nifi_api + processor_id
        res = requests.get(url, auth=CLOUDERA_CREDENTIALS)
        return custom_response(res)

    @classmethod
    def update_run_status(cls, processor_id, clientId, state="STOPPED"):

        data = {
            "revision": {
                'clientId': clientId,
                'version': 1
            },
            "state": state,
            "disconnectedNodeAcknowledged": True
        }

        url = nifi_api + f"{processor_id}/run-status"

        res = requests.put(
            url,
            data=data,
            auth=CLOUDERA_CREDENTIALS,
            headers={'content-type': 'application/json'}
        )
        return custom_response(res)

# Cell
class Connection:

    nifi_api = NIFI_API_CONNECTIONS



    @classmethod
    def list_queues(cls, processor_id):
        url = cls.nifi_api + processor_id
        res = requests.get(url, auth=CLOUDERA_CREDENTIALS)
        return custom_response(res)



    @classmethod
    def update_run_status(cls, processor_id, clientId, state="STOPPED"):

        data = {
            "revision": {
                'clientId': clientId,
                'version': 1
            },
            "state": state,
            "disconnectedNodeAcknowledged": True
        }

        url = nifi_api + f"{processor_id}/run-status"

        res = requests.put(
            url,
            data=data,
            auth=CLOUDERA_CREDENTIALS,
            headers={'content-type': 'application/json'}
        )
        return custom_response(res)

# Cell
class Flowfile:

    nifi_api = NIFI_API_FLOWFILE_QUEUES

    @classmethod
    def listing_request(cls,connection_id):
        url = cls.nifi_api + f"{connection_id}/listing-requests"
        res = requests.post(url, auth=CLOUDERA_CREDENTIALS)
        return custom_response(res)

    @classmethod
    def list_queues(cls,connection_id):
        listing_request,_ = cls.listing_request(connection_id)
        listing_request_id  = listing_request["listingRequest"]['id']
        url = cls.nifi_api + f"{connection_id}/listing-requests/{listing_request_id}"
        res = requests.get(url, auth=CLOUDERA_CREDENTIALS)
        return custom_response(res)
