from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic_schemaorg.Text import Text
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.Integer import Integer
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.ItemListOrderType import ItemListOrderType
from pydantic_schemaorg.ListItem import ListItem


class ItemList(BaseModel):
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top"
     "100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.

    See: https://schema.org/ItemList
    Model depth: 3
    """
    type_: str = Field(default="ItemList", alias='@type', const=True)
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
    itemListOrder: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('ItemListOrderType')]], str, dynamic_creation('Text'), dynamic_creation('ItemListOrderType')]] = Field(
        default=None,
        description="Type of ordering (e.g. Ascending, Descending, Unordered).",
    )
    numberOfItems: Optional[Union[List[Union[int, dynamic_creation('Integer'), str]], int, dynamic_creation('Integer'), str]] = Field(
        default=None,
        description="The number of items in an ItemList. Note that some descriptions might not fully describe"
     "all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems"
     "would be for the entire list.",
    )
    itemListElement: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('Thing'), dynamic_creation('ListItem')]], str, dynamic_creation('Text'), dynamic_creation('Thing'), dynamic_creation('ListItem')]] = Field(
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
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.ListItem import ListItem
    from pydantic import BaseModel
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.ItemListOrderType import ItemListOrderType
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Integer import Integer
