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
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration
from pydantic_schemaorg.Action import Action


class EnergyConsumptionDetails(BaseModel):
    """EnergyConsumptionDetails represents information related to the energy efficiency"
     "of a product that consumes energy. The information that can be provided is based on international"
     "regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj)"
     "for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer)"
     "under the Energy Policy and Conservation Act (EPCA) in the US.

    See: https://schema.org/EnergyConsumptionDetails
    Model depth: 3
    """
    type_: str = Field(default="EnergyConsumptionDetails", alias='@type', const=True)
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
    hasEnergyEfficiencyCategory: Optional[Union[List[Union[dynamic_creation('EnergyEfficiencyEnumeration'), str]], dynamic_creation('EnergyEfficiencyEnumeration'), str]] = Field(
        default=None,
        description="Defines the energy efficiency Category (which could be either a rating out of range of"
     "values or a yes/no certification) for a product according to an international energy"
     "efficiency standard.",
    )
    energyEfficiencyScaleMin: Optional[Union[List[Union[dynamic_creation('EUEnergyEfficiencyEnumeration'), str]], dynamic_creation('EUEnergyEfficiencyEnumeration'), str]] = Field(
        default=None,
        description="Specifies the least energy efficient class on the regulated EU energy consumption scale"
     "for the product category a product belongs to. For example, energy consumption for televisions"
     "placed on the market after January 1, 2020 is scaled from D to A+++.",
    )
    energyEfficiencyScaleMax: Optional[Union[List[Union[dynamic_creation('EUEnergyEfficiencyEnumeration'), str]], dynamic_creation('EUEnergyEfficiencyEnumeration'), str]] = Field(
        default=None,
        description="Specifies the most energy efficient class on the regulated EU energy consumption scale"
     "for the product category a product belongs to. For example, energy consumption for televisions"
     "placed on the market after January 1, 2020 is scaled from D to A+++.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration
    from pydantic import BaseModel
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.URL import URL
