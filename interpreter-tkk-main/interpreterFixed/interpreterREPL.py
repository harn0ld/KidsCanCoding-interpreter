from antlr4 import *
from gramatykaLexer import gramatykaLexer
from gramatykaParser import gramatykaParser
from gramatykaListener import gramatykaListener
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}, column {column}: {msg}")


class MyListener(gramatykaListener):
    def enterWrite_statement(self, ctx: gramatykaParser.Write_statementContext):
        expression = ctx.expression()
        if expression:
            print(expression.getText())


def main():
    lexer = gramatykaLexer(None)
    while True:
        try:
            code = input(">>> ")
            if not code:
                break
            lexer.inputStream = InputStream(code)
            lexer.removeErrorListeners()
            lexer.addErrorListener(MyErrorListener())
            stream = CommonTokenStream(lexer)
            parser = gramatykaParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(MyErrorListener())
            tree = parser.start()
            printer = MyListener()
            walker = ParseTreeWalker()
            walker.walk(printer, tree)
        except EOFError:
            break
        except SyntaxError as e:
            print(e)


if __name__ == '__main__':
    main()

