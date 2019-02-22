from ._base import ModelSchema
from ..models import History


class HistorySchema(ModelSchema):
    class Meta:
        model = History
