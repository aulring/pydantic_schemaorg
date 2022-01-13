from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.UserInteraction import UserInteraction


class UserPlays(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See: https://schema.org/UserPlays
    Model depth: 4
    """

    type_: str = Field("UserPlays", const=True, alias="@type")


if TYPE_CHECKING:

    UserPlays.update_forward_refs()
