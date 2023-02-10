from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class Grant(BaseModel):
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a"
     "[[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],"
     "sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in"
     "one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]]"
     "of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s"
     "of resources (e.g. office space). Grants support activities directed towards some"
     "agreed collective goals, often but not always organized as [[Project]]s. Long-lived"
     "projects are sometimes sponsored by a variety of grants over time, but it is also common"
     "for a project to be associated with a single grant. The amount of a [[Grant]] is represented"
     "using [[amount]] as a [[MonetaryAmount]].

    See: https://schema.org/Grant
    Model depth: 3
    """
    type_: str = Field(default="Grant", alias='@type', const=True)
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
    fundedItem: Optional[Union[List[Union[MedicalEntity, Organization, Person, Event, Product, BioChemEntity, CreativeWork, str]], MedicalEntity, Organization, Person, Event, Product, BioChemEntity, CreativeWork, str]] = Field(
        default=None,
        description="Indicates something directly or indirectly funded or sponsored through a [[Grant]]."
     "See also [[ownershipFundingInfo]].",
    )
    funder: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    sponsor: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.BioChemEntity import BioChemEntity
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.ImageObject import ImageObject
