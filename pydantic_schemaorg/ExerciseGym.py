from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from datetime import date, datetime, time
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic_schemaorg.Photograph import Photograph
from pydantic_schemaorg.GeoShape import GeoShape
from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
from pydantic_schemaorg.Integer import Integer
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Boolean import Boolean
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.InteractionCounter import InteractionCounter
from pydantic_schemaorg.Brand import Brand
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Grant import Grant
from pydantic_schemaorg.LocalBusiness import LocalBusiness
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Number import Number
from pydantic_schemaorg.ProgramMembership import ProgramMembership
from pydantic_schemaorg.AggregateRating import AggregateRating
from pydantic_schemaorg.LocationFeatureSpecification import LocationFeatureSpecification
from pydantic_schemaorg.GeoCoordinates import GeoCoordinates
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.OfferCatalog import OfferCatalog
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Article import Article
from pydantic_schemaorg.OwnershipInfo import OwnershipInfo
from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
from pydantic_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
from pydantic_schemaorg.Review import Review
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.Language import Language
from pydantic_schemaorg.NonprofitType import NonprofitType
from pydantic_schemaorg.Map import Map
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.AboutPage import AboutPage
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.VirtualLocation import VirtualLocation
from pydantic_schemaorg.GeospatialGeometry import GeospatialGeometry
from pydantic_schemaorg.PostalAddress import PostalAddress


