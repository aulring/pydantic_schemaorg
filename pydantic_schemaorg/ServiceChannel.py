from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.PostalAddress import PostalAddress
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Language import Language
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.Action import Action


class ServiceChannel(BaseModel):
    """A means for accessing a service, e.g. a government office location, web site, or phone"
     "number.

    See: https://schema.org/ServiceChannel
    Model depth: 3
    """
    type_: str = Field(default="ServiceChannel", alias='@type', const=True)
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
    servicePhone: Optional[Union[List[Union[ContactPoint, str]], ContactPoint, str]] = Field(
        default=None,
        description="The phone number to use to access the service.",
    )
    availableLanguage: Optional[Union[List[Union[str, Text, Language]], str, Text, Language]] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]].",
    )
    serviceUrl: Optional[Union[List[Union[AnyUrl, URL, str]], AnyUrl, URL, str]] = Field(
        default=None,
        description="The website to access the service.",
    )
    processingTime: Optional[Union[List[Union[Duration, str]], Duration, str]] = Field(
        default=None,
        description="Estimated processing time for the service using this channel.",
    )
    servicePostalAddress: Optional[Union[List[Union[PostalAddress, str]], PostalAddress, str]] = Field(
        default=None,
        description="The address for accessing the service by mail.",
    )
    providesService: Optional[Union[List[Union[Service, str]], Service, str]] = Field(
        default=None,
        description="The service provided by this channel.",
    )
    serviceSmsNumber: Optional[Union[List[Union[ContactPoint, str]], ContactPoint, str]] = Field(
        default=None,
        description="The number to access the service by text message.",
    )
    serviceLocation: Optional[Union[List[Union[Place, str]], Place, str]] = Field(
        default=None,
        description="The location (e.g. civic structure, local business, etc.) where a person can go to access"
     "the service.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Place import Place
