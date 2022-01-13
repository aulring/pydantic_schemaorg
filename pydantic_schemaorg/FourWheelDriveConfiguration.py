from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue


class FourWheelDriveConfiguration(DriveWheelConfigurationValue):
    """Four-wheel drive is a transmission layout where the engine primarily drives two wheels"
     "with a part-time four-wheel drive capability.

    See: https://schema.org/FourWheelDriveConfiguration
    Model depth: 6
    """

    type_: str = Field("FourWheelDriveConfiguration", const=True, alias="@type")


if TYPE_CHECKING:

    FourWheelDriveConfiguration.update_forward_refs()
