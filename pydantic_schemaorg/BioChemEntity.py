from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic_schemaorg.Text import Text
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Grant import Grant
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Gene import Gene
from pydantic_schemaorg.Taxon import Taxon
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.Action import Action


class BioChemEntity(BaseModel):
    """Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical;"
     "a synthetic chemical.

    See: https://schema.org/BioChemEntity
    Model depth: 2
    """
    type_: str = Field(default="BioChemEntity", alias='@type', const=True)
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
    hasBioChemEntityPart: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part.",
    )
    isEncodedByBioChemEntity: Optional[Union[List[Union[dynamic_creation('Gene'), str]], dynamic_creation('Gene'), str]] = Field(
        default=None,
        description="Another BioChemEntity encoding by this one.",
    )
    taxonomicRange: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm'), dynamic_creation('Taxon')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm'), dynamic_creation('Taxon')]] = Field(
        default=None,
        description="The taxonomic grouping of the organism that expresses, encodes, or in some way related"
     "to the BioChemEntity.",
    )
    isLocatedInSubcellularLocation: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('DefinedTerm'), dynamic_creation('PropertyValue'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('DefinedTerm'), dynamic_creation('PropertyValue'), str]] = Field(
        default=None,
        description="Subcellular location where this BioChemEntity is located; please use PropertyValue"
     "if you want to include any evidence.",
    )
    bioChemInteraction: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A BioChemEntity that is known to interact with this item.",
    )
    funding: Optional[Union[List[Union[dynamic_creation('Grant'), str]], dynamic_creation('Grant'), str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    isPartOfBioChemEntity: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity.",
    )
    bioChemSimilarity: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.",
    )
    hasRepresentation: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('PropertyValue')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('PropertyValue')]] = Field(
        default=None,
        description="A common representation such as a protein sequence or chemical structure for this entity."
     "For images use schema.org/image.",
    )
    biologicalRole: Optional[Union[List[Union[dynamic_creation('DefinedTerm'), str]], dynamic_creation('DefinedTerm'), str]] = Field(
        default=None,
        description="A role played by the BioChemEntity within a biological context.",
    )
    isInvolvedInBiologicalProcess: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('DefinedTerm'), dynamic_creation('PropertyValue'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('DefinedTerm'), dynamic_creation('PropertyValue'), str]] = Field(
        default=None,
        description="Biological process this BioChemEntity is involved in; please use PropertyValue if"
     "you want to include any evidence.",
    )
    associatedDisease: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('PropertyValue'), dynamic_creation('MedicalCondition'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('PropertyValue'), dynamic_creation('MedicalCondition'), str]] = Field(
        default=None,
        description="Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or"
     "a URL. If you want to add an evidence supporting the association, please use PropertyValue.",
    )
    hasMolecularFunction: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('DefinedTerm'), dynamic_creation('PropertyValue'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('DefinedTerm'), dynamic_creation('PropertyValue'), str]] = Field(
        default=None,
        description="Molecular function performed by this BioChemEntity; please use PropertyValue if you"
     "want to include any evidence.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Taxon import Taxon
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Grant import Grant
    from pydantic import BaseModel
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Gene import Gene
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.PropertyValue import PropertyValue
