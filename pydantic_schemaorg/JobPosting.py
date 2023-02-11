from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class JobPosting(BaseModel):
    """A listing that describes a job opening in a certain organization.

    See: https://schema.org/JobPosting
    Model depth: 3
    """
    type_: str = Field(default="JobPosting", alias='@type', const=True)
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
    incentiveCompensation: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Description of bonus and commission compensation aspects of the job.",
    )
    securityClearanceRequirement: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,
        description="A description of any security clearance requirements of the job.",
    )
    hiringOrganization: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Organization or Person offering the job position.",
    )
    baseSalary: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="The base salary of the job or of an employee in an EmployeeRole.",
    )
    workHours: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).",
    )
    jobImmediateStart: Optional[Union[List[Union[StrictBool, Any, str]], StrictBool, Any, str]] = Field(
        default=None,
        description="An indicator as to whether a position is available for an immediate start.",
    )
    employerOverview: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A description of the employer, career opportunities and work environment for this position.",
    )
    skills: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A statement of knowledge, skill, ability, task or any other assertion expressing a competency"
     "that is desired or required to fulfill this role or to work in this occupation.",
    )
    physicalRequirement: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,
        description="A description of the types of physical activity associated with the job. Defined terms"
     "such as those in O*net may be used, but note that there is no way to specify the level of ability"
     "as well as its nature when using a defined term.",
    )
    experienceRequirements: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Description of skills and experience needed for the position or Occupation.",
    )
    qualifications: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Specific qualifications required for this role or Occupation.",
    )
    specialCommitments: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Any special commitments associated with this job posting. Valid entries include VeteranCommit,"
     "MilitarySpouseCommit, etc.",
    )
    jobStartDate: Union[List[Union[date, Any, str]], date, Any, str] = Field(
        default=None,
        description="The date on which a successful applicant for this job would be expected to start work."
     "Choose a specific date in the future or use the jobImmediateStart property to indicate"
     "the position is to be filled as soon as possible.",
    )
    title: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The title of the job.",
    )
    relevantOccupation: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The Occupation for the JobPosting.",
    )
    jobLocation: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A (typically single) geographic location associated with the job position.",
    )
    educationRequirements: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Educational background needed for the position or Occupation.",
    )
    eligibilityToWorkRequirement: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The legal requirements such as citizenship, visa and other documentation required"
     "for an applicant to this job.",
    )
    estimatedSalary: Optional[Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str]] = Field(
        default=None,
        description="An estimated salary for a job posting or occupation, based on a variety of variables including,"
     "but not limited to industry, job title, and location. Estimated salaries are often computed"
     "by outside organizations rather than the hiring organization, who may not have committed"
     "to the estimated value.",
    )
    validThrough: Optional[Union[List[Union[datetime, date, Any, str]], datetime, date, Any, str]] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    sensoryRequirement: Union[List[Union[Any, str, AnyUrl]], Any, str, AnyUrl] = Field(
        default=None,
        description="A description of any sensory requirements and levels necessary to function on the job,"
     "including hearing and vision. Defined terms such as those in O*net may be used, but note"
     "that there is no way to specify the level of ability as well as its nature when using a defined"
     "term.",
    )
    employmentType: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).",
    )
    totalJobOpenings: Optional[Union[List[Union[Any, int, str]], Any, int, str]] = Field(
        default=None,
        description="The number of positions open for this job posting. Use a positive integer. Do not use if"
     "the number of positions is unclear or not known.",
    )
    salaryCurrency: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217))"
     "used for the main salary information in this job posting or for this employee.",
    )
    applicationContact: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Contact details for further information relevant to this job posting.",
    )
    experienceInPlaceOfEducation: Optional[Union[List[Union[StrictBool, Any, str]], StrictBool, Any, str]] = Field(
        default=None,
        description="Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]])"
     "in place of its formal educational qualifications (as indicated by [[educationRequirements]])."
     "If true, indicates that satisfying one of these requirements is sufficient.",
    )
    datePosted: Optional[Union[List[Union[datetime, date, Any, str]], datetime, date, Any, str]] = Field(
        default=None,
        description="Publication date of an online listing.",
    )
    jobBenefits: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Description of benefits associated with the job.",
    )
    applicantLocationRequirements: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The location(s) applicants can apply from. This is usually used for telecommuting jobs"
     "where the applicant does not need to be in a physical office. Note: This should not be used"
     "for citizenship or work visa requirements.",
    )
    occupationalCategory: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    industry: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="The industry associated with the job position.",
    )
    employmentUnit: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Indicates the department, unit and/or facility where the employee reports and/or in"
     "which the job is to be performed.",
    )
    benefits: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Description of benefits associated with the job.",
    )
    jobLocationType: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A description of the job location (e.g. TELECOMMUTE for telecommute jobs).",
    )
    responsibilities: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Responsibilities associated with this role or Occupation.",
    )
    directApply: Optional[Union[List[Union[StrictBool, Any, str]], StrictBool, Any, str]] = Field(
        default=None,
        description="Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct"
     "application for the job, via the posting website. A job posting is considered to have"
     "directApply of [[True]] if an application process for the specified job can be directly"
     "initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless"
     "be involved at an implementation level). A value of [[False]] is appropriate if there"
     "is no clear path to applying directly online for the specified job, navigating directly"
     "from the JobPosting url(s) supplied.",
    )
    incentives: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="Description of bonus and commission compensation aspects of the job.",
    )
    
