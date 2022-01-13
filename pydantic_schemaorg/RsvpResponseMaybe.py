from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.RsvpResponseType import RsvpResponseType


class RsvpResponseMaybe(RsvpResponseType):
    """The invitee may or may not attend.

    See: https://schema.org/RsvpResponseMaybe
    Model depth: 5
    """

    type_: str = Field("RsvpResponseMaybe", const=True, alias="@type")


if TYPE_CHECKING:

    RsvpResponseMaybe.update_forward_refs()