class ExerciseGym(BaseModel):
    """A gym.

    See: https://schema.org/ExerciseGym
    Model depth: 5
    """
    type_: str = Field(default="ExerciseGym", alias='@type', const=True)
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
    serviceArea: Optional[Union[List[Union[dynamic_creation('GeoShape'), dynamic_creation('Place'), dynamic_creation('AdministrativeArea'), str]], dynamic_creation('GeoShape'), dynamic_creation('Place'), dynamic_creation('AdministrativeArea'), str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    founder: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A person who founded this organization.",
    )
    isicV4: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    hasPOS: Optional[Union[List[Union[dynamic_creation('Place'), str]], dynamic_creation('Place'), str]] = Field(
        default=None,
        description="Points-of-Sales operated by the organization or person.",
    )
    globalLocationNumber: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",
    )
    member: Optional[Union[List[Union[Any, dynamic_creation('Person'), str]], Any, dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
     "organizations; ProgramMembership is typically for individuals.",
    )
    knowsAbout: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('Thing')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('Thing')]] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",
    )
    makesOffer: Optional[Union[List[Union[dynamic_creation('Offer'), str]], dynamic_creation('Offer'), str]] = Field(
        default=None,
        description="A pointer to products or services offered by the organization or person.",
    )
    ownershipFundingInfo: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CreativeWork'), dynamic_creation('AboutPage')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CreativeWork'), dynamic_creation('AboutPage')]] = Field(
        default=None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a description of organizational ownership structure; funding and grants. In a news/media"
     "setting, this is with particular reference to editorial independence. Note that the"
     "[[funder]] is also available and can be used to make basic funder information machine-readable.",
    )
    founders: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A person who founded this organization.",
    )
    legalName: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The official name of the organization, e.g. the registered company name.",
    )
    actionableFeedbackPolicy: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement"
     "about public engagement activities (for news media, the newsroom’s), including involving"
     "the public - digitally or otherwise -- in coverage decisions, reporting and activities"
     "after publication.",
    )
    areaServed: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('AdministrativeArea'), dynamic_creation('Place')]], str, dynamic_creation('Text'), dynamic_creation('GeoShape'), dynamic_creation('AdministrativeArea'), dynamic_creation('Place')]] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    parentOrganization: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The larger organization that this organization is a [[subOrganization]] of, if any.",
    )
    slogan: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    department: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A relationship between an organization and a department of that organization, also"
     "described as an organization (allowing different urls, logos, opening hours). For"
     "example: a store with a pharmacy, or a bakery with a cafe.",
    )
    keywords: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",
    )
    reviews: Optional[Union[List[Union[dynamic_creation('Review'), str]], dynamic_creation('Review'), str]] = Field(
        default=None,
        description="Review of the item.",
    )
    memberOf: Optional[Union[List[Union[dynamic_creation('ProgramMembership'), Any, str]], dynamic_creation('ProgramMembership'), Any, str]] = Field(
        default=None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",
    )
    publishingPrinciples: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]]"
     "writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity"
     "policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles"
     "are those of the party primarily responsible for the creation of the [[CreativeWork]]."
     "While such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",
    )
    employee: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Someone working for this organization.",
    )
    award: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    email: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Email address.",
    )
    contactPoints: Optional[Union[List[Union[dynamic_creation('ContactPoint'), str]], dynamic_creation('ContactPoint'), str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    diversityStaffingReport: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('Article'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('Article'), str]] = Field(
        default=None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a report on staffing diversity issues. In a news context this might be for example ASNE"
     "or RTDNA (US) reports, or self-reported.",
    )
    foundingDate: Optional[Union[List[Union[date, dynamic_creation('Date'), str]], date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date that this organization was founded.",
    )
    owns: Optional[Union[List[Union[dynamic_creation('Product'), dynamic_creation('OwnershipInfo'), str]], dynamic_creation('Product'), dynamic_creation('OwnershipInfo'), str]] = Field(
        default=None,
        description="Products owned by the organization or person.",
    )
    awards: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Awards won by or for this item.",
    )
    review: Optional[Union[List[Union[dynamic_creation('Review'), str]], dynamic_creation('Review'), str]] = Field(
        default=None,
        description="A review of the item.",
    )
    dissolutionDate: Optional[Union[List[Union[date, dynamic_creation('Date'), str]], date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date that this organization was dissolved.",
    )
    funding: Optional[Union[List[Union[dynamic_creation('Grant'), str]], dynamic_creation('Grant'), str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    interactionStatistic: Optional[Union[List[Union[dynamic_creation('InteractionCounter'), str]], dynamic_creation('InteractionCounter'), str]] = Field(
        default=None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",
    )
    events: Optional[Union[List[Union[dynamic_creation('Event'), str]], dynamic_creation('Event'), str]] = Field(
        default=None,
        description="Upcoming or past events associated with this place or organization.",
    )
    seeks: Optional[Union[List[Union[dynamic_creation('Demand'), str]], dynamic_creation('Demand'), str]] = Field(
        default=None,
        description="A pointer to products or services sought by the organization or person (demand).",
    )
    employees: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="People working for this organization.",
    )
    unnamedSourcesPolicy: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about"
     "policy on use of unnamed sources and the decision process required.",
    )
    subOrganization: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A relationship between two organizations where the first includes the second, e.g.,"
     "as a subsidiary. See also: the more specific 'department' property.",
    )
    foundingLocation: Optional[Union[List[Union[dynamic_creation('Place'), str]], dynamic_creation('Place'), str]] = Field(
        default=None,
        description="The place where the Organization was founded.",
    )
    funder: Optional[Union[List[Union[Any, dynamic_creation('Person'), str]], Any, dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    iso6523Code: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An organization identifier as defined in ISO 6523(-1). Note that many existing organization"
     "identifiers such as [leiCode](https://schema.org/leiCode), [duns](https://schema.org/duns)"
     "and [vatID](https://schema.org/vatID) can be expressed as an ISO 6523 identifier"
     "by setting the ICD part of the ISO 6523 identifier accordingly.",
    )
    diversityPolicy: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]."
     "For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity"
     "policy on both staffing and sources, typically providing staffing data.",
    )
    hasMerchantReturnPolicy: Optional[Union[List[Union[dynamic_creation('MerchantReturnPolicy'), str]], dynamic_creation('MerchantReturnPolicy'), str]] = Field(
        default=None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    event: Optional[Union[List[Union[dynamic_creation('Event'), str]], dynamic_creation('Event'), str]] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    duns: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",
    )
    alumni: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Alumni of an organization.",
    )
    ethicsPolicy: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic"
     "and publishing practices, or of a [[Restaurant]], a page describing food source policies."
     "In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement"
     "describing the personal, organizational, and corporate standards of behavior expected"
     "by the organization.",
    )
    leiCode: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An organization identifier that uniquely identifies a legal entity as defined in ISO"
     "17442.",
    )
    vatID: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The Value-added Tax ID of the organization or person.",
    )
    knowsLanguage: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('Language')]], str, dynamic_creation('Text'), dynamic_creation('Language')]] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",
    )
    correctionsPolicy: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing"
     "(in news media, the newsroom’s) disclosure and correction policy for errors.",
    )
    logo: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]] = Field(
        default=None,
        description="An associated logo.",
    )
    hasCredential: Optional[Union[List[Union[dynamic_creation('EducationalOccupationalCredential'), str]], dynamic_creation('EducationalOccupationalCredential'), str]] = Field(
        default=None,
        description="A credential awarded to the Person or Organization.",
    )
    address: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('PostalAddress')]], str, dynamic_creation('Text'), dynamic_creation('PostalAddress')]] = Field(
        default=None,
        description="Physical address of the item.",
    )
    brand: Optional[Union[List[Union[Any, dynamic_creation('Brand'), str]], Any, dynamic_creation('Brand'), str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    nonprofitStatus: Optional[Union[List[Union[dynamic_creation('NonprofitType'), str]], dynamic_creation('NonprofitType'), str]] = Field(
        default=None,
        description="nonprofitStatus indicates the legal status of a non-profit organization in its primary"
     "place of business.",
    )
    contactPoint: Optional[Union[List[Union[dynamic_creation('ContactPoint'), str]], dynamic_creation('ContactPoint'), str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    hasOfferCatalog: Optional[Union[List[Union[dynamic_creation('OfferCatalog'), str]], dynamic_creation('OfferCatalog'), str]] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    members: Optional[Union[List[Union[Any, dynamic_creation('Person'), str]], Any, dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A member of this organization.",
    )
    aggregateRating: Optional[Union[List[Union[dynamic_creation('AggregateRating'), str]], dynamic_creation('AggregateRating'), str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    faxNumber: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The fax number.",
    )
    telephone: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The telephone number.",
    )
    taxID: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",
    )
    naics: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",
    )
    location: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('PostalAddress'), dynamic_creation('Place'), dynamic_creation('VirtualLocation')]], str, dynamic_creation('Text'), dynamic_creation('PostalAddress'), dynamic_creation('Place'), dynamic_creation('VirtualLocation')]] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    numberOfEmployees: Optional[Union[List[Union[dynamic_creation('QuantitativeValue'), str]], dynamic_creation('QuantitativeValue'), str]] = Field(
        default=None,
        description="The number of employees in an organization, e.g. business.",
    )
    sponsor: Optional[Union[List[Union[Any, dynamic_creation('Person'), str]], Any, dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
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
    geoCovers: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a covering geometry to a covered geometry. \"Every point of b is a point of (the interior"
     "or boundary of) a\". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    longitude: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]], StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    smokingAllowed: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or"
     "hotel room.",
    )
    isicV4: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    globalLocationNumber: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",
    )
    amenityFeature: Optional[Union[List[Union[dynamic_creation('LocationFeatureSpecification'), str]], dynamic_creation('LocationFeatureSpecification'), str]] = Field(
        default=None,
        description="An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic"
     "property does not make a statement about whether the feature is included in an offer for"
     "the main accommodation or available at extra costs.",
    )
    additionalProperty: Optional[Union[List[Union[dynamic_creation('PropertyValue'), str]], dynamic_creation('PropertyValue'), str]] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g."
     "a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    slogan: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    photos: Optional[Union[List[Union[dynamic_creation('ImageObject'), dynamic_creation('Photograph'), str]], dynamic_creation('ImageObject'), dynamic_creation('Photograph'), str]] = Field(
        default=None,
        description="Photographs of this place.",
    )
    keywords: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",
    )
    reviews: Optional[Union[List[Union[dynamic_creation('Review'), str]], dynamic_creation('Review'), str]] = Field(
        default=None,
        description="Review of the item.",
    )
    tourBookingPage: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]]"
     "or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.",
    )
    geoWithin: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined"
     "in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    containsPlace: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The basic containment relation between a place and another that it contains.",
    )
    review: Optional[Union[List[Union[dynamic_creation('Review'), str]], dynamic_creation('Review'), str]] = Field(
        default=None,
        description="A review of the item.",
    )
    hasMap: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('Map'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('Map'), str]] = Field(
        default=None,
        description="A URL to a map of the place.",
    )
    containedIn: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The basic containment relation between a place and one that contains it.",
    )
    events: Optional[Union[List[Union[dynamic_creation('Event'), str]], dynamic_creation('Event'), str]] = Field(
        default=None,
        description="Upcoming or past events associated with this place or organization.",
    )
    geoOverlaps: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to another that geospatially overlaps it, i.e. they have some but not all points"
     "in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    geoEquals: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM)."
     "\"Two geometries are topologically equal if their interiors intersect and no part of"
     "the interior or boundary of one geometry intersects the exterior of the other\" (a symmetric"
     "relationship).",
    )
    maps: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="A URL to a map of the place.",
    )
    isAccessibleForFree: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    event: Optional[Union[List[Union[dynamic_creation('Event'), str]], dynamic_creation('Event'), str]] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    photo: Optional[Union[List[Union[dynamic_creation('ImageObject'), dynamic_creation('Photograph'), str]], dynamic_creation('ImageObject'), dynamic_creation('Photograph'), str]] = Field(
        default=None,
        description="A photograph of this place.",
    )
    containedInPlace: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The basic containment relation between a place and one that contains it.",
    )
    logo: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('ImageObject'), str]] = Field(
        default=None,
        description="An associated logo.",
    )
    geoCrosses: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to another that crosses it: \"a crosses b: they have some but not all interior"
     "points in common, and the dimension of the intersection is less than that of at least one"
     "of them\". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    address: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('PostalAddress')]], str, dynamic_creation('Text'), dynamic_creation('PostalAddress')]] = Field(
        default=None,
        description="Physical address of the item.",
    )
    geo: Optional[Union[List[Union[dynamic_creation('GeoCoordinates'), dynamic_creation('GeoShape'), str]], dynamic_creation('GeoCoordinates'), dynamic_creation('GeoShape'), str]] = Field(
        default=None,
        description="The geo coordinates of the place.",
    )
    openingHoursSpecification: Optional[Union[List[Union[dynamic_creation('OpeningHoursSpecification'), str]], dynamic_creation('OpeningHoursSpecification'), str]] = Field(
        default=None,
        description="The opening hours of a certain place.",
    )
    geoDisjoint: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "are topologically disjoint: \"they have no point in common. They form a set of disconnected"
     "geometries.\" (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)",
    )
    geoIntersects: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    latitude: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]], StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    maximumAttendeeCapacity: Optional[Union[List[Union[int, dynamic_creation('Integer'), str]], int, dynamic_creation('Integer'), str]] = Field(
        default=None,
        description="The total number of individuals that may attend an event or venue.",
    )
    aggregateRating: Optional[Union[List[Union[dynamic_creation('AggregateRating'), str]], dynamic_creation('AggregateRating'), str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    map: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="A URL to a map of the place.",
    )
    branchCode: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A short textual code (also called \"store code\") that uniquely identifies a place of"
     "business. The code is typically assigned by the parentOrganization and used in structured"
     "URLs. For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047"
     "the code \"3047\" is a branchCode for a particular branch.",
    )
    faxNumber: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The fax number.",
    )
    publicAccess: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="A flag to signal that the [[Place]] is open to public visitors. If this property is omitted"
     "there is no assumed default boolean value",
    )
    geoTouches: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents spatial relations in which two geometries (or the places they represent)"
     "touch: \"they have at least one boundary point in common, but no interior points.\" (A"
     "symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)",
    )
    geoCoveredBy: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    telephone: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The telephone number.",
    )
    hasDriveThroughService: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]])"
     "offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]]"
     "such facilities could potentially help with social distancing from other potentially-infected"
     "users.",
    )
    specialOpeningHoursSpecification: Optional[Union[List[Union[dynamic_creation('OpeningHoursSpecification'), str]], dynamic_creation('OpeningHoursSpecification'), str]] = Field(
        default=None,
        description="The special opening hours of a certain place. Use this to explicitly override general"
     "opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].",
    )
    geoContains: Optional[Union[List[Union[Any, dynamic_creation('GeospatialGeometry'), str]], Any, dynamic_creation('GeospatialGeometry'), str]] = Field(
        default=None,
        description="Represents a relationship between two geometries (or the places they represent), relating"
     "a containing geometry to a contained geometry. \"a contains b iff no points of b lie in"
     "the exterior of a, and at least one point of the interior of b lies in the interior of a\"."
     "As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).",
    )
    priceRange: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The price range of the business, for example ```$$$```.",
    )
    currenciesAccepted: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The currency accepted. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    branchOf: Optional[Union[List[Union[dynamic_creation('Organization'), str]], dynamic_creation('Organization'), str]] = Field(
        default=None,
        description="The larger organization that this local business is a branch of, if any. Not to be confused"
     "with (anatomical) [[branch]].",
    )
    paymentAccepted: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc.",
    )
    openingHours: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The general opening hours for a business. Opening hours can be specified as a weekly time"
     "range, starting with days, then times per day. Multiple days can be listed with commas"
     "',' separating each day. Day or time ranges are specified using a hyphen '-'. * Days are"
     "specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```,"
     "```Th```, ```Fr```, ```Sa```, ```Su```. * Times are specified using 24:00 format."
     "For example, 3pm is specified as ```15:00```, 10am as ```10:00```. * Here is an example:"
     "<code>&lt;time itemprop=\"openingHours\" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays"
     "and Thursdays 4-8pm&lt;/time&gt;</code>. * If a business is open 7 days a week, then"
     "it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday"
     "through Sunday, all day&lt;/time&gt;</code>.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.AboutPage import AboutPage
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic import BaseModel
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.GeospatialGeometry import GeospatialGeometry
    from pydantic_schemaorg.NonprofitType import NonprofitType
    from pydantic_schemaorg.Photograph import Photograph
    from pydantic_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.OfferCatalog import OfferCatalog
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.GeoCoordinates import GeoCoordinates
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.Article import Article
    from pydantic_schemaorg.OwnershipInfo import OwnershipInfo
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.LocationFeatureSpecification import LocationFeatureSpecification
    from pydantic_schemaorg.Map import Map
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.ProgramMembership import ProgramMembership
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.InteractionCounter import InteractionCounter
