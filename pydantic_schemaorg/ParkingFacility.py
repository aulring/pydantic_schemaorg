from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class ParkingFacility(CivicStructure):
    """A parking lot or other parking facility.

    See: https://schema.org/ParkingFacility
    Model depth: 4
    """

    type_: str = Field("ParkingFacility", const=True, alias="@type")


if TYPE_CHECKING:

    ParkingFacility.update_forward_refs()
