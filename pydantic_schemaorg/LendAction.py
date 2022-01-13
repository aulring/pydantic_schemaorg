from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.TransferAction import TransferAction


class LendAction(TransferAction):
    """The act of providing an object under an agreement that it will be returned at a later date."
     "Reciprocal of BorrowAction. Related actions: * [[BorrowAction]]: Reciprocal of LendAction.

    See: https://schema.org/LendAction
    Model depth: 4
    """

    type_: str = Field("LendAction", const=True, alias="@type")
    borrower: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="A sub property of participant. The person that borrows the object being lent.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    LendAction.update_forward_refs()
