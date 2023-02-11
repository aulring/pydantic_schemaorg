from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class RadioBroadcastService(BaseModel):
    """A delivery service through which radio content is provided via broadcast over the air"
     "or online.

    See: https://schema.org/RadioBroadcastService
    Model depth: 5
    """
    type_: str = Field(default="RadioBroadcastService", alias='@type', const=True)
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
    serviceArea: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
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
    areaServed: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    slogan: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    award: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    termsOfService: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,
        description="Human-readable terms of service documentation.",
    )
    review: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A review of the item.",
    )
    availableChannel: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).",
    )
    isRelatedTo: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    serviceAudience: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The audience eligible for this service.",
    )
    isSimilarTo: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    audience: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    logo: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,
        description="An associated logo.",
    )
    providerMobility: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Indicates the mobility of a provided service (e.g. 'static', 'dynamic').",
    )
    hoursAvailable: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    brand: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    serviceOutput: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    produces: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    hasOfferCatalog: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    category: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    aggregateRating: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    serviceType: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The type of service being offered, e.g. veterans' benefits, emergency relief, etc.",
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
    hasBroadcastChannel: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A broadcast channel of a broadcast service.",
    )
    parentService: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A broadcast service to which the broadcast service may belong to such as regional variations"
     "of a national channel.",
    )
    broadcastAffiliateOf: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The media network(s) whose content is broadcast on this station.",
    )
    broadcaster: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The organization owning or operating the broadcast service.",
    )
    videoFormat: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    broadcastTimezone: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The timezone in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) for which"
     "the service bases its broadcasts.",
    )
    broadcastDisplayName: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The name displayed in the channel guide. For many US affiliates, it is the network name.",
    )
    broadcastFrequency: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g."
     "87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels,"
     "e.g. \"87 FM\".",
    )
    inLanguage: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    area: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The area within which users can expect to reach the broadcast service.",
    )
    callSign: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",
    )
    
