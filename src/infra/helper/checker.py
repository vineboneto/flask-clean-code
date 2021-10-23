class Checker:
    def __init__(self, values) -> None:
        self.values = values

    def of(values):
        return Checker(values)

    def exist(self, field_name):
        return self.values[field_name] if field_name in self.values else None
