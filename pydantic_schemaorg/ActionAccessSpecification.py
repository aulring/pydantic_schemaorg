from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from datetime import date, datetime, time
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from pydantic import AnyUrl, StrictBool


from pydantic_schemaorg.GeoShape import GeoShape
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.Boolean import Boolean
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Time import Time
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic import Field
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.MediaSubscription import MediaSubscription


class ActionAccessSpecification(BaseModel):
    """A set of requirements that must be fulfilled in order to perform an Action.

    See: https://schema.org/ActionAccessSpecification
    Model depth: 3
    """
    type_: str = Field(default="ActionAccessSpecification", alias='@type', const=True)
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
    availabilityEnds: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), time, dynamic_creation('Time'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), time, dynamic_creation('Time'), str]] = Field(
        default=None,
        description="The end of the availability of the product or service included in the offer.",
    )
    expectsAcceptanceOf: Optional[Union[List[Union[dynamic_creation('Offer'), str]], dynamic_creation('Offer'), str]] = Field(
        default=None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    availabilityStarts: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), time, dynamic_creation('Time'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), time, dynamic_creation('Time'), str]] = Field(
        default=None,
        description="The beginning of the availability of the product or service included in the offer.",
    )
    requiresSubscription: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), dynamic_creation('MediaSubscription'), str]], StrictBool, dynamic_creation('Boolean'), dynamic_creation('MediaSubscription'), str]] = Field(
        default=None,
        description="Indicates if use of the media require a subscription (either paid or free). Allowed values"
     "are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').",
    )
    eligibleRegion: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('Place')]], str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('Place')]] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    ineligibleRegion: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('Place')]], str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('Place')]] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    category: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CategoryCode'), dynamic_creation('PhysicalActivityCategory'), dynamic_creation('Thing')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CategoryCode'), dynamic_creation('PhysicalActivityCategory'), dynamic_creation('Thing')]] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    

if TYPE_CHECKING:
    from pydantic import BaseModel
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.MediaSubscription import MediaSubscription
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
