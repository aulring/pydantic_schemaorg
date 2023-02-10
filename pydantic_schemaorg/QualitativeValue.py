from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Property import Property
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Class import Class
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
from pydantic_schemaorg.StructuredValue import StructuredValue
from pydantic_schemaorg.Action import Action


class QualitativeValue(BaseModel):
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or"
     "the garment sizes 'S', 'M', 'L', and 'XL'.

    See: https://schema.org/QualitativeValue
    Model depth: 4
    """
    type_: str = Field(default="QualitativeValue", alias='@type', const=True)
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
    supersededBy: Optional[Union[List[Union['Enumeration', Property, Class, str]], 'Enumeration', Property, Class, str]] = Field(
        default=None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    greater: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than the object.",
    )
    additionalProperty: Optional[Union[List[Union[PropertyValue, str]], PropertyValue, str]] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g."
     "a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    valueReference: Optional[Union[List[Union[str, Text, StructuredValue, MeasurementTypeEnumeration, QuantitativeValue, Enumeration, DefinedTerm, 'QualitativeValue', PropertyValue]], str, Text, StructuredValue, MeasurementTypeEnumeration, QuantitativeValue, Enumeration, DefinedTerm, 'QualitativeValue', PropertyValue]] = Field(
        default=None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",
    )
    equal: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is equal to"
     "the object.",
    )
    lesser: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than the object.",
    )
    greaterOrEqual: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than or equal to the object.",
    )
    lesserOrEqual: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than or equal to the object.",
    )
    nonEqual: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is not equal"
     "to the object.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Class import Class
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
    from pydantic import BaseModel
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Property import Property
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Enumeration import Enumeration
    from pydantic_schemaorg.ImageObject import ImageObject
