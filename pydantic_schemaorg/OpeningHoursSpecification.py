from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from datetime import date, datetime, time
from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic_schemaorg.StructuredValue import StructuredValue
from pydantic import Field
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.Time import Time
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.DayOfWeek import DayOfWeek
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.Action import Action


class OpeningHoursSpecification(BaseModel):
    """A structured value providing information about the opening hours of a place or a certain"
     "service inside a place. The place is __open__ if the [[opens]] property is specified,"
     "and __closed__ otherwise. If the value for the [[closes]] property is less than the value"
     "for the [[opens]] property then the hour range is assumed to span over the next day.

    See: https://schema.org/OpeningHoursSpecification
    Model depth: 4
    """
    type_: str = Field(default="OpeningHoursSpecification", alias='@type', const=True)
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
    closes: Optional[Union[List[Union[time, dynamic_creation('Time'), str]], time, dynamic_creation('Time'), str]] = Field(
        default=None,
        description="The closing hour of the place or service on the given day(s) of the week.",
    )
    validThrough: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    opens: Optional[Union[List[Union[time, dynamic_creation('Time'), str]], time, dynamic_creation('Time'), str]] = Field(
        default=None,
        description="The opening hour of the place or service on the given day(s) of the week.",
    )
    validFrom: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    dayOfWeek: Optional[Union[List[Union[dynamic_creation('DayOfWeek'), str]], dynamic_creation('DayOfWeek'), str]] = Field(
        default=None,
        description="The day of the week for which these opening hours are valid.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Event import Event
    from pydantic import BaseModel
    from pydantic_schemaorg.DayOfWeek import DayOfWeek
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
