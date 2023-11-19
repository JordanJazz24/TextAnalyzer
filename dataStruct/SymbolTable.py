
class SymbolTable:
    def __init__(self):
        self.dictionary = {}


    def hash_function(self, value):
        hash_value = 5381
        for char in value:
            hash_value = (hash_value << 5) + hash_value + ord(char)
        return hash_value

    def add_symbol(self, value, valor):
        key = self.hash_function(value)
        if self.dictionary.get(key) is None:
            self.dictionary[key] = valor

    def find_Symbol(self, value):
        key = self.hash_function(value);
        if self.dictionary.get(key) is None:
            return None
        else:
            return self.dictionary[key]


