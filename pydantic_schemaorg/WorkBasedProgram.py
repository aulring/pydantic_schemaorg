from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from pydantic import AnyUrl, StrictInt, StrictFloat
from datetime import date, datetime
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.AlignmentObject import AlignmentObject
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.EducationalOccupationalProgram import EducationalOccupationalProgram
from pydantic_schemaorg.Integer import Integer
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Number import Number
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.Course import Course
from pydantic_schemaorg.DayOfWeek import DayOfWeek
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.StructuredValue import StructuredValue


class WorkBasedProgram(BaseModel):
    """A program with both an educational and employment component. Typically based at a workplace"
     "and structured around work-based learning, with the aim of instilling competencies"
     "related to an occupation. WorkBasedProgram is used to distinguish programs such as"
     "apprenticeships from school, college or other classroom based educational programs.

    See: https://schema.org/WorkBasedProgram
    Model depth: 4
    """
    type_: str = Field(default="WorkBasedProgram", alias='@type', const=True)
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
    applicationDeadline: Optional[Union[List[Union[date, Date, str]], date, Date, str]] = Field(
        default=None,
        description="The date at which the program stops collecting applications for the next enrollment"
     "cycle.",
    )
    timeToComplete: Optional[Union[List[Union[Duration, str]], Duration, str]] = Field(
        default=None,
        description="The expected length of time to complete the program if attending full-time.",
    )
    timeOfDay: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The time of day the program normally runs. For example, \"evenings\".",
    )
    provider: Optional[Union[List[Union[Organization, Person, str]], Organization, Person, str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    termsPerYear: Optional[Union[List[Union[StrictInt, StrictFloat, Number, str]], StrictInt, StrictFloat, Number, str]] = Field(
        default=None,
        description="The number of times terms of study are offered per year. Semesters and quarters are common"
     "units for term. For example, if the student can only take 2 semesters for the program in"
     "one year, then termsPerYear should be 2.",
    )
    termDuration: Optional[Union[List[Union[Duration, str]], Duration, str]] = Field(
        default=None,
        description="The amount of time in a term as defined by the institution. A term is a length of time where"
     "students take one or more classes. Semesters and quarters are common units for term.",
    )
    occupationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, URL, str, Text, EducationalOccupationalCredential]], AnyUrl, URL, str, Text, EducationalOccupationalCredential]] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    financialAidEligible: Optional[Union[List[Union[str, Text, DefinedTerm]], str, Text, DefinedTerm]] = Field(
        default=None,
        description="A financial aid type or program which students may use to pay for tuition or fees associated"
     "with the program.",
    )
    salaryUponCompletion: Optional[Union[List[Union[MonetaryAmountDistribution, str]], MonetaryAmountDistribution, str]] = Field(
        default=None,
        description="The expected salary upon completing the training.",
    )
    hasCourse: Optional[Union[List[Union[Course, str]], Course, str]] = Field(
        default=None,
        description="A course or class that is one of the learning opportunities that constitute an educational"
     "/ occupational program. No information is implied about whether the course is mandatory"
     "or optional; no guarantee is implied about whether the course will be available to everyone"
     "on the program.",
    )
    educationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, URL, str, Text, EducationalOccupationalCredential]], AnyUrl, URL, str, Text, EducationalOccupationalCredential]] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other educational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    typicalCreditsPerTerm: Optional[Union[List[Union[int, Integer, StructuredValue, str]], int, Integer, StructuredValue, str]] = Field(
        default=None,
        description="The number of credits or units a full-time student would be expected to take in 1 term however"
     "'term' is defined by the institution.",
    )
    maximumEnrollment: Optional[Union[List[Union[int, Integer, str]], int, Integer, str]] = Field(
        default=None,
        description="The maximum number of students who may be enrolled in the program.",
    )
    programType: Optional[Union[List[Union[str, Text, DefinedTerm]], str, Text, DefinedTerm]] = Field(
        default=None,
        description="The type of educational or occupational program. For example, classroom, internship,"
     "alternance, etc.",
    )
    programPrerequisites: Optional[Union[List[Union[str, Text, Course, EducationalOccupationalCredential, AlignmentObject]], str, Text, Course, EducationalOccupationalCredential, AlignmentObject]] = Field(
        default=None,
        description="Prerequisites for enrolling in the program.",
    )
    educationalProgramMode: Optional[Union[List[Union[AnyUrl, URL, str, Text]], AnyUrl, URL, str, Text]] = Field(
        default=None,
        description="Similar to courseMode, the medium or means of delivery of the program as a whole. The value"
     "may either be a text label (e.g. \"online\", \"onsite\" or \"blended\"; \"synchronous\""
     "or \"asynchronous\"; \"full-time\" or \"part-time\") or a URL reference to a term from"
     "a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous"
     ").",
    )
    dayOfWeek: Optional[Union[List[Union[DayOfWeek, str]], DayOfWeek, str]] = Field(
        default=None,
        description="The day of the week for which these opening hours are valid.",
    )
    occupationalCategory: Optional[Union[List[Union[str, Text, CategoryCode]], str, Text, CategoryCode]] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    startDate: Optional[Union[List[Union[datetime, DateTime, date, Date, str]], datetime, DateTime, date, Date, str]] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    numberOfCredits: Optional[Union[List[Union[int, Integer, StructuredValue, str]], int, Integer, StructuredValue, str]] = Field(
        default=None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    offers: Optional[Union[List[Union[Demand, Offer, str]], Demand, Offer, str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    trainingSalary: Optional[Union[List[Union[MonetaryAmountDistribution, str]], MonetaryAmountDistribution, str]] = Field(
        default=None,
        description="The estimated salary earned while in the program.",
    )
    endDate: Optional[Union[List[Union[datetime, DateTime, date, Date, str]], datetime, DateTime, date, Date, str]] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    applicationStartDate: Optional[Union[List[Union[date, Date, str]], date, Date, str]] = Field(
        default=None,
        description="The date at which the program begins collecting applications for the next enrollment"
     "cycle.",
    )
    occupationalCategory: Optional[Union[List[Union[str, Text, CategoryCode]], str, Text, CategoryCode]] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    trainingSalary: Optional[Union[List[Union[MonetaryAmountDistribution, str]], MonetaryAmountDistribution, str]] = Field(
        default=None,
        description="The estimated salary earned while in the program.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Course import Course
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DayOfWeek import DayOfWeek
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.AlignmentObject import AlignmentObject
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Person import Person
