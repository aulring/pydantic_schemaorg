from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class SizeSystemEnumeration(Enumeration):
    """Enumerates common size systems for different categories of products, for example \"EN-13402\""
     "or \"UK\" for wearables or \"Imperial\" for screws.

    See: https://schema.org/SizeSystemEnumeration
    Model depth: 4
    """

    type_: str = Field("SizeSystemEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    SizeSystemEnumeration.update_forward_refs()
