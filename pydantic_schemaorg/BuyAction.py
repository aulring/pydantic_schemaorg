from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.TradeAction import TradeAction


class BuyAction(TradeAction):
    """The act of giving money to a seller in exchange for goods or services rendered. An agent"
     "buys an object, product, or service from a seller for a price. Reciprocal of SellAction.

    See: https://schema.org/BuyAction
    Model depth: 4
    """

    type_: str = Field("BuyAction", const=True, alias="@type")
    vendor: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="'vendor' is an earlier term for 'seller'.",
    )
    seller: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
        "also be a provider.",
    )
    warrantyPromise: "Optional[Union[List[Union[WarrantyPromise, str]], Union[WarrantyPromise, str]]]" = Field(
        None,
        description="The warranty promise(s) included in the offer.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    from pydantic_schemaorg.WarrantyPromise import WarrantyPromise

    BuyAction.update_forward_refs()
