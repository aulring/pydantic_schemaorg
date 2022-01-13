from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Offer import Offer


class AggregateOffer(Offer):
    """When a single product is associated with multiple offers (for example, the same pair"
     "of shoes is offered by different merchants), then AggregateOffer can be used. Note:"
     "AggregateOffers are normally expected to associate multiple offers that all share"
     "the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell"
     "if businessFunction is not explicitly defined.

    See: https://schema.org/AggregateOffer
    Model depth: 4
    """

    type_: str = Field("AggregateOffer", const=True, alias="@type")
    offers: "Optional[Union[List[Union[Demand, Offer, str]], Union[Demand, Offer, str]]]" = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
        "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
        "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
        "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
        "of common types, it can be used in others. In that case, using a second type, such as Product"
        "or a subtype of Product, can clarify the nature of the offer.",
    )
    lowPrice: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="The lowest price of all offers available. Usage guidelines: * Use values from 0123456789"
        "(Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
        "similiar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to"
        "indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    highPrice: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="The highest price of all offers available. Usage guidelines: * Use values from 0123456789"
        "(Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
        "similiar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to"
        "indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    offerCount: "Optional[Union[List[Union[int, str]], Union[int, str]]]" = Field(
        None,
        description="The number of offers for the product.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Demand import Demand

    from pydantic_schemaorg.Offer import Offer

    from decimal import Decimal

    AggregateOffer.update_forward_refs()
