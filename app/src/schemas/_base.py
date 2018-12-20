from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields

ma = Marshmallow()


class ModelSchema(ma.ModelSchema):
    created_at = fields.DateTime('%Y/%m/%d')
    updated_at = fields.DateTime('%Y/%m/%d')

    def __init__(self, *args, **kwargs):
        include = kwargs.get('include', [])
        exclude = kwargs.get('exclude', [])
        if not (isinstance(include, list) or isinstance(include, tuple)):
            raise ValueError('`include` option must be a list or tuple.')
        elif include:
            self.opts.exclude = list(set(self.opts.exclude) - set(include))
            del kwargs['include']
        if not (isinstance(exclude, list) or isinstance(exclude, tuple)):
            raise ValueError('`exclude` option must be a list or tuple.')
        elif exclude:
            self.opts.exclude = list(set(self.opts.exclude) | set(exclude))
            del kwargs['exclude']
        super().__init__(*args, **kwargs)

    def dump(self, obj, many=None, update_fields=True, **kwargs):
        # 最新のmarshmallowのdumpは引数がmanyまでなのでflask_marshmallowのバージョンがあがれば変更
        data = super().dump(obj, many=many, update_fields=update_fields, **kwargs)
        if hasattr(self.Meta, 'exclude'):
            # 親クラスのoptsは最初の１度しかインスタンスにならないためexcludeを元に戻す
            self.opts.exclude = self.Meta.exclude
        return data
