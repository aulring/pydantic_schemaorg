from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupRegular(WearableSizeGroupEnumeration):
    """Size group \"Regular\" for wearables.

    See: https://schema.org/WearableSizeGroupRegular
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupRegular", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupRegular.update_forward_refs()
