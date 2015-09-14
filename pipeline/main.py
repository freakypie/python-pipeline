from __future__ import print_function
from importlib import import_module


class StopProcessing(Exception):
    pass


class Pipeline(object):
    """ processes nodes passing the results of one to the next """

    def __init__(self, nodes=None):
        self._nodes = []
        if nodes:
            self.load(nodes)

    def import_function(self, path):
        path, last = path.rsplit(".", 1)
        return getattr(import_module(path), last)

    def load(self, modules):
        for module in modules:
            self._nodes.append(self.import_function(module))

    def process(self, **kwargs):
        try:
            for node in self._nodes:
                result = node(**kwargs)
                if result:
                    kwargs = result
        except StopProcessing:
            pass
        return kwargs
