from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Rheumatologic(MedicalSpecialty):
    """A specific branch of medical science that deals with the study and treatment of rheumatic,"
     "autoimmune or joint diseases.

    See: https://schema.org/Rheumatologic
    Model depth: 6
    """

    type_: str = Field("Rheumatologic", const=True, alias="@type")


if TYPE_CHECKING:

    Rheumatologic.update_forward_refs()
