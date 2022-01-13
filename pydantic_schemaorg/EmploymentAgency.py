from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EmploymentAgency(LocalBusiness):
    """An employment agency.

    See: https://schema.org/EmploymentAgency
    Model depth: 4
    """

    type_: str = Field("EmploymentAgency", const=True, alias="@type")


if TYPE_CHECKING:

    EmploymentAgency.update_forward_refs()
