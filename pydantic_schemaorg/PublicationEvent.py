from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Event import Event


class PublicationEvent(Event):
    """A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork"
     "of any type e.g. a broadcast event, an on-demand event, a book/journal publication via"
     "a variety of delivery media.

    See: https://schema.org/PublicationEvent
    Model depth: 3
    """

    type_: str = Field("PublicationEvent", const=True, alias="@type")
    publishedBy: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="An agent associated with the publication event.",
    )
    publishedOn: "Optional[Union[List[Union[BroadcastService, str]], Union[BroadcastService, str]]]" = Field(
        None,
        description="A broadcast service associated with the publication event.",
    )
    free: "Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]]" = Field(
        None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    from pydantic_schemaorg.BroadcastService import BroadcastService

    from pydantic import StrictBool

    PublicationEvent.update_forward_refs()
