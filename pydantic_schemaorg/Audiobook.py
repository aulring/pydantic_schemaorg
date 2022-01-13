from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.AudioObject import AudioObject

from pydantic_schemaorg.Book import Book


class Audiobook(AudioObject, Book):
    """An audiobook.

    See: https://schema.org/Audiobook
    Model depth: 4
    """

    type_: str = Field("Audiobook", const=True, alias="@type")
    duration: "Optional[Union[List[Union[Duration, str]], Union[Duration, str]]]" = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    readBy: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="A person who reads (performs) the audiobook.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Duration import Duration

    from pydantic_schemaorg.Person import Person

    Audiobook.update_forward_refs()
