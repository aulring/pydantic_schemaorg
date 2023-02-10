from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from datetime import date, datetime
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.PostalAddress import PostalAddress
from pydantic_schemaorg.DeliveryEvent import DeliveryEvent
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Order import Order
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Product import Product


class ParcelDelivery(BaseModel):
    """The delivery of a parcel either via the postal service or a commercial service.

    See: https://schema.org/ParcelDelivery
    Model depth: 3
    """
    type_: str = Field(default="ParcelDelivery", alias='@type', const=True)
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
    itemShipped: Optional[Union[List[Union[Product, str]], Product, str]] = Field(
        default=None,
        description="Item(s) being shipped.",
    )
    trackingNumber: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="Shipper tracking number.",
    )
    expectedArrivalUntil: Optional[Union[List[Union[datetime, DateTime, date, Date, str]], datetime, DateTime, date, Date, str]] = Field(
        default=None,
        description="The latest date the package may arrive.",
    )
    provider: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    deliveryAddress: Optional[Union[List[Union[PostalAddress, str]], PostalAddress, str]] = Field(
        default=None,
        description="Destination address.",
    )
    expectedArrivalFrom: Optional[Union[List[Union[datetime, DateTime, date, Date, str]], datetime, DateTime, date, Date, str]] = Field(
        default=None,
        description="The earliest date the package may arrive.",
    )
    carrier: Optional[Union[List[Union[Organization, str]], Organization, str]] = Field(
        default=None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    originAddress: Optional[Union[List[Union[PostalAddress, str]], PostalAddress, str]] = Field(
        default=None,
        description="Shipper's address.",
    )
    deliveryStatus: Optional[Union[List[Union[DeliveryEvent, str]], DeliveryEvent, str]] = Field(
        default=None,
        description="New entry added as the package passes through each leg of its journey (from shipment to"
     "final delivery).",
    )
    trackingUrl: Optional[Union[List[Union[AnyUrl, URL, str]], AnyUrl, URL, str]] = Field(
        default=None,
        description="Tracking url for the parcel delivery.",
    )
    partOfOrder: Optional[Union[List[Union[Order, str]], Order, str]] = Field(
        default=None,
        description="The overall order the items in this delivery were included in.",
    )
    hasDeliveryMethod: Optional[Union[List[Union[DeliveryMethod, str]], DeliveryMethod, str]] = Field(
        default=None,
        description="Method used for delivery or shipping.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Order import Order
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.DeliveryEvent import DeliveryEvent
