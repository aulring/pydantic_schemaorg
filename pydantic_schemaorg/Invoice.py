from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Order import Order
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.PriceSpecification import PriceSpecification
from pydantic import Field
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.PaymentMethod import PaymentMethod
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.PaymentStatusType import PaymentStatusType


class Invoice(BaseModel):
    """A statement of the money due for goods or services; a bill.

    See: https://schema.org/Invoice
    Model depth: 3
    """
    type_: str = Field(default="Invoice", alias='@type', const=True)
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
    provider: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    totalPaymentDue: Optional[Union[List[Union[dynamic_creation('MonetaryAmount'), dynamic_creation('PriceSpecification'), str]], dynamic_creation('MonetaryAmount'), dynamic_creation('PriceSpecification'), str]] = Field(
        default=None,
        description="The total amount due.",
    )
    accountId: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The identifier for the account the payment will be applied to.",
    )
    customer: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",
    )
    paymentDue: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), str]], datetime, dynamic_creation('DateTime'), str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    billingPeriod: Optional[Union[List[Union[dynamic_creation('Duration'), str]], dynamic_creation('Duration'), str]] = Field(
        default=None,
        description="The time interval used to compute the invoice.",
    )
    paymentMethodId: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    paymentStatus: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('PaymentStatusType')]], str, dynamic_creation('Text'), dynamic_creation('PaymentStatusType')]] = Field(
        default=None,
        description="The status of payment; whether the invoice has been paid or not.",
    )
    paymentMethod: Optional[Union[List[Union[dynamic_creation('PaymentMethod'), str]], dynamic_creation('PaymentMethod'), str]] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",
    )
    scheduledPaymentDate: Optional[Union[List[Union[date, dynamic_creation('Date'), str]], date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date the invoice is scheduled to be paid.",
    )
    referencesOrder: Optional[Union[List[Union[dynamic_creation('Order'), str]], dynamic_creation('Order'), str]] = Field(
        default=None,
        description="The Order(s) related to this Invoice. One or more Orders may be combined into a single"
     "Invoice.",
    )
    category: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CategoryCode'), dynamic_creation('PhysicalActivityCategory'), dynamic_creation('Thing')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CategoryCode'), dynamic_creation('PhysicalActivityCategory'), dynamic_creation('Thing')]] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    minimumPaymentDue: Optional[Union[List[Union[dynamic_creation('MonetaryAmount'), dynamic_creation('PriceSpecification'), str]], dynamic_creation('MonetaryAmount'), dynamic_creation('PriceSpecification'), str]] = Field(
        default=None,
        description="The minimum payment required at this time.",
    )
    

if TYPE_CHECKING:
    from pydantic import BaseModel
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Order import Order
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.PaymentStatusType import PaymentStatusType
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
