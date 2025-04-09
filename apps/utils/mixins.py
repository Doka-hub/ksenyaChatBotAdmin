class SetValuesModelMixin:
    def set_values(self, **values):
        for field, value in values.items():
            setattr(self, field, value)
