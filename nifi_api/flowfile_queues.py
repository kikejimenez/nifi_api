# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_flowfile_queues.ipynb (unless otherwise specified).

__all__ = ['FlowfileQueues']

# Cell
import requests
from .endpoints import *
import json

# Cell
class FlowfileQueues:

    nifi_api = NIFI_API_FLOWFILE_QUEUES

    @staticmethod
    def custom_response(res):
        try:
            return json.loads(res.text), res
        except:
            return "No JSON available", res

    @classmethod
    def get(cls, processor_id):
        url = nifi_api + processor_id
        res = requests.get(url, auth=CLOUDERA_CREDENTIALS)
        return cls.custom_response(res)

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
        return cls.custom_response(res)