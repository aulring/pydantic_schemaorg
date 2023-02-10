from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool


from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.Text import Text
from pydantic import Field
from pydantic_schemaorg.ShippingDeliveryTime import ShippingDeliveryTime
from pydantic_schemaorg.StructuredValue import StructuredValue
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.DefinedRegion import DefinedRegion
from pydantic_schemaorg.Distance import Distance
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from pydantic_schemaorg.Boolean import Boolean


class OfferShippingDetails(BaseModel):
    """OfferShippingDetails represents information about shipping destinations. Multiple"
     "of these entities can be used to represent different shipping rates for different destinations:"
     "One entity for Alaska/Hawaii. A different one for continental US. A different one for"
     "all France. Multiple of these entities can be used to represent different shipping costs"
     "and delivery times. Two entities that are identical but differ in rate and time: E.g."
     "Cheaper and slower: $5 in 5-7 days or Fast and expensive: $15 in 1-2 days.

    See: https://schema.org/OfferShippingDetails
    Model depth: 4
    """
    type_: str = Field(default="OfferShippingDetails", alias='@type', const=True)
    potentialAction: Optional[Union[List[Union[dynamic_creation('Action'), str]], dynamic_creation('Action'), str]] = Field(
        default=None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",
    )
    mainEntityOfPage: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",
    )
    subjectOf: Optional[Union[List[Union[dynamic_creation('CreativeWork'), dynamic_creation('Event'), str]], dynamic_creation('CreativeWork'), dynamic_creation('Event'), str]] = Field(
        default=None,
        description="A CreativeWork or Event about this Thing.",
    )
    url: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="URL of the item.",
    )
    alternateName: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An alias for the item.",
    )
    sameAs: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",
    )
    description: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A description of the item.",
    )
    disambiguatingDescription: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",
    )
    identifier: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('PropertyValue')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('PropertyValue')]] = Field(
        default=None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",
    )
    image: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]] = Field(
        default=None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",
    )
    name: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The name of the item.",
    )
    additionalType: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof'"
     "attribute - for multiple types. Schema.org tools may have only weaker understanding"
     "of extra types, in particular those defined externally.",
    )
    width: Optional[Union[List[Union[dynamic_creation('Distance'), dynamic_creation('QuantitativeValue'), str]], dynamic_creation('Distance'), dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="The width of the item.",
    )
    shippingSettingsLink: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="Link to a page containing [[ShippingRateSettings]] and [[DeliveryTimeSettings]]"
     "details.",
    )
    depth: Optional[Union[List[Union[dynamic_creation('Distance'), dynamic_creation('QuantitativeValue'), str]], dynamic_creation('Distance'), dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="The depth of the item.",
    )
    shippingDestination: Optional[Union[List[Union[dynamic_creation('DefinedRegion'), str]], dynamic_creation('DefinedRegion'), str]] = Field(
        default=None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
     "ways, e.g. postalCode ranges.",
    )
    shippingLabel: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    height: Optional[Union[List[Union[dynamic_creation('Distance'), dynamic_creation('QuantitativeValue'), str]], dynamic_creation('Distance'), dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="The height of the item.",
    )
    doesNotShip: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    weight: Optional[Union[List[Union[dynamic_creation('QuantitativeValue'), str]], dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    deliveryTime: Optional[Union[List[Union[dynamic_creation('ShippingDeliveryTime'), str]], dynamic_creation('ShippingDeliveryTime'), str]] = Field(
        default=None,
        description="The total delay between the receipt of the order and the goods reaching the final customer.",
    )
    shippingOrigin: Optional[Union[List[Union[dynamic_creation('DefinedRegion'), str]], dynamic_creation('DefinedRegion'), str]] = Field(
        default=None,
        description="Indicates the origin of a shipment, i.e. where it should be coming from.",
    )
    transitTimeLabel: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    shippingRate: Optional[Union[List[Union[dynamic_creation('MonetaryAmount'), str]], dynamic_creation('MonetaryAmount'), str]] = Field(
        default=None,
        description="The shipping rate is the cost of shipping to the specified destination. Typically, the"
     "maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ShippingDeliveryTime import ShippingDeliveryTime
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic import BaseModel
    from pydantic_schemaorg.DefinedRegion import DefinedRegion
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.URL import URL
