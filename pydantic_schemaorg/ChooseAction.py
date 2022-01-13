from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.AssessAction import AssessAction


class ChooseAction(AssessAction):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    See: https://schema.org/ChooseAction
    Model depth: 4
    """

    type_: str = Field("ChooseAction", const=True, alias="@type")
    option: "Optional[Union[List[Union[str, Thing]], Union[str, Thing]]]" = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )
    actionOption: "Optional[Union[List[Union[str, Thing]], Union[str, Thing]]]" = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Thing import Thing

    ChooseAction.update_forward_refs()
