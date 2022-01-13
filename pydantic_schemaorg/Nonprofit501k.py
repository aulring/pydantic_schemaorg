from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501k(USNonprofitType):
    """Nonprofit501k: Non-profit type referring to Child Care Organizations.

    See: https://schema.org/Nonprofit501k
    Model depth: 6
    """

    type_: str = Field("Nonprofit501k", const=True, alias="@type")


if TYPE_CHECKING:

    Nonprofit501k.update_forward_refs()
