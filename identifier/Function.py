
class Function:
    def __init__(self, return_type, function_name, body, line_number):
        self.return_type = return_type
        self.function_name = function_name
        self.body = body
        self.line_number = line_number

    def get_return_type(self):
        return self.return_type

    def get_body(self):
        return self.body


