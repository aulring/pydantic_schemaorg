from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Event import Event


class UserInteraction(Event):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See: https://schema.org/UserInteraction
    Model depth: 3
    """

    type_: str = Field("UserInteraction", const=True, alias="@type")


if TYPE_CHECKING:

    UserInteraction.update_forward_refs()
