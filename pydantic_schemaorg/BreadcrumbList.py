from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.ItemList import ItemList
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Integer import Integer
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Action import Action


class BreadcrumbList(BaseModel):
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically"
     "described using at least their URL and their name, and typically ending with the current"
     "page. The [[position]] property is used to reconstruct the order of the items in a BreadcrumbList."
     "The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]]"
     "(lower values listed first), and that the first items in this list correspond to the \"top\""
     "or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific"
     "values of 'position' are not assigned meaning for a BreadcrumbList, but they should"
     "be integers, e.g. beginning with '1' for the first item in the list.

    See: https://schema.org/BreadcrumbList
    Model depth: 4
    """
    type_: str = Field(default="BreadcrumbList", alias='@type', const=True)
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
    itemListOrder: Optional[Union[List[Union[str, Text, ItemListOrderType]], str, Text, ItemListOrderType]] = Field(
        default=None,
        description="Type of ordering (e.g. Ascending, Descending, Unordered).",
    )
    numberOfItems: Optional[Union[List[Union[int, Integer, str]], int, Integer, str]] = Field(
        default=None,
        description="The number of items in an ItemList. Note that some descriptions might not fully describe"
     "all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems"
     "would be for the entire list.",
    )
    itemListElement: Optional[Union[List[Union[str, Text, ListItem, Thing]], str, Text, ListItem, Thing]] = Field(
        default=None,
        description="For itemListElement values, you can use simple strings (e.g. \"Peter\", \"Paul\","
     "\"Mary\"), existing entities, or use ListItem. Text values are best if the elements"
     "in the list are plain strings. Existing entities are best for a simple, unordered list"
     "of existing things in your data. ListItem is used with ordered lists when you want to provide"
     "additional context about the element in that list or when the same item might be in different"
     "places in different lists. Note: The order of elements in your mark-up is not sufficient"
     "for indicating the order or elements. Use ListItem with a 'position' property in such"
     "cases.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ListItem import ListItem
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.ItemListOrderType import ItemListOrderType
    from pydantic_schemaorg.ImageObject import ImageObject
