"""
Not yet recruiting.

https://schema.org/NotYetRecruiting
"""

from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class None(BaseModel):
    """Not yet recruiting.

    References:
        https://schema.org/NotYetRecruiting
    Note:
        Model Depth 6
    Attributes:
        None: (Optional[Union[List[Union[Any, str]], Any, str]]): Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.
        None: (Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]]): Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.
        None: (Optional[Union[List[Union[Any, str]], Any, str]]): A CreativeWork or Event about this Thing.
        None: (Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]]): URL of the item.
        None: (Union[List[Union[Any, str]], Any, str]): An alias for the item.
        None: (Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]]): URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
        None: (Union[List[Union[Any, str]], Any, str]): A description of the item.
        None: (Union[List[Union[Any, str]], Any, str]): A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.
        None: (Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]): The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.        
        None: (Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]]): An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].
        None: (Union[List[Union[Any, str]], Any, str]): The name of the item.
        None: (Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]]): An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.
        None: (Optional[Union[List[Union[Any, str]], Any, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.

    """
    type_: str = Field(default="NotYetRecruiting", alias='@type', const=True)
    None: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,alias="potentialAction",
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",
    )
    None: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,alias="mainEntityOfPage",
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",
    )
    None: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,alias="subjectOf",
        description="A CreativeWork or Event about this Thing.",
    )
    None: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,alias="url",
        description="URL of the item.",
    )
    None: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,alias="alternateName",
        description="An alias for the item.",
    )
    None: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,alias="sameAs",
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",
    )
    None: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,alias="description",
        description="A description of the item.",
    )
    None: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,alias="disambiguatingDescription",
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",
    )
    None: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,alias="identifier",
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",
    )
    None: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,alias="image",
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",
    )
    None: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,alias="name",
        description="The name of the item.",
    )
    None: Optional[Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl]] = Field(
        default=None,alias="additionalType",
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof'"
     "attribute - for multiple types. Schema.org tools may have only weaker understanding"
     "of extra types, in particular those defined externally.",
    )
    None: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,alias="supersededBy",
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    
