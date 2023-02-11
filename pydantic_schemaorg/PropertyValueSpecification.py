from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class PropertyValueSpecification(BaseModel):
    """A Property value specification.

    See: https://schema.org/PropertyValueSpecification
    Model depth: 3
    """
    type_: str = Field(default="PropertyValueSpecification", alias='@type', const=True)
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
    valuePattern: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Specifies a regular expression for testing literal values according to the HTML spec.",
    )
    readonlyValue: Optional[Union[List[Union[StrictBool, Any, str]], StrictBool, Any, str]] = Field(
        default=None,
        description="Whether or not a property is mutable. Default is false. Specifying this for a property"
     "that also has a value makes it act similar to a \"hidden\" input in an HTML form.",
    )
    valueMinLength: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="Specifies the minimum allowed range for number of characters in a literal value.",
    )
    valueName: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Indicates the name of the PropertyValueSpecification to be used in URL templates and"
     "form encoding in a manner analogous to HTML's input@name.",
    )
    maxValue: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="The upper value of some characteristic or property.",
    )
    valueMaxLength: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="Specifies the allowed range for number of characters in a literal value.",
    )
    valueRequired: Optional[Union[List[Union[StrictBool, Any, str]], StrictBool, Any, str]] = Field(
        default=None,
        description="Whether the property must be filled in to complete the action. Default is false.",
    )
    stepValue: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="The stepValue attribute indicates the granularity that is expected (and required)"
     "of the value in a PropertyValueSpecification.",
    )
    defaultValue: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The default value of the input. For properties that expect a literal, the default is a"
     "literal value, for properties that expect an object, it's an ID reference to one of the"
     "current values.",
    )
    multipleValues: Optional[Union[List[Union[StrictBool, Any, str]], StrictBool, Any, str]] = Field(
        default=None,
        description="Whether multiple values are allowed for the property. Default is false.",
    )
    minValue: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="The lower value of some characteristic or property.",
    )
    
