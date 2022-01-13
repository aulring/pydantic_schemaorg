from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.EmergencyService import EmergencyService

from pydantic_schemaorg.CivicStructure import CivicStructure

from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Hospital(EmergencyService, MedicalOrganization):
    """A hospital.

    See: https://schema.org/Hospital
    Model depth: 4
    """

    type_: str = Field("Hospital", const=True, alias="@type")
    medicalSpecialty: "Optional[Union[List[Union[MedicalSpecialty, str]], Union[MedicalSpecialty, str]]]" = Field(
        None,
        description="A medical specialty of the provider.",
    )
    healthcareReportingData: "Optional[Union[List[Union[Dataset, CDCPMDRecord, str]], Union[Dataset, CDCPMDRecord, str]]]" = Field(
        None,
        description="Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of"
        "[[Dataset]].",
    )
    availableService: "Optional[Union[List[Union[MedicalTherapy, MedicalProcedure, MedicalTest, str]], Union[MedicalTherapy, MedicalProcedure, MedicalTest, str]]]" = Field(
        None,
        description="A medical service available from this provider.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

    from pydantic_schemaorg.Dataset import Dataset

    from pydantic_schemaorg.CDCPMDRecord import CDCPMDRecord

    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy

    from pydantic_schemaorg.MedicalProcedure import MedicalProcedure

    from pydantic_schemaorg.MedicalTest import MedicalTest

    Hospital.update_forward_refs()
