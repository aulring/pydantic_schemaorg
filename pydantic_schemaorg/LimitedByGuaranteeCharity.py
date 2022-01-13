from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class LimitedByGuaranteeCharity(UKNonprofitType):
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that"
     "is limited by guarantee (UK).

    See: https://schema.org/LimitedByGuaranteeCharity
    Model depth: 6
    """

    type_: str = Field("LimitedByGuaranteeCharity", const=True, alias="@type")


if TYPE_CHECKING:

    LimitedByGuaranteeCharity.update_forward_refs()
