from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.LearningResource import LearningResource

from pydantic_schemaorg.CreativeWork import CreativeWork


class Course(LearningResource, CreativeWork):
    """A description of an educational course which may be offered as distinct instances at"
     "which take place at different times or take place at different locations, or be offered"
     "through different media or modes of study. An educational course is a sequence of one"
     "or more educational events and/or creative works which aims to build knowledge, competence"
     "or ability of learners.

    See: https://schema.org/Course
    Model depth: 3
    """

    type_: str = Field("Course", const=True, alias="@type")
    numberOfCredits: "Optional[Union[List[Union[int, StructuredValue, str]], Union[int, StructuredValue, str]]]" = Field(
        None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    educationalCredentialAwarded: "Optional[Union[List[Union[AnyUrl, str, EducationalOccupationalCredential]], Union[AnyUrl, str, EducationalOccupationalCredential]]]" = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other educational"
        "credential awarded as a consequence of successful completion of this course or program.",
    )
    courseCode: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The identifier for the [[Course]] used by the course [[provider]] (e.g. CS101 or 6.001).",
    )
    hasCourseInstance: "Optional[Union[List[Union[CourseInstance, str]], Union[CourseInstance, str]]]" = Field(
        None,
        description="An offering of the course at a specific time and place or through specific media or mode"
        "of study or to a specific section of students.",
    )
    coursePrerequisites: "Optional[Union[List[Union[str, 'Course', AlignmentObject]], Union[str, 'Course', AlignmentObject]]]" = Field(
        None,
        description="Requirements for taking the Course. May be completion of another [[Course]] or a textual"
        'description like "permission of instructor". Requirements may be a pre-requisite'
        "competency, referenced using [[AlignmentObject]].",
    )
    occupationalCredentialAwarded: "Optional[Union[List[Union[AnyUrl, str, EducationalOccupationalCredential]], Union[AnyUrl, str, EducationalOccupationalCredential]]]" = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
        "credential awarded as a consequence of successful completion of this course or program.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.StructuredValue import StructuredValue

    from pydantic import AnyUrl

    from pydantic_schemaorg.EducationalOccupationalCredential import (
        EducationalOccupationalCredential,
    )

    from pydantic_schemaorg.CourseInstance import CourseInstance

    from pydantic_schemaorg.AlignmentObject import AlignmentObject

    Course.update_forward_refs()
