from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.GenderType import GenderType
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Integer import Integer
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Number import Number
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Action import Action


class PeopleAudience(BaseModel):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    See: https://schema.org/PeopleAudience
    Model depth: 4
    """
    type_: str = Field(default="PeopleAudience", alias='@type', const=True)
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
    audienceType: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The target group associated with a given audience (e.g. veterans, car owners, musicians,"
     "etc.).",
    )
    geographicArea: Optional[Union[List[Union[AdministrativeArea, str]], AdministrativeArea, str]] = Field(
        default=None,
        description="The geographic area associated with the audience.",
    )
    healthCondition: Optional[Union[List[Union[MedicalCondition, str]], MedicalCondition, str]] = Field(
        default=None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    requiredGender: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="Audiences defined by a person's gender.",
    )
    suggestedMinAge: Optional[Union[List[Union[StrictInt, StrictFloat, Number, str]], StrictInt, StrictFloat, Number, str]] = Field(
        default=None,
        description="Minimum recommended age in years for the audience or user.",
    )
    requiredMinAge: Optional[Union[List[Union[int, Integer, str]], int, Integer, str]] = Field(
        default=None,
        description="Audiences defined by a person's minimum age.",
    )
    suggestedMeasurement: Optional[Union[List[Union[QuantitativeValue, str]], QuantitativeValue, str]] = Field(
        default=None,
        description="A suggested range of body measurements for the intended audience or person, for example"
     "inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size"
     "chart for wearable products.",
    )
    suggestedGender: Optional[Union[List[Union[str, Text, GenderType]], str, Text, GenderType]] = Field(
        default=None,
        description="The suggested gender of the intended person or audience, for example \"male\", \"female\","
     "or \"unisex\".",
    )
    requiredMaxAge: Optional[Union[List[Union[int, Integer, str]], int, Integer, str]] = Field(
        default=None,
        description="Audiences defined by a person's maximum age.",
    )
    suggestedAge: Optional[Union[List[Union[QuantitativeValue, str]], QuantitativeValue, str]] = Field(
        default=None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants,"
     "1-5 years for toddlers.",
    )
    suggestedMaxAge: Optional[Union[List[Union[StrictInt, StrictFloat, Number, str]], StrictInt, StrictFloat, Number, str]] = Field(
        default=None,
        description="Maximum recommended age in years for the audience or user.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.GenderType import GenderType
    from pydantic_schemaorg.ImageObject import ImageObject
