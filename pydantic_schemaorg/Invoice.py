from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class Invoice(BaseModel):
    """A statement of the money due for goods or services; a bill.

    See: https://schema.org/Invoice
    Model depth: 3
    """
    type_: str = Field(default="Invoice", alias='@type', const=True)
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
    confirmationNumber: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",
    )
    broker: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    paymentDueDate: Optional[Union[List[Union[datetime, date, Any, str]], datetime, date, Any, str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    provider: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    totalPaymentDue: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The total amount due.",
    )
    accountId: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The identifier for the account the payment will be applied to.",
    )
    customer: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",
    )
    paymentDue: Optional[Union[List[Union[datetime, Any, str]], datetime, Any, str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    billingPeriod: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The time interval used to compute the invoice.",
    )
    paymentMethodId: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    paymentStatus: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The status of payment; whether the invoice has been paid or not.",
    )
    paymentMethod: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",
    )
    scheduledPaymentDate: Optional[Union[List[Union[date, Any, str]], date, Any, str]] = Field(
        default=None,
        description="The date the invoice is scheduled to be paid.",
    )
    referencesOrder: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The Order(s) related to this Invoice. One or more Orders may be combined into a single"
     "Invoice.",
    )
    category: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    minimumPaymentDue: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The minimum payment required at this time.",
    )
    
