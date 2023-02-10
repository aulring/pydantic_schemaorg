from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import datetime, time


from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.ActionAccessSpecification import ActionAccessSpecification
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Time import Time
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.ConsumeAction import ConsumeAction
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.EntryPoint import EntryPoint
from pydantic_schemaorg.ActionStatusType import ActionStatusType
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.VirtualLocation import VirtualLocation
from pydantic_schemaorg.PostalAddress import PostalAddress


class EatAction(BaseModel):
    """The act of swallowing solid objects.

    See: https://schema.org/EatAction
    Model depth: 4
    """
    type_: str = Field(default="EatAction", alias='@type', const=True)
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
    endTime: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), time, dynamic_creation('Time'), str]], datetime, dynamic_creation('DateTime'), time, dynamic_creation('Time'), str]] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    provider: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    startTime: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), time, dynamic_creation('Time'), str]], datetime, dynamic_creation('DateTime'), time, dynamic_creation('Time'), str]] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    result: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="The result produced in the action. E.g. John wrote *a book*.",
    )
    actionStatus: Optional[Union[List[Union[dynamic_creation('ActionStatusType'), str]], dynamic_creation('ActionStatusType'), str]] = Field(
        default=None,
        description="Indicates the current disposition of the Action.",
    )
    agent: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote"
     "a book.",
    )
    instrument: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.",
    )
    object: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="The object upon which the action is carried out, whose state is kept intact or changed."
     "Also known as the semantic roles patient, affected or undergoer (which change their"
     "state) or theme (which doesn't). E.g. John read *a book*.",
    )
    error: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="For failed actions, more information on the cause of the failure.",
    )
    target: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('EntryPoint'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('EntryPoint'), str]] = Field(
        default=None,
        description="Indicates a target EntryPoint, or url, for an Action.",
    )
    location: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('PostalAddress'), dynamic_creation('Place'), dynamic_creation('VirtualLocation')]], str, dynamic_creation('Text'), dynamic_creation('PostalAddress'), dynamic_creation('Place'), dynamic_creation('VirtualLocation')]] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    participant: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Other co-agents that participated in the action indirectly. E.g. John wrote a book with"
     "*Steve*.",
    )
    actionAccessibilityRequirement: Optional[Union[List[Union[dynamic_creation('ActionAccessSpecification'), str]], dynamic_creation('ActionAccessSpecification'), str]] = Field(
        default=None,
        description="A set of requirements that must be fulfilled in order to perform an Action. If more than"
     "one value is specified, fulfilling one set of requirements will allow the Action to be"
     "performed.",
    )
    expectsAcceptanceOf: Optional[Union[List[Union[dynamic_creation('Offer'), str]], dynamic_creation('Offer'), str]] = Field(
        default=None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic import BaseModel
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.ActionStatusType import ActionStatusType
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.EntryPoint import EntryPoint
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ActionAccessSpecification import ActionAccessSpecification
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Thing import Thing
