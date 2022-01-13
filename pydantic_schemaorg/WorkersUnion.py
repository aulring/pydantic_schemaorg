from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Organization import Organization


class WorkersUnion(Organization):
    """A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization"
     "that promotes the interests of its worker members by collectively bargaining with management,"
     "organizing, and political lobbying.

    See: https://schema.org/WorkersUnion
    Model depth: 3
    """

    type_: str = Field("WorkersUnion", const=True, alias="@type")


if TYPE_CHECKING:

    WorkersUnion.update_forward_refs()
