from __future__ import annotations
from pydantic import BaseModel
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Country import Country
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.GeoShape import GeoShape
from pydantic_schemaorg.Text import Text
from pydantic_schemaorg.ContactPointOption import ContactPointOption
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.Language import Language
from pydantic_schemaorg.Intangible import Intangible
from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.URL import URL
from pydantic_schemaorg.Action import Action
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.Event import Event
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Product import Product
from pydantic_schemaorg.StructuredValue import StructuredValue


class PostalAddress(BaseModel):
    """The mailing address.

    See: https://schema.org/PostalAddress
    Model depth: 5
    """
    type_: str = Field(default="PostalAddress", alias='@type', const=True)
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
    serviceArea: Optional[Union[List[Union[AdministrativeArea, GeoShape, Place, str]], AdministrativeArea, GeoShape, Place, str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    availableLanguage: Optional[Union[List[Union[str, Text, Language]], str, Text, Language]] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]].",
    )
    productSupported: Optional[Union[List[Union[str, Text, Product]], str, Text, Product]] = Field(
        default=None,
        description="The product or service this support contact point is related to (such as product support"
     "for a particular product line). This can be a specific product or product line (e.g. \"iPhone\")"
     "or a general category of products or services (e.g. \"smartphones\").",
    )
    areaServed: Optional[Union[List[Union[str, Text, AdministrativeArea, Place, GeoShape]], str, Text, AdministrativeArea, Place, GeoShape]] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    contactOption: Optional[Union[List[Union[ContactPointOption, str]], ContactPointOption, str]] = Field(
        default=None,
        description="An option available on this contact point (e.g. a toll-free number or support for hearing-impaired"
     "callers).",
    )
    email: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="Email address.",
    )
    contactType: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="A person or organization can have different contact points, for different purposes."
     "For example, a sales contact point, a PR contact point and so on. This property is used"
     "to specify the kind of contact point.",
    )
    hoursAvailable: Optional[Union[List[Union[OpeningHoursSpecification, str]], OpeningHoursSpecification, str]] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    faxNumber: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The fax number.",
    )
    telephone: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The telephone number.",
    )
    addressLocality: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The locality in which the street address is, and which is in the region. For example, Mountain"
     "View.",
    )
    postOfficeBoxNumber: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The post office box number for PO box addresses.",
    )
    streetAddress: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The street address. For example, 1600 Amphitheatre Pkwy.",
    )
    addressCountry: Optional[Union[List[Union[str, Text, Country]], str, Text, Country]] = Field(
        default=None,
        description="The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2"
     "country code](http://en.wikipedia.org/wiki/ISO_3166-1).",
    )
    postalCode: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The postal code. For example, 94043.",
    )
    addressRegion: Optional[Union[List[Union[str, Text]], str, Text]] = Field(
        default=None,
        description="The region in which the locality is, and which is in the country. For example, California"
     "or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic import BaseModel
    from pydantic_schemaorg.ContactPointOption import ContactPointOption
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Place import Place
