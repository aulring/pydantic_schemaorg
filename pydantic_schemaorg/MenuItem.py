from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.RestrictedDiet import RestrictedDiet
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.MenuSection import MenuSection
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.NutritionInformation import NutritionInformation
from pydantic_schemaorg.Action import Action


class MenuItem(BaseModel):
    """A food or drink item listed in a menu or menu section.

    See: https://schema.org/MenuItem
    Model depth: 3
    """
    type_: str = Field(default="MenuItem", alias='@type', const=True)
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
    nutrition: Optional[Union[List[Union[NutritionInformation, str]], NutritionInformation, str]] = Field(
        default=None,
        description="Nutrition information about the recipe or menu item.",
    )
    suitableForDiet: Optional[Union[List[Union[RestrictedDiet, str]], RestrictedDiet, str]] = Field(
        default=None,
        description="Indicates a dietary restriction or guideline for which this recipe or menu item is suitable,"
     "e.g. diabetic, halal etc.",
    )
    menuAddOn: Optional[Union[List[Union['MenuItem', MenuSection, str]], 'MenuItem', MenuSection, str]] = Field(
        default=None,
        description="Additional menu item(s) such as a side dish of salad or side order of fries that can be added"
     "to this menu item. Additionally it can be a menu section containing allowed add-on menu"
     "items for this menu item.",
    )
    offers: Optional[Union[List[Union[Demand, Offer, str]], Demand, Offer, str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.MenuSection import MenuSection
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.NutritionInformation import NutritionInformation
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.RestrictedDiet import RestrictedDiet
