from ._base import ModelSchema
from ..models import Image


class ImageSchema(ModelSchema):
    class Meta:
        model = Image
