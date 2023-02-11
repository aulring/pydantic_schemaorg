from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class DrugStrength(BaseModel):
    """A specific strength in which a medical drug is available in a specific country.

    See: https://schema.org/DrugStrength
    Model depth: 4
    """
    type_: str = Field(default="DrugStrength", alias='@type', const=True)
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
    recognizingAuthority: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="If applicable, the organization that officially recognizes this entity as part of its"
     "endorsed system of medicine.",
    )
    relevantSpecialty: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="If applicable, a medical specialty in which this entity is relevant.",
    )
    medicineSystem: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The system of medicine that includes this MedicalEntity, for example 'evidence-based',"
     "'homeopathic', 'chiropractic', etc.",
    )
    funding: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    legalStatus: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    study: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A medical study or trial related to this entity.",
    )
    guideline: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A medical guideline related to this entity.",
    )
    code: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A medical code for the entity, taken from a controlled vocabulary or ontology such as"
     "ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.",
    )
    activeIngredient: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    availableIn: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The location in which the strength is available.",
    )
    strengthValue: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="The value of an active ingredient's strength, e.g. 325.",
    )
    strengthUnit: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The units of an active ingredient's strength, e.g. mg.",
    )
    maximumIntake: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    
