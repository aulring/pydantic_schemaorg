from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.GeoShape import GeoShape


class GeoCircle(GeoShape):
    """A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape"
     "it provides the simple textual property 'circle', but also allows the combination of"
     "postalCode alongside geoRadius. The center of the circle can be indicated via the 'geoMidpoint'"
     "property, or more approximately using 'address', 'postalCode'.

    See: https://schema.org/GeoCircle
    Model depth: 5
    """

    type_: str = Field("GeoCircle", const=True, alias="@type")
    geoMidpoint: "Optional[Union[List[Union[GeoCoordinates, str]], Union[GeoCoordinates, str]]]" = Field(
        None,
        description="Indicates the GeoCoordinates at the centre of a GeoShape e.g. GeoCircle.",
    )
    geoRadius: "Optional[Union[List[Union[Decimal, str, Distance]], Union[Decimal, str, Distance]]]" = Field(
        None,
        description="Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise"
        "via Distance notation).",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.GeoCoordinates import GeoCoordinates

    from decimal import Decimal

    from pydantic_schemaorg.Distance import Distance

    GeoCircle.update_forward_refs()
