from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Homeopathic(MedicineSystem):
    """A system of medicine based on the principle that a disease can be cured by a substance that"
     "produces similar symptoms in healthy people.

    See: https://schema.org/Homeopathic
    Model depth: 6
    """

    type_: str = Field("Homeopathic", const=True, alias="@type")


if TYPE_CHECKING:

    Homeopathic.update_forward_refs()
