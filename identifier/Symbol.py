
class Symbol:
    def __init__(self, type, name, value, scope, line):
        self.type = type
        self.name = name
        self.scope = scope
        self.value = value
        self.line = line


    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_scope(self):
        return self.scope

    def get_value(self):
        return self.value


