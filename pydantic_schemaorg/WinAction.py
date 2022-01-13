from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.AchieveAction import AchieveAction


class WinAction(AchieveAction):
    """The act of achieving victory in a competitive activity.

    See: https://schema.org/WinAction
    Model depth: 4
    """

    type_: str = Field("WinAction", const=True, alias="@type")
    loser: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="A sub property of participant. The loser of the action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    WinAction.update_forward_refs()
