from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.UserInteraction import UserInteraction


class UserPageVisits(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See: https://schema.org/UserPageVisits
    Model depth: 4
    """

    type_: str = Field("UserPageVisits", const=True, alias="@type")


if TYPE_CHECKING:

    UserPageVisits.update_forward_refs()
