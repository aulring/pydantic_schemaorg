from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class BusinessEntityType(Enumeration):
    """A business entity type is a conceptual entity representing the legal form, the size,"
     "the main line of business, the position in the value chain, or any combination thereof,"
     "of an organization or business person. Commonly used values: * http://purl.org/goodrelations/v1#Business"
     "* http://purl.org/goodrelations/v1#Enduser * http://purl.org/goodrelations/v1#PublicInstitution"
     "* http://purl.org/goodrelations/v1#Reseller

    See: https://schema.org/BusinessEntityType
    Model depth: 4
    """

    type_: str = Field("BusinessEntityType", const=True, alias="@type")


if TYPE_CHECKING:

    BusinessEntityType.update_forward_refs()
