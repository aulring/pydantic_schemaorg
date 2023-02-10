from typing import Optional

import networkx as nx
from pydantic import create_model, BaseModel



INIT = {}

class DependencyDict(dict):
    dependency_graphs = {}
  
    def __setitem__(self, *args, **kwargs):
        print("HIII")
        model, fields =  args
        for field_key, types in fields.items():
            if "dynamic_creation" in types:
                initialized = eval(types)
        super().__setitem__(*args, **kwargs)

LOOKUP = DependencyDict()


def dynamic_creation(model: str):
    if model not in INIT:
        fields = LOOKUP[model]
        print(fields)
        dynamic_creation = create_model(model, __base__=BaseModel, **fields)
        INIT[model] = dynamic_creation
        return dynamic_creation
    else:
        return INIT[model]


LOOKUP["ModelY"] =  {'field4': (str, None), 'field5': (Optional[str], None)}
LOOKUP["ModelX"] =  {'field1': (str, None), 'field2': (Optional[str], None), "field3": ("dynamic_creation('ModelY')", None)}
LOOKUP["ModelZ"] =  {'field1': (str, None), 'field2': (Optional[str], None), "field4": ("dynamic_creation('ModelX')", None)}

ModelY = dynamic_creation("ModelY")
ModelZ = dynamic_creation("ModelZ")
ModelX = dynamic_creation("ModelX")

