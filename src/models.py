from typing import Optional, List

from pydantic import BaseModel, validator


class PydanticBase(BaseModel):
    name: str
    description: str
    valid_name: Optional[str] = None

    def clean_description(self):
        return self.description.replace("\\n", "").replace("\n", "")


class AttributeType(PydanticBase):
    type: str


class ModelAttributes(PydanticBase):
    fields: List[AttributeType]
    parents: List["ModelAttributes"]
    depth: int = 1
    filename: str = ""


