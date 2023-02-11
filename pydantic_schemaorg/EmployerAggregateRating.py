from __future__ import annotations
from pydantic import *
from typing import *
from datetime import *
from time import *


class EmployerAggregateRating(BaseModel):
    """An aggregate rating of an Organization related to its role as an employer.

    See: https://schema.org/EmployerAggregateRating
    Model depth: 5
    """
    type_: str = Field(default="EmployerAggregateRating", alias='@type', const=True)
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
    reviewAspect: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )
    author: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The author of this content or rating. Please note that author is special in that HTML 5"
     "provides a special mechanism for indicating authorship via the rel tag. That is equivalent"
     "to this and may be used interchangeably.",
    )
    ratingExplanation: Union[List[Union[Any, str]], Any, str] = Field(
        default=None,
        description="A short explanation (e.g. one to two sentences) providing background context and other"
     "information that led to the conclusion expressed in the rating. This is particularly"
     "applicable to ratings associated with \"fact check\" markup using [[ClaimReview]].",
    )
    bestRating: Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str] = Field(
        default=None,
        description="The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.",
    )
    ratingValue: Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str] = Field(
        default=None,
        description="The rating for the content. Usage guidelines: * Use values from 0123456789 (Unicode"
     "'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar"
     "Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate"
     "a decimal point. Avoid using these symbols as a readability separator.",
    )
    worstRating: Union[List[Union[Any, StrictInt, StrictFloat, str]], Any, StrictInt, StrictFloat, str] = Field(
        default=None,
        description="The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.",
    )
    itemReviewed: Optional[Union[List[Union[Any, str]], Any, str]] = Field(
        default=None,
        description="The item that is being reviewed/rated.",
    )
    ratingCount: Optional[Union[List[Union[Any, int, str]], Any, int, str]] = Field(
        default=None,
        description="The count of total number of ratings.",
    )
    reviewCount: Optional[Union[List[Union[Any, int, str]], Any, int, str]] = Field(
        default=None,
        description="The count of total number of reviews.",
    )
    
