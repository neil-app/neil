from ._base import ModelSchema
from ..models import Magazine


class MagazineSchema(ModelSchema):
    class Meta:
        model = Magazine
