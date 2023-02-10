from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import datetime, time
from pydantic import AnyUrl
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.WarrantyPromise import WarrantyPromise
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.PriceSpecification import PriceSpecification
from pydantic_schemaorg.EntryPoint import EntryPoint
from pydantic_schemaorg.Number import Number
from pydantic_schemaorg.Time import Time
from pydantic_schemaorg.ActionStatusType import ActionStatusType
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.PostalAddress import PostalAddress
from pydantic_schemaorg.VirtualLocation import VirtualLocation
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Place import Place


class BuyAction(BaseModel):
    """The act of giving money to a seller in exchange for goods or services rendered. An agent"
     "buys an object, product, or service from a seller for a price. Reciprocal of SellAction.

    See: https://schema.org/BuyAction
    Model depth: 4
    """
    type_: str = Field(default="BuyAction", alias='@type', const=True)
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
    endTime: Optional[Union[List[Union[datetime, DateTime, time, Time, str]], datetime, DateTime, time, Time, str]] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    provider: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    startTime: Optional[Union[List[Union[datetime, DateTime, time, Time, str]], datetime, DateTime, time, Time, str]] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    result: Optional[Union[List[Union[Thing, str]], Thing, str]] = Field(
        default=None,
        description="The result produced in the action. E.g. John wrote *a book*.",
    )
    actionStatus: Optional[Union[List[Union[ActionStatusType, str]], ActionStatusType, str]] = Field(
        default=None,
        description="Indicates the current disposition of the Action.",
    )
    agent: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote"
     "a book.",
    )
    instrument: Optional[Union[List[Union[Thing, str]], Thing, str]] = Field(
        default=None,
        description="The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.",
    )
    object: Optional[Union[List[Union[Thing, str]], Thing, str]] = Field(
        default=None,
        description="The object upon which the action is carried out, whose state is kept intact or changed."
     "Also known as the semantic roles patient, affected or undergoer (which change their"
     "state) or theme (which doesn't). E.g. John read *a book*.",
    )
    error: Optional[Union[List[Union[Thing, str]], Thing, str]] = Field(
        default=None,
        description="For failed actions, more information on the cause of the failure.",
    )
    target: Optional[Union[List[Union[AnyUrl, URL, EntryPoint, str]], AnyUrl, URL, EntryPoint, str]] = Field(
        default=None,
        description="Indicates a target EntryPoint, or url, for an Action.",
    )
    location: Optional[Union[List[Union[str, Text, Place, VirtualLocation, PostalAddress]], str, Text, Place, VirtualLocation, PostalAddress]] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    participant: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="Other co-agents that participated in the action indirectly. E.g. John wrote a book with"
     "*Steve*.",
    )
    price: Optional[Union[List[Union[StrictInt, StrictFloat, Number, str, Text]], StrictInt, StrictFloat, Number, str, Text]] = Field(
        default=None,
        description="The offer price of a product, or of a price component when attached to PriceSpecification"
     "and its subtypes. Usage guidelines: * Use the [[priceCurrency]] property (with standard"
     "formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\") instead of including [ambiguous"
     "symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign)"
     "such as '$' in the value. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate"
     "a decimal point. Avoid using these symbols as a readability separator. * Note that both"
     "[RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute)"
     "and Microdata syntax allow the use of a \"content=\" attribute for publishing simple"
     "machine-readable values alongside more human-friendly formatting. * Use values from"
     "0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
     "similar Unicode symbols.",
    )
    priceSpecification: Optional[Union[List[Union[PriceSpecification, str]], PriceSpecification, str]] = Field(
        default=None,
        description="One or more detailed price specifications, indicating the unit price and delivery or"
     "payment charges.",
    )
    priceCurrency: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    seller: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    warrantyPromise: Optional[Union[List[Union[WarrantyPromise, str]], WarrantyPromise, str]] = Field(
        default=None,
        description="The warranty promise(s) included in the offer.",
    )
    vendor: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="'vendor' is an earlier term for 'seller'.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.WarrantyPromise import WarrantyPromise
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ActionStatusType import ActionStatusType
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.EntryPoint import EntryPoint
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Person import Person
