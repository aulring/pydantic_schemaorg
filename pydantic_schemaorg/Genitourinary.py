from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Genitourinary(PhysicalExam):
    """Genitourinary system function assessment with clinical examination.

    See: https://schema.org/Genitourinary
    Model depth: 5
    """

    type_: str = Field("Genitourinary", const=True, alias="@type")


if TYPE_CHECKING:

    Genitourinary.update_forward_refs()
