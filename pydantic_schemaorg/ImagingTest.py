from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalTest import MedicalTest


class ImagingTest(MedicalTest):
    """Any medical imaging modality typically used for diagnostic purposes.

    See: https://schema.org/ImagingTest
    Model depth: 4
    """

    type_: str = Field("ImagingTest", const=True, alias="@type")
    imagingTechnique: "Optional[Union[List[Union[MedicalImagingTechnique, str]], Union[MedicalImagingTechnique, str]]]" = Field(
        None,
        description="Imaging technique used.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique

    ImagingTest.update_forward_refs()
