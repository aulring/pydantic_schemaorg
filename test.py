from typing import Optional

import networkx as nx
from pydantic import create_model, BaseModel



class DependencyDict(dict):
  g = nx.DiGraph()
  
  def __setitem__(self, *args, **kwargs):
      print("hi")
      super().__setitem__(*args, **kwargs)


INIT = {}
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

