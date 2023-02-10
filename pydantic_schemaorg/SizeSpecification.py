from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic_schemaorg.StructuredValue import StructuredValue
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.GenderType import GenderType
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.QualitativeValue import QualitativeValue
from pydantic_schemaorg.Property import Property
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration
from pydantic_schemaorg.Enumeration import Enumeration
from pydantic_schemaorg.Class import Class
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
from pydantic_schemaorg.SizeGroupEnumeration import SizeGroupEnumeration
from pydantic_schemaorg.CreativeWork import CreativeWork


class SizeSpecification(BaseModel):
    """Size related properties of a product, typically a size code ([[name]]) and optionally"
     "a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]])."
     "In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]],"
     "and suggested body measurements ([[suggestedMeasurement]]).

    See: https://schema.org/SizeSpecification
    Model depth: 5
    """
    type_: str = Field(default="SizeSpecification", alias='@type', const=True)
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
    supersededBy: Optional[Union[List[Union[Any, dynamic_creation('Class'), dynamic_creation('Property'), str]], Any, dynamic_creation('Class'), dynamic_creation('Property'), str]] = Field(
        default=None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    greater: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than the object.",
    )
    additionalProperty: Optional[Union[List[Union[dynamic_creation('PropertyValue'), str]], dynamic_creation('PropertyValue'), str]] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g."
     "a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    valueReference: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('PropertyValue'), dynamic_creation('Enumeration'), dynamic_creation('MeasurementTypeEnumeration'), dynamic_creation('DefinedTerm'), Any, dynamic_creation('QuantitativeValue'), dynamic_creation('StructuredValue')]], str, dynamic_creation('Text'), dynamic_creation('PropertyValue'), dynamic_creation('Enumeration'), dynamic_creation('MeasurementTypeEnumeration'), dynamic_creation('DefinedTerm'), Any, dynamic_creation('QuantitativeValue'), dynamic_creation('StructuredValue')]] = Field(
        default=None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",
    )
    equal: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is equal to"
     "the object.",
    )
    lesser: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than the object.",
    )
    greaterOrEqual: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than or equal to the object.",
    )
    lesserOrEqual: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than or equal to the object.",
    )
    nonEqual: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is not equal"
     "to the object.",
    )
    hasMeasurement: Optional[Union[List[Union[dynamic_creation('QuantitativeValue'), str]], dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="A product measurement, for example the inseam of pants, the wheel size of a bicycle, or"
     "the gauge of a screw. Usually an exact measurement, but can also be a range of measurements"
     "for adjustable products, for example belts and ski bindings.",
    )
    suggestedMeasurement: Optional[Union[List[Union[dynamic_creation('QuantitativeValue'), str]], dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="A suggested range of body measurements for the intended audience or person, for example"
     "inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size"
     "chart for wearable products.",
    )
    sizeSystem: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('SizeSystemEnumeration')]], str, dynamic_creation('Text'), dynamic_creation('SizeSystemEnumeration')]] = Field(
        default=None,
        description="The size system used to identify a product's size. Typically either a standard (for example,"
     "\"GS1\" or \"ISO-EN13402\"), country code (for example \"US\" or \"JP\"), or a measuring"
     "system (for example \"Metric\" or \"Imperial\").",
    )
    sizeGroup: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('SizeGroupEnumeration')]], str, dynamic_creation('Text'), dynamic_creation('SizeGroupEnumeration')]] = Field(
        default=None,
        description="The size group (also known as \"size type\") for a product's size. Size groups are common"
     "in the fashion industry to define size segments and suggested audiences for wearable"
     "products. Multiple values can be combined, for example \"men's big and tall\", \"petite"
     "maternity\" or \"regular\"",
    )
    suggestedGender: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('GenderType')]], str, dynamic_creation('Text'), dynamic_creation('GenderType')]] = Field(
        default=None,
        description="The suggested gender of the intended person or audience, for example \"male\", \"female\","
     "or \"unisex\".",
    )
    suggestedAge: Optional[Union[List[Union[dynamic_creation('QuantitativeValue'), str]], dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants,"
     "1-5 years for toddlers.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.Property import Property
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.SizeGroupEnumeration import SizeGroupEnumeration
    from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration
    from pydantic import BaseModel
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.GenderType import GenderType
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Class import Class
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Enumeration import Enumeration
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
