from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.GeoShape import GeoShape
from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.Brand import Brand
from pydantic import Field
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.AggregateRating import AggregateRating
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.OfferCatalog import OfferCatalog
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.ServiceChannel import ServiceChannel
from pydantic_schemaorg.Review import Review
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebAPI(BaseModel):
    """An application programming interface accessible over Web/Internet technologies.

    See: https://schema.org/WebAPI
    Model depth: 4
    """
    type_: str = Field(default="WebAPI", alias='@type', const=True)
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
    serviceArea: Optional[Union[List[Union[dynamic_creation('GeoShape'), dynamic_creation('Place'), dynamic_creation('AdministrativeArea'), str]], dynamic_creation('GeoShape'), dynamic_creation('Place'), dynamic_creation('AdministrativeArea'), str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    broker: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    provider: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    areaServed: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('AdministrativeArea'), dynamic_creation('Place')]], str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('AdministrativeArea'), dynamic_creation('Place')]] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    slogan: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    award: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    termsOfService: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Human-readable terms of service documentation.",
    )
    review: Optional[Union[List[Union[dynamic_creation('Review'), str]], dynamic_creation('Review'), str]] = Field(
        default=None,
        description="A review of the item.",
    )
    availableChannel: Optional[Union[List[Union[dynamic_creation('ServiceChannel'), str]], dynamic_creation('ServiceChannel'), str]] = Field(
        default=None,
        description="A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).",
    )
    isRelatedTo: Optional[Union[List[Union[dynamic_creation('Product'), Any, str]], dynamic_creation('Product'), Any, str]] = Field(
        default=None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    serviceAudience: Optional[Union[List[Union[dynamic_creation('Audience'), str]], dynamic_creation('Audience'), str]] = Field(
        default=None,
        description="The audience eligible for this service.",
    )
    isSimilarTo: Optional[Union[List[Union[dynamic_creation('Product'), Any, str]], dynamic_creation('Product'), Any, str]] = Field(
        default=None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    audience: Optional[Union[List[Union[dynamic_creation('Audience'), str]], dynamic_creation('Audience'), str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    logo: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]] = Field(
        default=None,
        description="An associated logo.",
    )
    providerMobility: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Indicates the mobility of a provided service (e.g. 'static', 'dynamic').",
    )
    hoursAvailable: Optional[Union[List[Union[dynamic_creation('OpeningHoursSpecification'), str]], dynamic_creation('OpeningHoursSpecification'), str]] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    brand: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Brand'), str]], dynamic_creation('Organization'), dynamic_creation('Brand'), str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    serviceOutput: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    produces: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    hasOfferCatalog: Optional[Union[List[Union[dynamic_creation('OfferCatalog'), str]], dynamic_creation('OfferCatalog'), str]] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    category: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CategoryCode'), dynamic_creation('PhysicalActivityCategory'), dynamic_creation('Thing')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CategoryCode'), dynamic_creation('PhysicalActivityCategory'), dynamic_creation('Thing')]] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    aggregateRating: Optional[Union[List[Union[dynamic_creation('AggregateRating'), str]], dynamic_creation('AggregateRating'), str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    serviceType: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('GovernmentBenefitsType')]], str, dynamic_creation('Text'), dynamic_creation('GovernmentBenefitsType')]] = Field(
        default=None,
        description="The type of service being offered, e.g. veterans' benefits, emergency relief, etc.",
    )
    offers: Optional[Union[List[Union[dynamic_creation('Offer'), dynamic_creation('Demand'), str]], dynamic_creation('Offer'), dynamic_creation('Demand'), str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    documentation: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="Further documentation describing the Web API in more detail.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType
    from pydantic import BaseModel
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.ServiceChannel import ServiceChannel
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.OfferCatalog import OfferCatalog
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
