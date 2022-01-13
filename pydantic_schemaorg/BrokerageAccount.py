from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InvestmentOrDeposit import InvestmentOrDeposit


class BrokerageAccount(InvestmentOrDeposit):
    """An account that allows an investor to deposit funds and place investment orders with"
     "a licensed broker or brokerage firm.

    See: https://schema.org/BrokerageAccount
    Model depth: 6
    """

    type_: str = Field("BrokerageAccount", const=True, alias="@type")


if TYPE_CHECKING:

    BrokerageAccount.update_forward_refs()
