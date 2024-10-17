

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in '\n\r':
                self.advance()
            elif self.current_char.isdigit():
                tokens.append(self.make_number())
            elif self.current_char.isalpha():
                tokens.append(self.make_identifier())
            elif self.current_char == '"':
                tokens.append(self.make_string())
            elif self.current_char == ':':
                tokens.append(Token('COLON'))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token('LBRACE'))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token('RBRACE'))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token('LPAREN'))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token('RPAREN'))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token('COMMA'))
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token('PLUS'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token('MINUS'))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token('MUL'))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token('DIV'))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token('EQUAL'))
                self.advance()
            elif self.current_char == 'o':
                tokens.append(self.make_keyword_or())
            elif self.current_char == 'a':
                tokens.append(self.make_keyword_and())
            elif self.current_char == 'w':
                tokens.append(self.make_keyword_while())
            elif self.current_char == 'u':
                tokens.append(self.make_keyword_until())
            elif self.current_char == 'f':
                tokens.append(self.make_keyword_function())
            elif self.current_char == 'r':
                tokens.append(self.make_keyword_returns())
            elif self.current_char == 'n':
                tokens.append(self.make_keyword_number())
            elif self.current_char == 's':
                tokens.append(self.make_keyword_string())
            elif self.current_char == 'c':
                tokens.append(self.make_keyword_character())
            elif self.current_char == 'b':
                tokens.append(self.make_keyword_boolean())
            elif self.current_char == 't':
                tokens.append(Token('BOOLEAN_LITERAL', 'true'))
                self.advance()
            elif self.current_char == 'f':
                tokens.append(Token('BOOLEAN_LITERAL', 'false'))
                self.advance()
            else:
                self.error()

        return tokens

    def make_number(self):
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return Token('NUMBER_LITERAL', int(num_str))

    def make_identifier(self):
        id_str = ''
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == '_'):
            id_str += self.current_char
            self.advance()
        if id_str in ('if', 'unless'):
            return Token('LOGIC_KEYWORD', id_str)
        elif id_str in ('true', 'false'):
            return Token('BOOLEAN_LITERAL', id_str)
        elif id_str in ('number', 'string', 'character', 'boolean'):
            return Token('TYPE', id_str)
        return Token('IDENTIFIER', id_str)

    def make_string(self):
        self.advance()  
        str_value = ''
        while self.current_char is not None and self.current_char != '"':
            str_value += self.current_char
            self.advance()
        if self.current_char == '"':
            self.advance()  
            return Token('STRING_LITERAL', str_value)
        else:
            self.error('Unterminated string')

    def make_keyword_or(self):
        if self.peek() == 'r':
            self.advance()
            if self.peek() == 'e':
                self.advance()
                return Token('OR', 'or')
        self.error()

    def make_keyword_and(self):
        if self.peek() == 'n':
            self.advance()
            if self.peek() == 'd':
                self.advance()
                return Token('AND', 'and')
        self.error()

    def make_keyword_while(self):
        if self.peek() == 'h':
            self.advance()
            if self.peek() == 'i':
                self.advance()
                if self.peek() == 'l':
                    self.advance()
                    if self.peek() == 'e':
                        self.advance()
                        return Token('WHILE', 'while')
        self.error()

    def make_keyword_until(self):
        if self.peek() == 'n':
            self.advance()
            if self.peek() == 't':
                self.advance()
                if self.peek() == 'i':
                    self.advance()
                    if self.peek() == 'l':
                        self.advance()
                        return Token('UNTIL', 'until')
        self.error()

    def make_keyword_function(self):
        if self.peek() == 'u':
            self.advance()
            if self.peek() == 'n':
                self.advance()
                if self.peek() == 'c':
                    self.advance()
                    if self.peek() == 't':
                        self.advance()
                        if self.peek() == 'i':
                            self.advance()
                            if self.peek() == 'o':
                                self.advance()
                                if self.peek() == 'n':
                                    self.advance()
                                    return Token('FUNCTION', 'function')
        self.error()

    def make_keyword_returns(self):
        if self.peek() == 'e':
            self.advance()
            if self.peek() == 't':
                self.advance()
                if self.peek() == 'u':
                    self.advance()
                    if self.peek() == 'r':
                        self.advance()
                        if self.peek() == 'n':
                            self.advance()
                            if self.peek() == 's':
                                self.advance()
                                return Token('RETURNS', 'returns')
        self.error()

    def make_keyword_number(self):
        if self.peek() == 'u':
            self.advance()
            if self.peek() == 'm':
                self.advance()
                if self.peek() == 'b':
                    self.advance()
                    if self.peek() == 'e':
                        self.advance()
                        if self.peek() == 'r':
                            self.advance()
                            return Token('TYPE', 'number')
        self.error()

    def make_keyword_string(self):
        if self.peek() == 't':
            self.advance()
            if self.peek() == 'r':
                self.advance()
                if self.peek() == 'i':
                    self.advance()
                    if self.peek() == 'n':
                        self.advance()
                        if self.peek() == 'g':
                            self.advance()
                            return Token('TYPE', 'string')
        self.error()

    def make_keyword_character(self):
        if self.peek() == 'h':
            self.advance()
            if self.peek() == 'a':
                self.advance()
                if self.peek() == 'r':
                    self.advance()
                    if self.peek() == 'a':
                        self.advance()
                        if self.peek() == 'c':
                            self.advance()
                            if self.peek() == 't':
                                self.advance()
                                if self.peek() == 'e':
                                    self.advance()
                                    if self.peek() == 'r':
                                        self.advance()
                                        return Token('TYPE', 'character')
        self.error()

    def make_keyword_boolean(self):
        if self.peek() == 'o':
            self.advance()
            if self.peek() == 'o':
                self.advance()
                if self.peek() == 'l':
                    self.advance()
                    if self.peek() == 'e':
                        self.advance()
                        if self.peek() == 'a':
                            self.advance()
                            if self.peek() == 'n':
                                self.advance()
                                return Token('TYPE', 'boolean')
        self.error()

    def peek(self):
        if self.pos + 1 < len(self.text):
            return self.text[self.pos + 1]
        return None


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = self.tokens[0]
        self.pos = 0

    def error(self):
        raise Exception('Invalid syntax')

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = Token('EOF')

    def parse(self):
        result = self.statement_list()
        if self.current_token.type != 'EOF':
            self.error()
        return result
    def write_statement(self):
        self.consume('WRITE')
        if self.current_token.type == 'LPAREN':
            self.advance()
            expr = self.expression()
            self.consume('RPAREN')
        else:
            expr = self.expression()
        return ('write_statement', expr)

    def get_statement(self):
        self.consume('GET')
        if self.current_token.type == 'LPAREN':
            self.advance()
            identifier = self.current_token.value
            self.consume('IDENTIFIER')
            self.consume('RPAREN')
        else:
            identifier = self.current_token.value
            self.consume('IDENTIFIER')
        return ('get_statement', identifier)

    # Override existing method
    def statement(self):
        if self.current_token.type == 'WRITE':
            return self.write_statement()
        elif self.current_token.type == 'GET':
            return self.get_statement()
        elif self.current_token.type == 'LOGIC_KEYWORD':
            return self.logic_statement()
        elif self.current_token.type in ('WHILE', 'UNTIL', 'NUMBER_LITERAL'):
            return self.loop_statement()
        elif self.current_token.type == 'TYPE':
            return self.variable_definition()
        elif self.current_token.type == 'FUNCTION':
            return self.function_definition()
        else:
            return self.expression()

    def logic_statement(self):
        if self.current_token.type == 'LOGIC_KEYWORD':
            keyword = self.current_token.value
            self.advance()
            expression = self.expression()
            true_body = self.scope_body()
            else_body = []
            if self.current_token.value == 'else':
                self.advance()
                if self.current_token.type == 'LOGIC_KEYWORD':
                    else_body.append(self.logic_statement())
                else:
                    else_body = self.scope_body()
            return ('logic_statement', keyword, expression, true_body, else_body)

    def expression(self):
        node = self.arithmetic_expression()
        while self.current_token.type in ('OR', 'AND'):
            op = self.current_token.value
            self.advance()
            right = self.arithmetic_expression()
            node = ('binary_operation', op, node, right)
        return node

    def arithmetic_expression(self):
        node = self.term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            op = self.current_token.value
            self.advance()
            right = self.term()
            node = ('binary_operation', op, node, right)
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in ('MUL', 'DIV'):
            op = self.current_token.value
            self.advance()
            right = self.factor()
            node = ('binary_operation', op, node, right)
        return node

    def factor(self):
        if self.current_token.type == 'LPAREN':
            self.advance()
            node = self.expression()
            self.consume('RPAREN')
            return node
        elif self.current_token.type in ('IDENTIFIER', 'STRING_LITERAL', 'NUMBER_LITERAL', 'BOOLEAN_LITERAL'):
            node = self.current_token
            self.advance()
            return node
        elif self.current_token.type == 'FUNCTION_CALL':
            return self.function_call()

    def loop_statement(self):
        if self.current_token.value == 'while':
            self.advance()
            condition = self.expression()
            body = self.scope_body()
            return ('while_loop', condition, body)
        elif self.current_token.value == 'until':
            self.advance()
            condition = self.expression()
            body = self.scope_body()
            return ('until_loop', condition, body)
        elif self.current_token.type == 'NUMBER_LITERAL':
            times = int(self.current_token.value)
            self.advance()
            body = self.scope_body()
            return ('loop_times', times, body)
        else:
            # Handle other loop types
            pass

    def variable_definition(self):
        var_type = self.current_token.value
        self.advance()
        identifier = self.current_token.value
        self.advance()
        if self.current_token.value == 'is':
            self.advance()
            expression = self.expression()
            return ('variable_definition', var_type, identifier, expression)
        else:
            return ('variable_definition', var_type, identifier, None)

    def function_definition(self):
        self.consume('FUNCTION')
        identifier = self.current_token.value
        self.consume('IDENTIFIER')
        self.consume('LPAREN')
        parameters = self.parameter_list()
        self.consume('RPAREN')
        self.consume('RETURNS')
        return_type = self.current_token.value
        self.consume('TYPE')
        body = self.function_scope_body()
        return ('function_definition', identifier, parameters, return_type, body)

    def function_call(self):
        identifier = self.current_token.value
        self.consume('IDENTIFIER')
        args = self.arguments()
        return ('function_call', identifier, args)

    def parameter_list(self):
        parameters = []
        if self.current_token.type == 'TYPE':
            parameters.append((self.current_token.value, self.current_token.value))
            self.advance()
            while self.current_token.value == ',':
                self.advance()
                parameters.append((self.current_token.value, self.current_token.value))
                self.advance()
        return parameters

    def arguments(self):
        args = []
        self.consume('LPAREN')
        if self.current_token.type != 'RPAREN':
            args.append(self.expression())
            while self.current_token.type == 'COMMA':
                self.advance()
                args.append(self.expression())
        self.consume('RPAREN')
        return args

    def scope_body(self):
        if self.current_token.type == 'COLON':
            self.advance()
            self.consume('EOL')
            statement = self.statement()
            return [statement]
        elif self.current_token.type == 'LBRACE':
            self.advance()
            self.consume('EOL')
            statements = []
            while self.current_token.type != 'RBRACE':
                statements.append(self.statement())
                self.consume('EOL')
            self.consume('RBRACE')
            return statements

    def function_scope_body(self):
        if self.current_token.type == 'COLON':
            self.advance()
            self.consume('EOL')
            statement = self.statement()
            return [statement]
        elif self.current_token.type == 'LBRACE':
            self.advance()
            self.consume('EOL')
            statements = []
            while self.current_token.type != 'RBRACE':
                statements.append(self.statement())
                self.consume('EOL')
            self.consume('RBRACE')
            return statements

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, text):
        lexer = Lexer(text)
        tokens = lexer.make_tokens()
        parser = Parser(tokens)
        result = parser.parse()
        return self.evaluate(result)

    def evaluate(self, node):
        if isinstance(node, tuple):
            if node[0] == 'variable_definition':
                _, var_type, identifier, expression = node
                if expression is not None:
                    self.variables[identifier] = self.evaluate(expression)
                else:
                    self.variables[identifier] = None
            elif node[0] == 'function_definition':
                _, identifier, parameters, return_type, body = node
                # Implement function definition handling here
                pass
            elif node[0] == 'loop_times':
                _, times, body = node
                for _ in range(times):
                    self.evaluate(body)
            elif node[0] in ('while_loop', 'until_loop'):
                _, condition, body = node
                while self.evaluate(condition):
                    self.evaluate(body)
            elif node[0] == 'LOGIC_KEYWORD':
                # Implement logic statement handling here
                pass
        elif isinstance(node, Token):
            if node.type == 'IDENTIFIER':
                return self.variables.get(node.value, None)
            elif node.type == 'NUMBER_LITERAL':
                return node.value
            elif node.type == 'STRING_LITERAL':
                return node.value
            elif node.type == 'BOOLEAN_LITERAL':
                return node.value == 'true'
        elif isinstance(node, list):
            for statement in node:
                self.evaluate(statement)
        return None
