from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Service import Service


class GovernmentService(Service):
    """A service provided by a government organization, e.g. food stamps, veterans benefits,"
     "etc.

    See: https://schema.org/GovernmentService
    Model depth: 4
    """

    type_: str = Field("GovernmentService", const=True, alias="@type")
    jurisdiction: "Optional[Union[List[Union[str, AdministrativeArea]], Union[str, AdministrativeArea]]]" = Field(
        None,
        description="Indicates a legal jurisdiction, e.g. of some legislation, or where some government"
        "service is based.",
    )
    serviceOperator: "Optional[Union[List[Union[Organization, str]], Union[Organization, str]]]" = Field(
        None,
        description="The operating organization, if different from the provider. This enables the representation"
        "of services that are provided by an organization, but operated by another organization"
        "like a subcontractor.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea

    from pydantic_schemaorg.Organization import Organization

    GovernmentService.update_forward_refs()
