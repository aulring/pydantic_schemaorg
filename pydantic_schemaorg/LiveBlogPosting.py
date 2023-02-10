from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date, datetime, time
from typing import List, Optional, Union
from datetime import datetime


from pydantic_schemaorg.AlignmentObject import AlignmentObject
from pydantic_schemaorg.Integer import Integer
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.Offer import Offer
from pydantic_schemaorg.SpeakableSpecification import SpeakableSpecification
from pydantic_schemaorg.MusicRecording import MusicRecording
from pydantic_schemaorg.Boolean import Boolean
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.AudioObject import AudioObject
from pydantic_schemaorg.DateTime import DateTime
from pydantic_schemaorg.WebPage import WebPage
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.BlogPosting import BlogPosting
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.SizeSpecification import SizeSpecification
from pydantic_schemaorg.MediaObject import MediaObject
from pydantic_schemaorg.ItemList import ItemList
from pydantic_schemaorg.Rating import Rating
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.InteractionCounter import InteractionCounter
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.PublicationEvent import PublicationEvent
from pydantic_schemaorg.VideoObject import VideoObject
from pydantic import Field
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Grant import Grant
from pydantic_schemaorg.Country import Country
from pydantic_schemaorg.Number import Number
from pydantic_schemaorg.AggregateRating import AggregateRating
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Article import Article
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Review import Review
from pydantic_schemaorg.Comment import Comment
from pydantic_schemaorg.CorrectionComment import CorrectionComment
from pydantic_schemaorg.Claim import Claim
from pydantic_schemaorg.Language import Language
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.Date import Date
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Clip import Clip
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class LiveBlogPosting(BaseModel):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage"
     "of an ongoing event through continuous updates.

    See: https://schema.org/LiveBlogPosting
    Model depth: 6
    """
    type_: str = Field(default="LiveBlogPosting", alias='@type', const=True)
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
    workTranslation: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A work that is a translation of the content of this work. E.g. 西遊記 has an English workTranslation"
     "“Journey to the West”, a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese"
     "translation Tây du ký bình khảo.",
    )
    educationalLevel: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",
    )
    associatedMedia: Optional[Union[List[Union[dynamic_creation('MediaObject'), str]], dynamic_creation('MediaObject'), str]] = Field(
        default=None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    exampleOfWork: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="A creative work that this work is an example/instance/realization/derivation of.",
    )
    releasedEvent: Optional[Union[List[Union[dynamic_creation('PublicationEvent'), str]], dynamic_creation('PublicationEvent'), str]] = Field(
        default=None,
        description="The place and time the release was issued, expressed as a PublicationEvent.",
    )
    version: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]], StrictInt, StrictFloat, dynamic_creation('Number'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The version of the CreativeWork embodied by a specified resource.",
    )
    locationCreated: Optional[Union[List[Union[dynamic_creation('Place'), str]], dynamic_creation('Place'), str]] = Field(
        default=None,
        description="The location where the CreativeWork was created, which may not be the same as the location"
     "depicted in the CreativeWork.",
    )
    acquireLicensePage: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, str]], AnyUrl, dynamic_creation('URL'), Any, str]] = Field(
        default=None,
        description="Indicates a page documenting how licenses can be purchased or otherwise acquired, for"
     "the current item.",
    )
    thumbnailUrl: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="A thumbnail image relevant to the Thing.",
    )
    provider: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    expires: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="Date the content expires and is no longer useful or available. For example a [[VideoObject]]"
     "or [[NewsArticle]] whose availability or relevance is time-limited, or a [[ClaimReview]]"
     "fact check whose publisher wants to indicate that it may no longer be relevant (or helpful"
     "to highlight) after some date.",
    )
    contentLocation: Optional[Union[List[Union[dynamic_creation('Place'), str]], dynamic_creation('Place'), str]] = Field(
        default=None,
        description="The location depicted or described in the content. For example, the location in a photograph"
     "or painting.",
    )
    educationalUse: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="The purpose of a work in the context of education; for example, 'assignment', 'group"
     "work'.",
    )
    copyrightHolder: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The party holding the legal copyright to the CreativeWork.",
    )
    accessibilityControl: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Identifies input methods that are sufficient to fully control the described resource."
     "Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityControl-vocabulary).",
    )
    maintainer: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A maintainer of a [[Dataset]], software package ([[SoftwareApplication]]), or other"
     "[[Project]]. A maintainer is a [[Person]] or [[Organization]] that manages contributions"
     "to, and/or publication of, some (typically complex) artifact. It is common for distributions"
     "of software and data to be based on \"upstream\" sources. When [[maintainer]] is applied"
     "to a specific version of something e.g. a particular version or packaging of a [[Dataset]],"
     "it is always possible that the upstream source has a different maintainer. The [[isBasedOn]]"
     "property can be used to indicate such relationships between datasets to make the different"
     "maintenance roles clear. Similarly in the case of software, a package may have dedicated"
     "maintainers working on integration into software distributions such as Ubuntu, as"
     "well as upstream maintainers of the underlying work.",
    )
    educationalAlignment: Optional[Union[List[Union[dynamic_creation('AlignmentObject'), str]], dynamic_creation('AlignmentObject'), str]] = Field(
        default=None,
        description="An alignment to an established educational framework. This property should not be used"
     "where the nature of the alignment can be described using a simple property, for example"
     "to express that a resource [[teaches]] or [[assesses]] a competency.",
    )
    spatial: Optional[Union[List[Union[dynamic_creation('Place'), str]], dynamic_creation('Place'), str]] = Field(
        default=None,
        description="The \"spatial\" property can be used in cases when more specific properties (e.g. [[locationCreated]],"
     "[[spatialCoverage]], [[contentLocation]]) are not known to be appropriate.",
    )
    publisher: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The publisher of the creative work.",
    )
    keywords: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",
    )
    assesses: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="The item being described is intended to assess the competency or learning outcome defined"
     "by the referenced term.",
    )
    reviews: Optional[Union[List[Union[dynamic_creation('Review'), str]], dynamic_creation('Review'), str]] = Field(
        default=None,
        description="Review of the item.",
    )
    isBasedOn: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, dynamic_creation('Product'), str]], AnyUrl, dynamic_creation('URL'), Any, dynamic_creation('Product'), str]] = Field(
        default=None,
        description="A resource from which this work is derived or from which it is a modification or adaption.",
    )
    mentions: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="Indicates that the CreativeWork contains a reference to, but is not necessarily about"
     "a concept.",
    )
    publishingPrinciples: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, str]], AnyUrl, dynamic_creation('URL'), Any, str]] = Field(
        default=None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]]"
     "writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity"
     "policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles"
     "are those of the party primarily responsible for the creation of the [[CreativeWork]]."
     "While such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",
    )
    contributor: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A secondary contributor to the CreativeWork or Event.",
    )
    license: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, str]], AnyUrl, dynamic_creation('URL'), Any, str]] = Field(
        default=None,
        description="A license document that applies to this content, typically indicated by URL.",
    )
    citation: Union[List[Union[str, dynamic_creation('Text'), Any]], str, dynamic_creation('Text'), Any] = Field(
        default=None,
        description="A citation or reference to another creative work, such as another publication, web page,"
     "scholarly article, etc.",
    )
    accessibilitySummary: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A human-readable summary of specific accessibility features or deficiencies, consistent"
     "with the other accessibility metadata but expressing subtleties such as \"short descriptions"
     "are present but long descriptions will be needed for non-visual users\" or \"short descriptions"
     "are present and no long descriptions are needed.\"",
    )
    award: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    commentCount: Optional[Union[List[Union[int, dynamic_creation('Integer'), str]], int, dynamic_creation('Integer'), str]] = Field(
        default=None,
        description="The number of comments this CreativeWork (e.g. Article, Question or Answer) has received."
     "This is most applicable to works published in Web sites with commenting system; additional"
     "comments may exist elsewhere.",
    )
    temporalCoverage: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], datetime, dynamic_creation('DateTime'), AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The temporalCoverage of a CreativeWork indicates the period that the content applies"
     "to, i.e. that it describes, either as a DateTime or as a textual string indicating a time"
     "period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)."
     "In the case of a Dataset it will typically indicate the relevant time period in a precise"
     "notation (e.g. for a 2011 census dataset, the year 2011 would be written \"2011/2012\")."
     "Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate"
     "their temporalCoverage in broader terms - textually or via well-known URL. Written"
     "works such as books may sometimes have precise temporal coverage too, e.g. a work set"
     "in 1939 - 1945 can be indicated in ISO 8601 interval format format via \"1939/1945\"."
     "Open-ended date ranges can be written with \"..\" in place of the end date. For example,"
     "\"2015-11/..\" indicates a range beginning in November 2015 and with no specified final"
     "date. This is tentative and might be updated in future when ISO 8601 is officially updated.",
    )
    dateCreated: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date on which the CreativeWork was created or the item was added to a DataFeed.",
    )
    discussionUrl: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str]], AnyUrl, dynamic_creation('URL'), str]] = Field(
        default=None,
        description="A link to the page containing the comments of the CreativeWork.",
    )
    copyrightNotice: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Text of a notice appropriate for describing the copyright aspects of this Creative Work,"
     "ideally indicating the owner of the copyright for the Work.",
    )
    learningResourceType: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="The predominant type or kind characterizing the learning resource. For example, 'presentation',"
     "'handout'.",
    )
    awards: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Awards won by or for this item.",
    )
    accessModeSufficient: Optional[Union[List[Union[dynamic_creation('ItemList'), str]], dynamic_creation('ItemList'), str]] = Field(
        default=None,
        description="A list of single or combined accessModes that are sufficient to understand all the intellectual"
     "content of a resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary).",
    )
    review: Optional[Union[List[Union[dynamic_creation('Review'), str]], dynamic_creation('Review'), str]] = Field(
        default=None,
        description="A review of the item.",
    )
    conditionsOfAccess: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Conditions that affect the availability of, or method(s) of access to, an item. Typically"
     "used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]."
     "This property is not suitable for use as a general Web access control mechanism. It is"
     "expressed only in natural language. For example \"Available by appointment from the"
     "Reading Room\" or \"Accessible only from logged-in accounts \".",
    )
    interactivityType: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The predominant mode of learning supported by the learning resource. Acceptable values"
     "are 'active', 'expositive', or 'mixed'.",
    )
    abstract: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An abstract is a short description that summarizes a [[CreativeWork]].",
    )
    fileFormat: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml))"
     "of the content, e.g. application/zip of a SoftwareApplication binary. In cases where"
     "a CreativeWork has several media type representations, 'encoding' can be used to indicate"
     "each MediaObject alongside particular fileFormat information. Unregistered or niche"
     "file formats can be indicated instead via the most appropriate URL, e.g. defining Web"
     "page or a Wikipedia entry.",
    )
    interpretedAsClaim: Optional[Union[List[Union[dynamic_creation('Claim'), str]], dynamic_creation('Claim'), str]] = Field(
        default=None,
        description="Used to indicate a specific claim contained, implied, translated or refined from the"
     "content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can"
     "be indicated using [[claimInterpreter]].",
    )
    text: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The textual content of this CreativeWork.",
    )
    archivedAt: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('WebPage'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('WebPage'), str]] = Field(
        default=None,
        description="Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case"
     "of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible,"
     "but be archived by archival, journalistic, activist, or law enforcement organizations."
     "In such cases, the referenced page may not directly publish the content.",
    )
    alternativeHeadline: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A secondary title of the CreativeWork.",
    )
    creditText: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Text that can be used to credit person(s) and/or organization(s) associated with a published"
     "Creative Work.",
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
    workExample: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Example/instance/realization/derivation of the concept of this creative work. E.g."
     "the paperback edition, first edition, or e-book.",
    )
    about: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="The subject matter of the content.",
    )
    encodings: Optional[Union[List[Union[dynamic_creation('MediaObject'), str]], dynamic_creation('MediaObject'), str]] = Field(
        default=None,
        description="A media object that encodes this CreativeWork.",
    )
    funder: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    video: Optional[Union[List[Union[dynamic_creation('VideoObject'), dynamic_creation('Clip'), str]], dynamic_creation('VideoObject'), dynamic_creation('Clip'), str]] = Field(
        default=None,
        description="An embedded video object.",
    )
    isPartOf: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, str]], AnyUrl, dynamic_creation('URL'), Any, str]] = Field(
        default=None,
        description="Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is"
     "part of.",
    )
    pattern: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",
    )
    editor: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Specifies the Person who edited the CreativeWork.",
    )
    dateModified: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="The date on which the CreativeWork was most recently modified or when the item's entry"
     "was modified within a DataFeed.",
    )
    translationOfWork: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The work that this work has been translated from. E.g. 物种起源 is a translationOf “On the"
     "Origin of Species”.",
    )
    creativeWorkStatus: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="The status of a creative work in terms of its stage in a lifecycle. Example terms include"
     "Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for"
     "the stages of their publication lifecycle.",
    )
    isBasedOnUrl: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, dynamic_creation('Product'), str]], AnyUrl, dynamic_creation('URL'), Any, dynamic_creation('Product'), str]] = Field(
        default=None,
        description="A resource that was used in the creation of this resource. This term can be repeated for"
     "multiple sources. For example, http://example.com/great-multiplication-intro.html.",
    )
    isFamilyFriendly: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="Indicates whether this content is family friendly.",
    )
    isAccessibleForFree: Optional[Union[List[Union[StrictBool, dynamic_creation('Boolean'), str]], StrictBool, dynamic_creation('Boolean'), str]] = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    author: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The author of this content or rating. Please note that author is special in that HTML 5"
     "provides a special mechanism for indicating authorship via the rel tag. That is equivalent"
     "to this and may be used interchangeably.",
    )
    contentReferenceTime: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), str]], datetime, dynamic_creation('DateTime'), str]] = Field(
        default=None,
        description="The specific time described by a creative work, for works (e.g. articles, video objects"
     "etc.) that emphasise a particular moment within an Event.",
    )
    correction: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CorrectionComment')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('CorrectionComment')]] = Field(
        default=None,
        description="Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]],"
     "textually or in another document.",
    )
    sdDatePublished: Optional[Union[List[Union[date, dynamic_creation('Date'), str]], date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="Indicates the date on which the current structured data was generated / published. Typically"
     "used alongside [[sdPublisher]]",
    )
    comment: Optional[Union[List[Union[dynamic_creation('Comment'), str]], dynamic_creation('Comment'), str]] = Field(
        default=None,
        description="Comments, typically from users.",
    )
    countryOfOrigin: Optional[Union[List[Union[dynamic_creation('Country'), str]], dynamic_creation('Country'), str]] = Field(
        default=None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    timeRequired: Optional[Union[List[Union[dynamic_creation('Duration'), str]], dynamic_creation('Duration'), str]] = Field(
        default=None,
        description="Approximate or typical time it takes to work with or through this learning resource for"
     "the typical intended target audience, e.g. 'PT30M', 'PT1H25M'.",
    )
    typicalAgeRange: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The typical expected age range, e.g. '7-9', '11-'.",
    )
    genre: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    producer: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The person or organization who produced the work (e.g. music album, movie, TV/radio"
     "series etc.).",
    )
    schemaVersion: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Indicates (by URL or string) a particular version of a schema used in some CreativeWork."
     "This property was created primarily to indicate the use of a specific schema.org release,"
     "e.g. ```10.0``` as a simple string, or more explicitly via URL, ```https://schema.org/docs/releases.html#v10.0```."
     "There may be situations in which other schemas might usefully be referenced this way,"
     "e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/```"
     "but this has not been carefully explored in the community.",
    )
    audience: Optional[Union[List[Union[dynamic_creation('Audience'), str]], dynamic_creation('Audience'), str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    encoding: Optional[Union[List[Union[dynamic_creation('MediaObject'), str]], dynamic_creation('MediaObject'), str]] = Field(
        default=None,
        description="A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.",
    )
    publisherImprint: Optional[Union[List[Union[dynamic_creation('Organization'), str]], dynamic_creation('Organization'), str]] = Field(
        default=None,
        description="The publishing division which published the comic.",
    )
    accessibilityAPI: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Indicates that the resource is compatible with the referenced accessibility API. Values"
     "should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityAPI-vocabulary).",
    )
    sdPublisher: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Indicates the party responsible for generating and publishing the current structured"
     "data markup, typically in cases where the structured data is derived automatically"
     "from existing published content but published on a different site. For example, student"
     "projects and open data initiatives often re-publish existing content with more explicitly"
     "structured metadata. The [[sdPublisher]] property helps make such practices more"
     "explicit.",
    )
    audio: Optional[Union[List[Union[dynamic_creation('MusicRecording'), dynamic_creation('Clip'), dynamic_creation('AudioObject'), str]], dynamic_creation('MusicRecording'), dynamic_creation('Clip'), dynamic_creation('AudioObject'), str]] = Field(
        default=None,
        description="An embedded audio object.",
    )
    accessibilityFeature: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Content features of the resource, such as accessible media, alternatives and supported"
     "enhancements for accessibility. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityFeature-vocabulary).",
    )
    spatialCoverage: Optional[Union[List[Union[dynamic_creation('Place'), str]], dynamic_creation('Place'), str]] = Field(
        default=None,
        description="The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of"
     "the content. It is a subproperty of contentLocation intended primarily for more technical"
     "and detailed materials. For example with a Dataset, it indicates areas that the dataset"
     "describes: a dataset of New York weather would have spatialCoverage which was the place:"
     "the state of New York.",
    )
    accessMode: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The human sensory perceptual system or cognitive faculty through which a person may"
     "process or perceive information. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessMode-vocabulary).",
    )
    editEIDR: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]]"
     "representing a specific edit / edition for a work of film or television. For example,"
     "the motion picture known as \"Ghostbusters\" whose [[titleEIDR]] is \"10.5240/7EC7-228A-510A-053E-CBB8-J\""
     "has several edits, e.g. \"10.5240/1F2A-E1C5-680A-14C6-E76B-I\" and \"10.5240/8A35-3BEE-6497-5D12-9E4F-3\"."
     "Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and"
     "their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general"
     "description), or alongside [[editEIDR]] for a more edit-specific description.",
    )
    usageInfo: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, str]], AnyUrl, dynamic_creation('URL'), Any, str]] = Field(
        default=None,
        description="The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]."
     "This property is applicable both to works that are freely available and to those that"
     "require payment or other transactions. It can reference additional information, e.g."
     "community expectations on preferred linking and citation conventions, as well as purchasing"
     "details. For something that can be commercially licensed, usageInfo can provide detailed,"
     "resource-specific information about licensing options. This property can be used"
     "alongside the license property which indicates license(s) applicable to some piece"
     "of content. The usageInfo property can provide information about other licensing options,"
     "e.g. acquiring commercial usage rights for an image that is also available under non-commercial"
     "creative commons licenses.",
    )
    position: Optional[Union[List[Union[int, dynamic_creation('Integer'), str, dynamic_creation('Text')]], int, dynamic_creation('Integer'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The position of an item in a series or sequence of items.",
    )
    encodingFormat: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)"
     "and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)),"
     "e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc. In"
     "cases where a [[CreativeWork]] has several media type representations, [[encoding]]"
     "can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]]"
     "information. Unregistered or niche encoding and file formats can be indicated instead"
     "via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.",
    )
    copyrightYear: Optional[Union[List[Union[StrictInt, StrictFloat, dynamic_creation('Number'), str]], StrictInt, StrictFloat, dynamic_creation('Number'), str]] = Field(
        default=None,
        description="The year during which the claimed copyright for the CreativeWork was first asserted.",
    )
    mainEntity: Optional[Union[List[Union[dynamic_creation('Thing'), str]], dynamic_creation('Thing'), str]] = Field(
        default=None,
        description="Indicates the primary entity described in some page or other CreativeWork.",
    )
    creator: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
     "CreativeWork.",
    )
    teaches: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]], str, dynamic_creation('Text'), dynamic_creation('DefinedTerm')]] = Field(
        default=None,
        description="The item being described is intended to help a person learn the competency or learning"
     "outcome defined by the referenced term.",
    )
    temporal: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), str, dynamic_creation('Text')]], datetime, dynamic_creation('DateTime'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The \"temporal\" property can be used in cases where more specific properties (e.g."
     "[[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]])"
     "are not known to be appropriate.",
    )
    size: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('DefinedTerm'), dynamic_creation('SizeSpecification'), dynamic_creation('QuantitativeValue')]], str, dynamic_creation('Text'), dynamic_creation('DefinedTerm'), dynamic_creation('SizeSpecification'), dynamic_creation('QuantitativeValue')]] = Field(
        default=None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",
    )
    translator: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Organization or person who adapts a creative work to different languages, regional"
     "differences and technical requirements of a target market, or that translates during"
     "some event.",
    )
    aggregateRating: Optional[Union[List[Union[dynamic_creation('AggregateRating'), str]], dynamic_creation('AggregateRating'), str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    accountablePerson: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Specifies the Person that is legally accountable for the CreativeWork.",
    )
    accessibilityHazard: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="A characteristic of the described resource that is physiologically dangerous to some"
     "users. Related to WCAG 2.0 guideline 2.3. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityHazard-vocabulary).",
    )
    contentRating: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('Rating')]], str, dynamic_creation('Text'), dynamic_creation('Rating')]] = Field(
        default=None,
        description="Official rating of a piece of content&#x2014;for example, 'MPAA PG-13'.",
    )
    recordedAt: Optional[Union[List[Union[dynamic_creation('Event'), str]], dynamic_creation('Event'), str]] = Field(
        default=None,
        description="The Event where the CreativeWork was recorded. The CreativeWork may capture all or part"
     "of the event.",
    )
    publication: Optional[Union[List[Union[dynamic_creation('PublicationEvent'), str]], dynamic_creation('PublicationEvent'), str]] = Field(
        default=None,
        description="A publication event associated with the item.",
    )
    sdLicense: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), Any, str]], AnyUrl, dynamic_creation('URL'), Any, str]] = Field(
        default=None,
        description="A license document that applies to this structured data, typically indicated by URL.",
    )
    headline: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Headline of the article.",
    )
    materialExtent: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('QuantitativeValue')]], str, dynamic_creation('Text'), dynamic_creation('QuantitativeValue')]] = Field(
        default=None,
        description="The quantity of the materials being described or an expression of the physical space"
     "they occupy.",
    )
    inLanguage: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('Language')]], str, dynamic_creation('Text'), dynamic_creation('Language')]] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    material: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('Product')]], AnyUrl, dynamic_creation('URL'), str, dynamic_creation('Text'), dynamic_creation('Product')]] = Field(
        default=None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",
    )
    datePublished: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]], datetime, dynamic_creation('DateTime'), date, dynamic_creation('Date'), str]] = Field(
        default=None,
        description="Date of first broadcast/publication.",
    )
    offers: Optional[Union[List[Union[dynamic_creation('Offer'), dynamic_creation('Demand'), str]], dynamic_creation('Offer'), dynamic_creation('Demand'), str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    hasPart: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some"
     "sense).",
    )
    sourceOrganization: Optional[Union[List[Union[dynamic_creation('Organization'), str]], dynamic_creation('Organization'), str]] = Field(
        default=None,
        description="The Organization on whose behalf the creator was working.",
    )
    sponsor: Optional[Union[List[Union[dynamic_creation('Organization'), dynamic_creation('Person'), str]], dynamic_creation('Organization'), dynamic_creation('Person'), str]] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    character: Optional[Union[List[Union[dynamic_creation('Person'), str]], dynamic_creation('Person'), str]] = Field(
        default=None,
        description="Fictional person connected with a creative work.",
    )
    pageEnd: Optional[Union[List[Union[int, dynamic_creation('Integer'), str, dynamic_creation('Text')]], int, dynamic_creation('Integer'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The page on which the work ends; for example \"138\" or \"xvi\".",
    )
    wordCount: Optional[Union[List[Union[int, dynamic_creation('Integer'), str]], int, dynamic_creation('Integer'), str]] = Field(
        default=None,
        description="The number of words in the text of the Article.",
    )
    articleSection: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports,"
     "Lifestyle, etc.",
    )
    articleBody: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The actual body of the article.",
    )
    speakable: Optional[Union[List[Union[AnyUrl, dynamic_creation('URL'), dynamic_creation('SpeakableSpecification'), str]], AnyUrl, dynamic_creation('URL'), dynamic_creation('SpeakableSpecification'), str]] = Field(
        default=None,
        description="Indicates sections of a Web page that are particularly 'speakable' in the sense of being"
     "highlighted as being especially appropriate for text-to-speech conversion. Other"
     "sections of a page may also be usefully spoken in particular circumstances; the 'speakable'"
     "property serves to indicate the parts most likely to be generally useful for speech."
     "The *speakable* property can be repeated an arbitrary number of times, with three kinds"
     "of possible 'content-locator' values: 1.) *id-value* URL references - uses *id-value*"
     "of an element in the page being annotated. The simplest use of *speakable* has (potentially"
     "relative) URL values, referencing identified sections of the document concerned."
     "2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute."
     "Use the [[cssSelector]] property. 3.) XPaths - addresses content via XPaths (assuming"
     "an XML view of the content). Use the [[xpath]] property. For more sophisticated markup"
     "of speakable sections beyond simple ID references, either CSS selectors or XPath expressions"
     "to pick out document section(s) as speakable. For this we define a supporting type, [[SpeakableSpecification]]"
     "which is defined to be a possible value of the *speakable* property.",
    )
    backstory: Optional[Union[List[Union[str, dynamic_creation('Text'), dynamic_creation('CreativeWork')]], str, dynamic_creation('Text'), dynamic_creation('CreativeWork')]] = Field(
        default=None,
        description="For an [[Article]], typically a [[NewsArticle]], the backstory property provides"
     "a textual summary giving a brief explanation of why and how an article was created. In"
     "a journalistic setting this could include information about reporting process, methods,"
     "interviews, data sources, etc.",
    )
    pagination: Optional[Union[List[Union[str, dynamic_creation('Text')]], str, dynamic_creation('Text')]] = Field(
        default=None,
        description="Any description of pages that is not separated into pageStart and pageEnd; for example,"
     "\"1-6, 9, 55\" or \"10-12, 46-49\".",
    )
    pageStart: Optional[Union[List[Union[int, dynamic_creation('Integer'), str, dynamic_creation('Text')]], int, dynamic_creation('Integer'), str, dynamic_creation('Text')]] = Field(
        default=None,
        description="The page on which the work starts; for example \"135\" or \"xiii\".",
    )
    sharedContent: Optional[Union[List[Union[dynamic_creation('CreativeWork'), str]], dynamic_creation('CreativeWork'), str]] = Field(
        default=None,
        description="A CreativeWork such as an image, video, or audio clip shared as part of this posting.",
    )
    liveBlogUpdate: Optional[Union[List[Union[dynamic_creation('BlogPosting'), str]], dynamic_creation('BlogPosting'), str]] = Field(
        default=None,
        description="An update to the LiveBlog.",
    )
    coverageStartTime: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), str]], datetime, dynamic_creation('DateTime'), str]] = Field(
        default=None,
        description="The time when the live blog will begin covering the Event. Note that coverage may begin"
     "before the Event's start time. The LiveBlogPosting may also be created before coverage"
     "begins.",
    )
    coverageEndTime: Optional[Union[List[Union[datetime, dynamic_creation('DateTime'), str]], datetime, dynamic_creation('DateTime'), str]] = Field(
        default=None,
        description="The time when the live blog will stop covering the Event. Note that coverage may continue"
     "after the Event concludes.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.PublicationEvent import PublicationEvent
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.WebPage import WebPage
    from pydantic import BaseModel
    from pydantic_schemaorg.Clip import Clip
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.AudioObject import AudioObject
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.BlogPosting import BlogPosting
    from pydantic_schemaorg.CorrectionComment import CorrectionComment
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.SpeakableSpecification import SpeakableSpecification
    from pydantic_schemaorg.Claim import Claim
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Rating import Rating
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.AlignmentObject import AlignmentObject
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.Comment import Comment
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.InteractionCounter import InteractionCounter
    from pydantic_schemaorg.SizeSpecification import SizeSpecification
