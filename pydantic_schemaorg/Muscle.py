from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.Grant import Grant
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.MedicalStudy import MedicalStudy
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.MedicalCode import MedicalCode
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
from pydantic_schemaorg.Vessel import Vessel
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Nerve import Nerve
from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus


class Muscle(BaseModel):
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals"
     "use to effect movement.

    See: https://schema.org/Muscle
    Model depth: 4
    """
    type_: str = Field(default="Muscle", alias='@type', const=True)
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
    recognizingAuthority: Optional[Union[List[Union[Organization, str]], Organization, str]] = Field(
        default=None,
        description="If applicable, the organization that officially recognizes this entity as part of its"
     "endorsed system of medicine.",
    )
    relevantSpecialty: Optional[Union[List[Union[MedicalSpecialty, str]], MedicalSpecialty, str]] = Field(
        default=None,
        description="If applicable, a medical specialty in which this entity is relevant.",
    )
    medicineSystem: Optional[Union[List[Union[MedicineSystem, str]], MedicineSystem, str]] = Field(
        default=None,
        description="The system of medicine that includes this MedicalEntity, for example 'evidence-based',"
     "'homeopathic', 'chiropractic', etc.",
    )
    funding: Optional[Union[List[Union[Grant, str]], Grant, str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    legalStatus: Optional[Union[List[Union[str, Text, MedicalEnumeration, DrugLegalStatus]], str, Text, MedicalEnumeration, DrugLegalStatus]] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    study: Optional[Union[List[Union[MedicalStudy, str]], MedicalStudy, str]] = Field(
        default=None,
        description="A medical study or trial related to this entity.",
    )
    guideline: Optional[Union[List[Union[MedicalGuideline, str]], MedicalGuideline, str]] = Field(
        default=None,
        description="A medical guideline related to this entity.",
    )
    code: Optional[Union[List[Union[MedicalCode, str]], MedicalCode, str]] = Field(
        default=None,
        description="A medical code for the entity, taken from a controlled vocabulary or ontology such as"
     "ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.",
    )
    connectedTo: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Other anatomical structures to which this structure is connected.",
    )
    partOfSystem: Optional[Union[List[Union[AnatomicalSystem, str]], AnatomicalSystem, str]] = Field(
        default=None,
        description="The anatomical or organ system that this structure is part of.",
    )
    associatedPathophysiology: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",
    )
    bodyLocation: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="Location in the body of the anatomical structure.",
    )
    relatedTherapy: Optional[Union[List[Union[MedicalTherapy, str]], MedicalTherapy, str]] = Field(
        default=None,
        description="A medical therapy related to this anatomy.",
    )
    subStructure: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Component (sub-)structure(s) that comprise this anatomical structure.",
    )
    relatedCondition: Optional[Union[List[Union[MedicalCondition, str]], MedicalCondition, str]] = Field(
        default=None,
        description="A medical condition associated with this anatomy.",
    )
    diagram: Optional[Union[List[Union[ImageObject, str]], ImageObject, str]] = Field(
        default=None,
        description="An image containing a diagram that illustrates the structure and/or its component substructures"
     "and/or connections with other structures.",
    )
    nerve: Optional[Union[List[Union[Nerve, str]], Nerve, str]] = Field(
        default=None,
        description="The underlying innervation associated with the muscle.",
    )
    muscleAction: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The movement the muscle generates.",
    )
    bloodSupply: Optional[Union[List[Union[Vessel, str]], Vessel, str]] = Field(
        default=None,
        description="The blood vessel that carries blood from the heart to the muscle.",
    )
    antagonist: Optional[Union[List[Union['Muscle', str]], 'Muscle', str]] = Field(
        default=None,
        description="The muscle whose action counteracts the specified muscle.",
    )
    insertion: Optional[Union[List[Union[AnatomicalStructure, str]], AnatomicalStructure, str]] = Field(
        default=None,
        description="The place of attachment of a muscle, or what the muscle moves.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic_schemaorg.MedicineSystem import MedicineSystem
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.Vessel import Vessel
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.MedicalStudy import MedicalStudy
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.MedicalCode import MedicalCode
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Nerve import Nerve
    from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.Organization import Organization
