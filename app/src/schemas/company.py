from ._base import ModelSchema
from ..models import Company


class CompantSchema(ModelSchema):
    class Meta:
        model = Company