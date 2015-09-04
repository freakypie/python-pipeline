
`pipeline` is just a simple data processor that will pass the results from the
top node down to the bottom.

If you have 3 nodes for instance:

    A    B    C

Then `pipeline`

    A(opts)  ->  B(opts)  ->  C(opts) -> opts

Any changes A adds will be passed to B, and so on. Finally, the `opts` are
returned

Any node can call `StopProcessing` and the `opts` will be returned immediately

pipeline can load function modules from a list of dotted module strings


```python

from pipeline import Pipeline

def A(**kwargs):
    # ...
    return kwargs


def B(**kwargs):
    # ...
    return kwargs


def C(**kwargs):
    # ...
    return kwargs


p = Pipeline([A, B, C])
print(p.process())

```
