from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool
from typing import List, Optional, Union
from typing import List, Optional, Union


from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalDevice import MedicalDevice
from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.MedicalStudy import MedicalStudy
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Drug import Drug
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.MedicineSystem import MedicineSystem
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Grant import Grant
from pydantic_schemaorg.MedicalSign import MedicalSign
from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.MedicalCode import MedicalCode
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class ImagingTest(BaseModel):
    """Any medical imaging modality typically used for diagnostic purposes.

    See: https://schema.org/ImagingTest
    Model depth: 4
    """
    type_: str = Field(default="ImagingTest", alias='@type', const=True)
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
    affectedBy: Optional[Union[List[Union[dynamic_creation('Drug'), str]], dynamic_creation('Drug'), str]] = Field(
        default=None,
        description="Drugs that affect the test's results.",
    )
    normalRange: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('MedicalEnumeration')]], str, dynamic_creation('Text'), dynamic_creation('MedicalEnumeration')]] = Field(
        default=None,
        description="Range of acceptable values for a typical patient, when applicable.",
    )
    signDetected: Optional[Union[List[Union[dynamic_creation('MedicalSign'), str]], dynamic_creation('MedicalSign'), str]] = Field(
        default=None,
        description="A sign detected by the test.",
    )
    usedToDiagnose: Optional[Union[List[Union[dynamic_creation('MedicalCondition'), str]], dynamic_creation('MedicalCondition'), str]] = Field(
        default=None,
        description="A condition the test is used to diagnose.",
    )
    usesDevice: Optional[Union[List[Union[dynamic_creation('MedicalDevice'), str]], dynamic_creation('MedicalDevice'), str]] = Field(
        default=None,
        description="Device used to perform the test.",
    )
    imagingTechnique: Optional[Union[List[Union[dynamic_creation('MedicalImagingTechnique'), str]], dynamic_creation('MedicalImagingTechnique'), str]] = Field(
        default=None,
        description="Imaging technique used.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Grant import Grant
    from pydantic import BaseModel
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.MedicalCode import MedicalCode
    from pydantic_schemaorg.MedicalSign import MedicalSign
    from pydantic_schemaorg.MedicalDevice import MedicalDevice
    from pydantic_schemaorg.MedicalStudy import MedicalStudy
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Drug import Drug
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.MedicalGuideline import MedicalGuideline
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.MedicineSystem import MedicineSystem
