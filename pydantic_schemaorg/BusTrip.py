from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class BusTrip(BaseModel):
    """A trip on a commercial bus line.

    See: https://schema.org/BusTrip
    Model depth: 4
    """
    type_: str = Field(default="BusTrip", alias='@type', const=True)
    potentialAction: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",
    )
    mainEntityOfPage: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",
    )
    subjectOf: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A CreativeWork or Event about this Thing.",
    )
    url: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,
        description="URL of the item.",
    )
    alternateName: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="An alias for the item.",
    )
    sameAs: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",
    )
    description: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A description of the item.",
    )
    disambiguatingDescription: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",
    )
    identifier: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",
    )
    image: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",
    )
    name: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The name of the item.",
    )
    additionalType: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof'"
     "attribute - for multiple types. Schema.org tools may have only weaker understanding"
     "of extra types, in particular those defined externally.",
    )
    departureTime: Optional[Union[List[Union[datetime, Any, time, str]], datetime, Any, time, str]] = Field(
        default=None,
        description="The expected departure time.",
    )
    itinerary: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is"
     "important use [[ItemList]] to specify that order (see examples).",
    )
    provider: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    partOfTrip: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Identifies that this [[Trip]] is a subTrip of another Trip. For example Day 1, Day 2, etc."
     "of a multi-day trip.",
    )
    arrivalTime: Optional[Union[List[Union[datetime, Any, time, str]], datetime, Any, time, str]] = Field(
        default=None,
        description="The expected arrival time.",
    )
    subTrip: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Identifies a [[Trip]] that is a subTrip of this Trip. For example Day 1, Day 2, etc. of a"
     "multi-day trip.",
    )
    offers: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    busName: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The name of the bus (e.g. Bolt Express).",
    )
    busNumber: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The unique identifier for the bus.",
    )
    departureBusStop: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The stop or station from which the bus departs.",
    )
    arrivalBusStop: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The stop or station from which the bus arrives.",
    )
    
