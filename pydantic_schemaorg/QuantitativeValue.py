from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic_schemaorg.StructuredValue import StructuredValue
from pydantic_schemaorg.Text import Text
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.QualitativeValue import QualitativeValue
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Number import Number
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Enumeration import Enumeration
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.Boolean import Boolean


class QuantitativeValue(BaseModel):
    """A point value or interval for product characteristics and other purposes.

    See: https://schema.org/QuantitativeValue
    Model depth: 4
    """
    type_: str = Field(default="QuantitativeValue", alias='@type', const=True)
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
    value: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), StrictBool, dynamic_creation('Boolean'), str, dynamic_creation('Text'), dynamic_creation('StructuredValue')]], StrictInt, StrictFloat, dynamic_creation('Number'), StrictBool, dynamic_creation('Boolean'), str, dynamic_creation('Text'), dynamic_creation('StructuredValue')]] = Field(
        default=None,
        description="The value of the quantitative value or property value node. * For [[QuantitativeValue]]"
     "and [[MonetaryAmount]], the recommended type for values is 'Number'. * For [[PropertyValue]],"
     "it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. * Use values from 0123456789"
     "(Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
     "similar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to"
     "indicate a decimal point. Avoid using these symbols as a readability separator.",
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
    valueReference: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('PropertyValue'), dynamic_creation('Enumeration'), dynamic_creation('MeasurementTypeEnumeration'), dynamic_creation('DefinedTerm'), dynamic_creation('QualitativeValue'), Any, dynamic_creation('StructuredValue')]], str, dynamic_creation('Text'), dynamic_creation('PropertyValue'), dynamic_creation('Enumeration'), dynamic_creation('MeasurementTypeEnumeration'), dynamic_creation('DefinedTerm'), dynamic_creation('QualitativeValue'), Any, dynamic_creation('StructuredValue')]] = Field(
        default=None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",
    )
    unitCode: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    maxValue: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), str]], StrictInt, StrictFloat, dynamic_creation('Number'), str]] = Field(
        default=None,
        description="The upper value of some characteristic or property.",
    )
    unitText: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",
    )
    minValue: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), str]], StrictInt, StrictFloat, dynamic_creation('Number'), str]] = Field(
        default=None,
        description="The lower value of some characteristic or property.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
    from pydantic import BaseModel
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Enumeration import Enumeration
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
