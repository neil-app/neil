from ._base import ModelSchema
from ..models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        exclude = []
