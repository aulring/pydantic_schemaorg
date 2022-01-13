from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EventStatusType import EventStatusType


class EventScheduled(EventStatusType):
    """The event is taking place or has taken place on the startDate as scheduled. Use of this"
     "value is optional, as it is assumed by default.

    See: https://schema.org/EventScheduled
    Model depth: 6
    """

    type_: str = Field("EventScheduled", const=True, alias="@type")


if TYPE_CHECKING:

    EventScheduled.update_forward_refs()
