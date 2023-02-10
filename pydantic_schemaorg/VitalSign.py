from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalRiskFactor import MedicalRiskFactor
from pydantic_schemaorg.MedicalSign import MedicalSign
from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
from pydantic_schemaorg.MedicineSystem import MedicineSystem
from pydantic_schemaorg.Drug import Drug
from pydantic_schemaorg.PhysicalExam import PhysicalExam
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.Grant import Grant
from pydantic_schemaorg.EventStatusType import EventStatusType
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalStudy import MedicalStudy
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.MedicalCode import MedicalCode
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.DDxElement import DDxElement
from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
from pydantic_schemaorg.MedicalConditionStage import MedicalConditionStage
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus


class VitalSign(BaseModel):
    """Vital signs are measures of various physiological functions in order to assess the most"
     "basic body functions.

    See: https://schema.org/VitalSign
    Model depth: 6
    """
    type_: str = Field(default="VitalSign", alias='@type', const=True)
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
    riskFactor: Optional[Union[List[Union[MedicalRiskFactor, str]], MedicalRiskFactor, str]] = Field(
        default=None,
        description="A modifiable or non-modifiable factor that increases the risk of a patient contracting"
     "this condition, e.g. age, coexisting condition.",
    )
    primaryPrevention: Optional[Union[List[Union[MedicalTherapy, str]], MedicalTherapy, str]] = Field(
        default=None,
        description="A preventative therapy used to prevent an initial occurrence of the medical condition,"
     "such as vaccination.",
    )
    expectedPrognosis: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The likely outcome in either the short term or long term of the medical condition.",
    )
    typicalTest: Optional[Union[List[Union[MedicalTest, str]], MedicalTest, str]] = Field(
        default=None,
        description="A medical test typically performed given this condition.",
    )
    differentialDiagnosis: Optional[Union[List[Union[DDxElement, str]], DDxElement, str]] = Field(
        default=None,
        description="One of a set of differential diagnoses for the condition. Specifically, a closely-related"
     "or competing diagnosis typically considered later in the cognitive process whereby"
     "this medical condition is distinguished from others most likely responsible for a similar"
     "collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses"
     "in a patient.",
    )
    pathophysiology: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated"
     "with this activity or condition.",
    )
    status: Optional[Union[List[Union[str, Text, EventStatusType, MedicalStudyStatus]], str, Text, EventStatusType, MedicalStudyStatus]] = Field(
        default=None,
        description="The status of the study (enumerated).",
    )
    naturalProgression: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The expected progression of the condition if it is not treated and allowed to progress"
     "naturally.",
    )
    drug: Optional[Union[List[Union[Drug, str]], Drug, str]] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    secondaryPrevention: Optional[Union[List[Union[MedicalTherapy, str]], MedicalTherapy, str]] = Field(
        default=None,
        description="A preventative therapy used to prevent reoccurrence of the medical condition after"
     "an initial episode of the condition.",
    )
    signOrSymptom: Optional[Union[List[Union[MedicalSignOrSymptom, str]], MedicalSignOrSymptom, str]] = Field(
        default=None,
        description="A sign or symptom of this condition. Signs are objective or physically observable manifestations"
     "of the medical condition while symptoms are the subjective experience of the medical"
     "condition.",
    )
    possibleTreatment: Optional[Union[List[Union[MedicalTherapy, str]], MedicalTherapy, str]] = Field(
        default=None,
        description="A possible treatment to address this condition, sign or symptom.",
    )
    epidemiology: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The characteristics of associated patients, such as age, gender, race etc.",
    )
    associatedAnatomy: Optional[Union[List[Union[AnatomicalStructure, AnatomicalSystem, SuperficialAnatomy, str]], AnatomicalStructure, AnatomicalSystem, SuperficialAnatomy, str]] = Field(
        default=None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",
    )
    possibleComplication: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="A possible unexpected and unfavorable evolution of a medical condition. Complications"
     "may include worsening of the signs or symptoms of the disease, extension of the condition"
     "to other organ systems, etc.",
    )
    stage: Optional[Union[List[Union[MedicalConditionStage, str]], MedicalConditionStage, str]] = Field(
        default=None,
        description="The stage of the condition, if applicable.",
    )
    possibleTreatment: Optional[Union[List[Union[MedicalTherapy, str]], MedicalTherapy, str]] = Field(
        default=None,
        description="A possible treatment to address this condition, sign or symptom.",
    )
    identifyingExam: Optional[Union[List[Union[PhysicalExam, str]], PhysicalExam, str]] = Field(
        default=None,
        description="A physical examination that can identify this sign.",
    )
    identifyingTest: Optional[Union[List[Union[MedicalTest, str]], MedicalTest, str]] = Field(
        default=None,
        description="A diagnostic test that can identify this sign.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.EventStatusType import EventStatusType
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic_schemaorg.MedicineSystem import MedicineSystem
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.MedicalConditionStage import MedicalConditionStage
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.Drug import Drug
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.MedicalTest import MedicalTest
    from pydantic_schemaorg.PhysicalExam import PhysicalExam
    from pydantic_schemaorg.MedicalRiskFactor import MedicalRiskFactor
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.MedicalStudy import MedicalStudy
    from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.MedicalCode import MedicalCode
    from pydantic_schemaorg.DDxElement import DDxElement
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
