from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class LodgingReservation(BaseModel):
    """A reservation for lodging at a hotel, motel, inn, etc. Note: This type is for information"
     "about actual reservations, e.g. in confirmation emails or HTML pages with individual"
     "confirmations of reservations.

    See: https://schema.org/LodgingReservation
    Model depth: 4
    """
    type_: str = Field(default="LodgingReservation", alias='@type', const=True)
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
    broker: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    provider: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    modifiedTime: Optional[Union[List[Union[datetime, Any, str]], datetime, Any, str]] = Field(
        default=None,
        description="The date and time the reservation was modified.",
    )
    programMembershipUsed: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the"
     "reservation.",
    )
    bookingAgent: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent.",
    )
    totalPrice: Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str] = Field(
        default=None,
        description="The total price for the reservation or ticket, including applicable taxes, shipping,"
     "etc. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",
    )
    reservedTicket: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A ticket associated with the reservation.",
    )
    reservationId: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A unique identifier for the reservation.",
    )
    reservationFor: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The thing -- flight, event, restaurant, etc. being reserved.",
    )
    underName: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The person or organization the reservation or ticket is for.",
    )
    bookingTime: Optional[Union[List[Union[datetime, Any, str]], datetime, Any, str]] = Field(
        default=None,
        description="The date and time the reservation was booked.",
    )
    reservationStatus: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The current status of the reservation.",
    )
    priceCurrency: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    checkoutTime: Optional[Union[List[Union[datetime, Any, time, str]], datetime, Any, time, str]] = Field(
        default=None,
        description="The latest someone may check out of a lodging establishment.",
    )
    lodgingUnitType: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Textual description of the unit type (including suite vs. room, size of bed, etc.).",
    )
    numChildren: Optional[Union[List[Union[Any, int, str]], Any, int, str]] = Field(
        default=None,
        description="The number of children staying in the unit.",
    )
    numAdults: Optional[Union[List[Union[Any, int, str]], Any, int, str]] = Field(
        default=None,
        description="The number of adults staying in the unit.",
    )
    checkinTime: Optional[Union[List[Union[datetime, Any, time, str]], datetime, Any, time, str]] = Field(
        default=None,
        description="The earliest someone may check into a lodging establishment.",
    )
    lodgingUnitDescription: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A full description of the lodging unit.",
    )
    
