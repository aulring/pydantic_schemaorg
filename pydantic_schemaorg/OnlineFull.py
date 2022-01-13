from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OnlineFull(GameServerStatus):
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number"
     "of players has reached.

    See: https://schema.org/OnlineFull
    Model depth: 6
    """

    type_: str = Field("OnlineFull", const=True, alias="@type")


if TYPE_CHECKING:

    OnlineFull.update_forward_refs()
