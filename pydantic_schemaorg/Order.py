from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from datetime import date, datetime
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.OrderStatus import OrderStatus
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.Invoice import Invoice
from pydantic_schemaorg.Boolean import Boolean
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.OrderItem import OrderItem
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Number import Number
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.ParcelDelivery import ParcelDelivery
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.PaymentMethod import PaymentMethod
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.PostalAddress import PostalAddress


class Order(BaseModel):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line"
     "items, each represented by an Offer that has been accepted by the customer.

    See: https://schema.org/Order
    Model depth: 3
    """
    type_: str = Field(default="Order", alias='@type', const=True)
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
    orderStatus: Optional[Union[List[Union[dynamic_creation('OrderStatus'), str]], dynamic_creation('OrderStatus'), str]] = Field(
        default=None,
        description="The current status of the order.",
    )
    isGift: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="Indicates whether the offer was accepted as a gift for someone other than the buyer.",
    )
    confirmationNumber: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",
    )
    broker: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    paymentDueDate: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    seller: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    discount: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]], StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Any discount applied (to an Order).",
    )
    discountCurrency: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The currency of the discount. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    customer: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",
    )
    paymentDue: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), str]], datetime, dynamic_creation('DateTime'), str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    acceptedOffer: Optional[Union[List[Union[dynamic_creation('Offer'), str]], dynamic_creation('Offer'), str]] = Field(
        default=None,
        description="The offer(s) -- e.g., product, quantity and price combinations -- included in the order.",
    )
    paymentMethodId: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    merchant: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="'merchant' is an out-dated term for 'seller'.",
    )
    partOfInvoice: Optional[Union[List[Union[dynamic_creation('Invoice'), str]], dynamic_creation('Invoice'), str]] = Field(
        default=None,
        description="The order is being paid as part of the referenced Invoice.",
    )
    orderNumber: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The identifier of the transaction.",
    )
    paymentMethod: Optional[Union[List[Union[dynamic_creation('PaymentMethod'), str]], dynamic_creation('PaymentMethod'), str]] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",
    )
    discountCode: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Code used to redeem a discount.",
    )
    orderDelivery: Optional[Union[List[Union[dynamic_creation('ParcelDelivery'), str]], dynamic_creation('ParcelDelivery'), str]] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",
    )
    orderedItem: Optional[Union[List[Union[dynamic_creation('Product'), dynamic_creation('OrderItem'), dynamic_creation('Service'), str]], dynamic_creation('Product'), dynamic_creation('OrderItem'), dynamic_creation('Service'), str]] = Field(
        default=None,
        description="The item ordered.",
    )
    billingAddress: Optional[Union[List[Union[dynamic_creation('PostalAddress'), str]], dynamic_creation('PostalAddress'), str]] = Field(
        default=None,
        description="The billing address for the order.",
    )
    paymentUrl: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="The URL for sending a payment.",
    )
    orderDate: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="Date order was placed.",
    )
    

if TYPE_CHECKING:
    from pydantic import BaseModel
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.OrderStatus import OrderStatus
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.OrderItem import OrderItem
    from pydantic_schemaorg.Invoice import Invoice
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.ParcelDelivery import ParcelDelivery
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Service import Service
