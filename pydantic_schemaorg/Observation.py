from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import datetime
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.StatisticalPopulation import StatisticalPopulation
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.DataType import DataType
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Property import Property


class Observation(BaseModel):
    """Instances of the class [[Observation]] are used to specify observations about an entity"
     "(which may or may not be an instance of a [[StatisticalPopulation]]), at a particular"
     "time. The principal properties of an [[Observation]] are [[observedNode]], [[measuredProperty]],"
     "[[measuredValue]] (or [[median]], etc.) and [[observationDate]] ([[measuredProperty]]"
     "properties can, but need not always, be W3C RDF Data Cube \"measure properties\", as"
     "in the [lifeExpectancy example](https://www.w3.org/TR/vocab-data-cube/#dsd-example))."
     "See also [[StatisticalPopulation]], and the [data and datasets](/docs/data-and-datasets.html)"
     "overview for more details.

    See: https://schema.org/Observation
    Model depth: 3
    """
    type_: str = Field(default="Observation", alias='@type', const=True)
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
    observedNode: Optional[Union[List[Union[StatisticalPopulation, str]], StatisticalPopulation, str]] = Field(
        default=None,
        description="The observedNode of an [[Observation]], often a [[StatisticalPopulation]].",
    )
    marginOfError: Optional[Union[List[Union[QuantitativeValue, str]], QuantitativeValue, str]] = Field(
        default=None,
        description="A marginOfError for an [[Observation]].",
    )
    measuredValue: Optional[Union[List[Union[DataType, str]], DataType, str]] = Field(
        default=None,
        description="The measuredValue of an [[Observation]].",
    )
    observationDate: Optional[Union[List[Union[datetime, DateTime, str]], datetime, DateTime, str]] = Field(
        default=None,
        description="The observationDate of an [[Observation]].",
    )
    measuredProperty: Optional[Union[List[Union[Property, str]], Property, str]] = Field(
        default=None,
        description="The measuredProperty of an [[Observation]], either a schema.org property, a property"
     "from other RDF-compatible systems, e.g. W3C RDF Data Cube, or schema.org extensions"
     "such as [GS1's](https://www.gs1.org/voc/?show=properties).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.StatisticalPopulation import StatisticalPopulation
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.DataType import DataType
    from pydantic import BaseModel
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Property import Property
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.ImageObject import ImageObject
