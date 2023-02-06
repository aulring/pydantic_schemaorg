from __future__ import annotations
from typing import TYPE_CHECKING


from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field, BaseModel


###################################################################################
#Attr Models
###################################################################################

{% for model in models.attr_models %}

{{model}}

{% endfor %}

###################################################################################
#Regular Models
###################################################################################

{% for model in models.models %}

{{model}}

{% endfor %}