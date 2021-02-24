# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_source_to_refined.ipynb (unless otherwise specified).

__all__ = ['source_to_refined']

# Cell

from time import sleep
from .environment import NifiIds
from .dataflow import DataFlow

# Cell
def source_to_refined():
    """ The Source To Refined dataflow is decomposed in three sequential steps:
        - Source To Raw
        - Raw To Discovery
        - Discovery To Refined
    The script assures that each of these steps starts only after the
    previous step has finished.
    """

    # time between steps
    T = 15

    source_to_raw = DataFlow(NifiIds.sourceToRaw)
    raw_to_discovery = DataFlow(NifiIds.rawToDiscovery)
    discovery_to_refined = DataFlow(NifiIds.discoveryToRefined)

    source_to_raw.run()
    sleep(T)
    raw_to_discovery.run()
    sleep(T)
    discovery_to_refined.run()