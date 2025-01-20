from humps import camelize
from pydantic import BaseModel


class BaseSchema(BaseModel):
    """Base Schema"""

    class Config:
        """Base Schema Config"""

        from_attributes = True
        validate_assignment = True
        extra = "forbid"
        populate_by_name = True


class CamelModel(BaseSchema):
    class Config:
        alias_generator = camelize
