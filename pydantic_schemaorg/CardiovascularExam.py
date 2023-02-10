from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.PhysicalExam import PhysicalExam
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.MedicalStudy import MedicalStudy
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.MedicineSystem import MedicineSystem
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.EventStatusType import EventStatusType
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Grant import Grant
from pydantic_schemaorg.Property import Property
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Enumeration import Enumeration
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Class import Class
from pydantic_schemaorg.MedicalCode import MedicalCode
from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class CardiovascularExam(BaseModel):
    """Cardiovascular system assessment with clinical examination.

    See: https://schema.org/CardiovascularExam
    Model depth: 5
    """
    type_: str = Field(default="CardiovascularExam", alias='@type', const=True)
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
    supersededBy: Optional[Union[List[Union[Any, dynamic_creation('Class'), dynamic_creation('Property'), str]], Any, dynamic_creation('Class'), dynamic_creation('Property'), str]] = Field(
        default=None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
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
    recognizingAuthority: Optional[Union[List[Union[dynamic_creation('Organization'), str]], dynamic_creation('Organization'), str]] = Field(
        default=None,
        description="If applicable, the organization that officially recognizes this entity as part of its"
     "endorsed system of medicine.",
    )
    relevantSpecialty: Optional[Union[List[Union[dynamic_creation('MedicalSpecialty'), str]], dynamic_creation('MedicalSpecialty'), str]] = Field(
        default=None,
        description="If applicable, a medical specialty in which this entity is relevant.",
    )
    medicineSystem: Optional[Union[List[Union[dynamic_creation('MedicineSystem'), str]], dynamic_creation('MedicineSystem'), str]] = Field(
        default=None,
        description="The system of medicine that includes this MedicalEntity, for example 'evidence-based',"
     "'homeopathic', 'chiropractic', etc.",
    )
    funding: Optional[Union[List[Union[dynamic_creation('Grant'), str]], dynamic_creation('Grant'), str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    legalStatus: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DrugLegalStatus'), dynamic_creation('MedicalEnumeration')]], str, dynamic_creation('Text'), dynamic_creation('DrugLegalStatus'), dynamic_creation('MedicalEnumeration')]] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    study: Optional[Union[List[Union[dynamic_creation('MedicalStudy'), str]], dynamic_creation('MedicalStudy'), str]] = Field(
        default=None,
        description="A medical study or trial related to this entity.",
    )
    guideline: Optional[Union[List[Union[dynamic_creation('MedicalGuideline'), str]], dynamic_creation('MedicalGuideline'), str]] = Field(
        default=None,
        description="A medical guideline related to this entity.",
    )
    code: Optional[Union[List[Union[dynamic_creation('MedicalCode'), str]], dynamic_creation('MedicalCode'), str]] = Field(
        default=None,
        description="A medical code for the entity, taken from a controlled vocabulary or ontology such as"
     "ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.",
    )
    howPerformed: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="How the procedure is performed.",
    )
    procedureType: Optional[Union[List[Union[dynamic_creation('MedicalProcedureType'), str]], dynamic_creation('MedicalProcedureType'), str]] = Field(
        default=None,
        description="The type of procedure, for example Surgical, Noninvasive, or Percutaneous.",
    )
    status: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('EventStatusType'), dynamic_creation('MedicalStudyStatus')]], str, dynamic_creation('Text'), dynamic_creation('EventStatusType'), dynamic_creation('MedicalStudyStatus')]] = Field(
        default=None,
        description="The status of the study (enumerated).",
    )
    bodyLocation: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Location in the body of the anatomical structure.",
    )
    followup: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Typical or recommended followup care after the procedure is performed.",
    )
    preparation: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('MedicalEntity')]], str, dynamic_creation('Text'), dynamic_creation('MedicalEntity')]] = Field(
        default=None,
        description="Typical preparation that a patient must undergo before having the procedure performed.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.Grant import Grant
    from pydantic import BaseModel
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.MedicalCode import MedicalCode
    from pydantic_schemaorg.EventStatusType import EventStatusType
    from pydantic_schemaorg.Class import Class
    from pydantic_schemaorg.MedicalStudy import MedicalStudy
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType
    from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic_schemaorg.Property import Property
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.MedicineSystem import MedicineSystem
