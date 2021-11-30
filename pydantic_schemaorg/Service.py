from pydantic import Field, AnyUrl
from pydantic_schemaorg.Demand import Demand
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Review import Review
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Intangible import Intangible


class Service(Intangible):
    """A service provided by an organization, e.g. delivery service, print services, etc.

    See https://schema.org/Service.

    """

    offers: Union[List[Union[Demand, Any]], Union[Demand, Any]] = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    areaServed: Union[List[Union[str, Place, Any]], Union[str, Place, Any]] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    serviceOutput: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    providerMobility: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates the mobility of a provided service (e.g. 'static', 'dynamic').",
    )
    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    award: Optional[Union[List[str], str]] = Field(
        None,
        description="An award won by or for this item.",
    )
    termsOfService: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Human-readable terms of service documentation.",
    )
    produces: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The tangible thing generated by the service, e.g. a passport, permit, etc.",
    )
    brand: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    category: Optional[Union[List[Union[AnyUrl, str, Thing, PhysicalActivityCategory]], Union[AnyUrl, str, Thing, PhysicalActivityCategory]]] = Field(
        None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    slogan: Optional[Union[List[str], str]] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    isSimilarTo: Union[List[Union[Product, Any]], Union[Product, Any]] = Field(
        None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    serviceType: Optional[Union[List[Union[str, GovernmentBenefitsType]], Union[str, GovernmentBenefitsType]]] = Field(
        None,
        description="The type of service being offered, e.g. veterans' benefits, emergency relief, etc.",
    )
    logo: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="An associated logo.",
    )
    audience: Optional[Union[List[Audience], Audience]] = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    serviceArea: Union[List[Union[Place, Any]], Union[Place, Any]] = Field(
        None,
        description="The geographic area where the service is provided.",
    )
    hasOfferCatalog: Any = Field(
        None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    isRelatedTo: Union[List[Union[Product, Any]], Union[Product, Any]] = Field(
        None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    hoursAvailable: Any = Field(
        None,
        description="The hours during which this service or contact is available.",
    )
    review: Optional[Union[List[Review], Review]] = Field(
        None,
        description="A review of the item.",
    )
    provider: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    availableChannel: Any = Field(
        None,
        description="A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).",
    )
    broker: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    serviceAudience: Optional[Union[List[Audience], Audience]] = Field(
        None,
        description="The audience eligible for this service.",
    )
    locals().update({"@type": Field("Service", const=True)})


Service.update_forward_refs()