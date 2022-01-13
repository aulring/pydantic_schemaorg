from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicineSystem(MedicalEnumeration):
    """Systems of medical practice.

    See: https://schema.org/MedicineSystem
    Model depth: 5
    """

    type_: str = Field("MedicineSystem", const=True, alias="@type")


if TYPE_CHECKING:

    MedicineSystem.update_forward_refs()
