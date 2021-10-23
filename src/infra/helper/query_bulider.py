class QueryBuilder:
    def __init__(self, model=None, values: dict = None, query_fields: list[str] = None):
        self.model = model
        self.values = values
        self.query_fields = query_fields

    @staticmethod
    def select(model):
        return QueryBuilder(model=model)

    def these_values(self, values):
        self.values = values
        return self

    def these_fields(self, query_fields):
        self.query_fields = query_fields
        return self

    def done(self):
        queries = self.__wheres()
        data = self.model().filter_by_queries(queries)
        return data

    def __wheres(self):
        query = [self.__where(field_name) for field_name in self.query_fields]
        not_none = [i for i in query if type(i) != type(None)]
        return not_none

    def __where(self, field_name):
        if field_name in self.values:
            return getattr(self.model, field_name) == self.values[field_name]
