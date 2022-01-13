from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupHusky(WearableSizeGroupEnumeration):
    """Size group \"Husky\" (or \"Stocky\") for wearables.

    See: https://schema.org/WearableSizeGroupHusky
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupHusky", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupHusky.update_forward_refs()
