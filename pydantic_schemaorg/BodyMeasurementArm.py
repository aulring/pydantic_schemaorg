from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyMeasurementTypeEnumeration import (
    BodyMeasurementTypeEnumeration,
)


class BodyMeasurementArm(BodyMeasurementTypeEnumeration):
    """Arm length (measured between arms/shoulder line intersection and the prominent wrist"
     "bone). Used, for example, to fit shirts.

    See: https://schema.org/BodyMeasurementArm
    Model depth: 6
    """

    type_: str = Field("BodyMeasurementArm", const=True, alias="@type")


if TYPE_CHECKING:

    BodyMeasurementArm.update_forward_refs()
