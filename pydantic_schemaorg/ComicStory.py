from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class ComicStory(CreativeWork):
    """The term \"story\" is any indivisible, re-printable unit of a comic, including the interior"
     "stories, covers, and backmatter. Most comics have at least two stories: a cover (ComicCoverArt)"
     "and an interior story.

    See: https://schema.org/ComicStory
    Model depth: 3
    """

    type_: str = Field("ComicStory", const=True, alias="@type")
    colorist: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="The individual who adds color to inked drawings.",
    )
    artist: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="The primary artist for a work in a medium other than pencils or digital line art--for example,"
        "if the primary artwork is done in watercolors or digital paints.",
    )
    letterer: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="The individual who adds lettering, including speech balloons and sound effects, to"
        "artwork.",
    )
    penciler: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="The individual who draws the primary narrative artwork.",
    )
    inker: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="The individual who traces over the pencil drawings in ink after pencils are complete.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    ComicStory.update_forward_refs()
