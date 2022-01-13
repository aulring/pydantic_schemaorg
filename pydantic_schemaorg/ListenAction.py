from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ListenAction(ConsumeAction):
    """The act of consuming audio content.

    See: https://schema.org/ListenAction
    Model depth: 4
    """

    type_: str = Field("ListenAction", const=True, alias="@type")


if TYPE_CHECKING:

    ListenAction.update_forward_refs()
