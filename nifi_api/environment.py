# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_environment.ipynb (unless otherwise specified).

__all__ = ['Credentials', 'NifiEndpoint', 'DataFlowIds']

# Cell
import requests
from os import environ
import json

# Cell
class Credentials:

    user = environ['CLOUDERA_USER']
    password = environ['CLOUDERA_PASS']
    credentials = (user, password)

# Cell
class NifiEndpoint:

    cluster = environ['CLOUDERA_CLUSTER']
    nifi_rest = cluster + environ['CLOUDERA_NIFI_REST']
    processors = nifi_rest + "processors/"
    connections = nifi_rest + "connections/"
    flowfile_queues = nifi_rest + "flowfile-queues/"

# Cell


class DataFlowIds:
    """ Dataflow uuids. Every valid DataFlow must have initial-middle-final
        procesors and initial-final connections
        """

    def __init__(
        self,
        pipeline: dict,
    ) -> None:
        self.in_connection = pipeline['in_connection']['Id']
        self.in_processor = pipeline['in_processor']['Id']
        self.middle_processor = pipeline['middle_processor']['Id']
        self.out_connection = pipeline['out_connection']['Id']
        self.out_processor = pipeline['out_processor']['Id']


