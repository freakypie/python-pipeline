from .main import StopProcessing


def A(**kwargs):
    kwargs["A"] = 1
    return kwargs


def B(**kwargs):
    kwargs["A"] += 1
    kwargs["B"] = True
    return kwargs


def C(**kwargs):
    return {"C": "masterful"}


def D(**kwargs):
    raise StopProcessing()
