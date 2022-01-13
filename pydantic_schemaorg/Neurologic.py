from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Neurologic(MedicalSpecialty):
    """A specific branch of medical science that studies the nerves and nervous system and its"
     "respective disease states.

    See: https://schema.org/Neurologic
    Model depth: 6
    """

    type_: str = Field("Neurologic", const=True, alias="@type")


if TYPE_CHECKING:

    Neurologic.update_forward_refs()
