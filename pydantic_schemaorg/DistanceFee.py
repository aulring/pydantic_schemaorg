from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PriceComponentTypeEnumeration import (
    PriceComponentTypeEnumeration,
)


class DistanceFee(PriceComponentTypeEnumeration):
    """Represents the distance fee (e.g., price per km or mile) part of the total price for an"
     "offered product, for example a car rental.

    See: https://schema.org/DistanceFee
    Model depth: 5
    """

    type_: str = Field("DistanceFee", const=True, alias="@type")


if TYPE_CHECKING:

    DistanceFee.update_forward_refs()
