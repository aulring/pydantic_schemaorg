from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.BroadcastChannel import BroadcastChannel
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.BroadcastFrequencySpecification import BroadcastFrequencySpecification
from pydantic_schemaorg.GeoShape import GeoShape
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.AggregateRating import AggregateRating
from pydantic_schemaorg.BroadcastService import BroadcastService
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Language import Language
from pydantic_schemaorg.OfferCatalog import OfferCatalog
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
from pydantic_schemaorg.Review import Review
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Brand import Brand
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.ServiceChannel import ServiceChannel
from pydantic_schemaorg.Product import Product


class RadioBroadcastService(BaseModel):
    """A delivery service through which radio content is provided via broadcast over the air"
     "or online.

    See: https://schema.org/RadioBroadcastService
    Model depth: 5
    """
    type_: str = Field(default="RadioBroadcastService", alias='@type', const=True)
    potentialAction: Optional[Union[List[Union[Action, str]], Action, str]] = Field(
        default=None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",
    )
    mainEntityOfPage: Optional[Union[List[Union[AnyUrl, URL, CreativeWork, str]], AnyUrl, URL, CreativeWork, str]] = Field(
        default=None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",
    )
    subjectOf: Optional[Union[List[Union[Event, CreativeWork, str]], Event, CreativeWork, str]] = Field(
        default=None,
        description="A CreativeWork or Event about this Thing.",
    )
    url: Optional[Union[List[Union[AnyUrl, URL, str]], AnyUrl, URL, str]] = Field(
        default=None,
        description="URL of the item.",
    )
    alternateName: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="An alias for the item.",
    )
    sameAs: Optional[Union[List[Union[AnyUrl, URL, str]], AnyUrl, URL, str]] = Field(
        default=None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",
    )
    description: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="A description of the item.",
    )
    disambiguatingDescription: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",
    )
    identifier: Optional[Union[List[Union[AnyUrl, URL, str, Text, PropertyValue]], AnyUrl, URL, str, Text, PropertyValue]] = Field(
        default=None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",
    )
    image: Optional[Union[List[Union[AnyUrl, URL, ImageObject, str]], AnyUrl, URL, ImageObject, str]] = Field(
        default=None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",
    )
    name: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The name of the item.",
    )
    additionalType: Optional[Union[List[Union[AnyUrl, URL, str]], AnyUrl, URL, str]] = Field(
        default=None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof'"
     "attribute - for multiple types. Schema.org tools may have only weaker understanding"
     "of extra types, in particular those defined externally.",
    )
    serviceArea: Optional[Union[List[Union[AdministrativeArea, GeoShape, Place, str]], AdministrativeArea, GeoShape, Place, str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    broker: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    provider: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    areaServed: Optional[Union[List[Union[str, Text, AdministrativeArea, Place, GeoShape]], str, Text, AdministrativeArea, Place, GeoShape]] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    slogan: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    award: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    termsOfService: Optional[Union[List[Union[AnyUrl, URL, str, Text]], AnyUrl, URL, str, Text]] = Field(
        default=None,
        description="Human-readable terms of service documentation.",
    )
    review: Optional[Union[List[Union[Review, str]], Review, str]] = Field(
        default=None,
        description="A review of the item.",
    )
    availableChannel: Optional[Union[List[Union[ServiceChannel, str]], ServiceChannel, str]] = Field(
        default=None,
        description="A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).",
    )
    isRelatedTo: Optional[Union[List[Union['Service', Product, str]], 'Service', Product, str]] = Field(
        default=None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    serviceAudience: Optional[Union[List[Union[Audience, str]], Audience, str]] = Field(
        default=None,
        description="The audience eligible for this service.",
    )
    isSimilarTo: Optional[Union[List[Union['Service', Product, str]], 'Service', Product, str]] = Field(
        default=None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    audience: Optional[Union[List[Union[Audience, str]], Audience, str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    logo: Optional[Union[List[Union[AnyUrl, URL, ImageObject, str]], AnyUrl, URL, ImageObject, str]] = Field(
        default=None,
        description="An associated logo.",
    )
    providerMobility: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="Indicates the mobility of a provided service (e.g. 'static', 'dynamic').",
    )
    hoursAvailable: Optional[Union[List[Union[OpeningHoursSpecification, str]], OpeningHoursSpecification, str]] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    brand: Optional[Union[List[Union[Brand, Organization, str]], Brand, Organization, str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    serviceOutput: Optional[Union[List[Union[Thing, str]], Thing, str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    produces: Optional[Union[List[Union[Thing, str]], Thing, str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    hasOfferCatalog: Optional[Union[List[Union[OfferCatalog, str]], OfferCatalog, str]] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    category: Optional[Union[List[Union[AnyUrl, URL, str, Text, PhysicalActivityCategory, Thing, CategoryCode]], AnyUrl, URL, str, Text, PhysicalActivityCategory, Thing, CategoryCode]] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    aggregateRating: Optional[Union[List[Union[AggregateRating, str]], AggregateRating, str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    serviceType: Optional[Union[List[Union[str, Text, GovernmentBenefitsType]], str, Text, GovernmentBenefitsType]] = Field(
        default=None,
        description="The type of service being offered, e.g. veterans' benefits, emergency relief, etc.",
    )
    offers: Optional[Union[List[Union[Demand, Offer, str]], Demand, Offer, str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    hasBroadcastChannel: Optional[Union[List[Union[BroadcastChannel, str]], BroadcastChannel, str]] = Field(
        default=None,
        description="A broadcast channel of a broadcast service.",
    )
    parentService: Optional[Union[List[Union['BroadcastService', str]], 'BroadcastService', str]] = Field(
        default=None,
        description="A broadcast service to which the broadcast service may belong to such as regional variations"
     "of a national channel.",
    )
    broadcastAffiliateOf: Optional[Union[List[Union[Organization, str]], Organization, str]] = Field(
        default=None,
        description="The media network(s) whose content is broadcast on this station.",
    )
    broadcaster: Optional[Union[List[Union[Organization, str]], Organization, str]] = Field(
        default=None,
        description="The organization owning or operating the broadcast service.",
    )
    videoFormat: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    broadcastTimezone: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The timezone in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) for which"
     "the service bases its broadcasts.",
    )
    broadcastDisplayName: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The name displayed in the channel guide. For many US affiliates, it is the network name.",
    )
    broadcastFrequency: Optional[Union[List[Union[str, Text, BroadcastFrequencySpecification]], str, Text, BroadcastFrequencySpecification]] = Field(
        default=None,
        description="The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g."
     "87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels,"
     "e.g. \"87 FM\".",
    )
    inLanguage: Optional[Union[List[Union[str, Text, Language]], str, Text, Language]] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    area: Optional[Union[List[Union[Place, str]], Place, str]] = Field(
        default=None,
        description="The area within which users can expect to reach the broadcast service.",
    )
    callSign: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.ServiceChannel import ServiceChannel
    from pydantic_schemaorg.BroadcastChannel import BroadcastChannel
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.OfferCatalog import OfferCatalog
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.BroadcastFrequencySpecification import BroadcastFrequencySpecification
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.AggregateRating import AggregateRating
