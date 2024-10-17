# Generated from gramatyka.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatykaParser import gramatykaParser
else:
    from gramatykaParser import gramatykaParser

# This class defines a complete listener for a parse tree produced by gramatykaParser.
class gramatykaListener(ParseTreeListener):

    # Enter a parse tree produced by gramatykaParser#start.
    def enterStart(self, ctx:gramatykaParser.StartContext):
        pass

    # Exit a parse tree produced by gramatykaParser#start.
    def exitStart(self, ctx:gramatykaParser.StartContext):
        pass


    # Enter a parse tree produced by gramatykaParser#statement.
    def enterStatement(self, ctx:gramatykaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#statement.
    def exitStatement(self, ctx:gramatykaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#write_statement.
    def enterWrite_statement(self, ctx:gramatykaParser.Write_statementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#write_statement.
    def exitWrite_statement(self, ctx:gramatykaParser.Write_statementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#get_statement.
    def enterGet_statement(self, ctx:gramatykaParser.Get_statementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#get_statement.
    def exitGet_statement(self, ctx:gramatykaParser.Get_statementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#logic_statement.
    def enterLogic_statement(self, ctx:gramatykaParser.Logic_statementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#logic_statement.
    def exitLogic_statement(self, ctx:gramatykaParser.Logic_statementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#logic_keyword.
    def enterLogic_keyword(self, ctx:gramatykaParser.Logic_keywordContext):
        pass

    # Exit a parse tree produced by gramatykaParser#logic_keyword.
    def exitLogic_keyword(self, ctx:gramatykaParser.Logic_keywordContext):
        pass


    # Enter a parse tree produced by gramatykaParser#comparison_operator.
    def enterComparison_operator(self, ctx:gramatykaParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by gramatykaParser#comparison_operator.
    def exitComparison_operator(self, ctx:gramatykaParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by gramatykaParser#expression.
    def enterExpression(self, ctx:gramatykaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramatykaParser#expression.
    def exitExpression(self, ctx:gramatykaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramatykaParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:gramatykaParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by gramatykaParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:gramatykaParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by gramatykaParser#term.
    def enterTerm(self, ctx:gramatykaParser.TermContext):
        pass

    # Exit a parse tree produced by gramatykaParser#term.
    def exitTerm(self, ctx:gramatykaParser.TermContext):
        pass


    # Enter a parse tree produced by gramatykaParser#factor.
    def enterFactor(self, ctx:gramatykaParser.FactorContext):
        pass

    # Exit a parse tree produced by gramatykaParser#factor.
    def exitFactor(self, ctx:gramatykaParser.FactorContext):
        pass


    # Enter a parse tree produced by gramatykaParser#loop_statement.
    def enterLoop_statement(self, ctx:gramatykaParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#loop_statement.
    def exitLoop_statement(self, ctx:gramatykaParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#variable_definition.
    def enterVariable_definition(self, ctx:gramatykaParser.Variable_definitionContext):
        pass

    # Exit a parse tree produced by gramatykaParser#variable_definition.
    def exitVariable_definition(self, ctx:gramatykaParser.Variable_definitionContext):
        pass


    # Enter a parse tree produced by gramatykaParser#function_definition.
    def enterFunction_definition(self, ctx:gramatykaParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by gramatykaParser#function_definition.
    def exitFunction_definition(self, ctx:gramatykaParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by gramatykaParser#function_call.
    def enterFunction_call(self, ctx:gramatykaParser.Function_callContext):
        pass

    # Exit a parse tree produced by gramatykaParser#function_call.
    def exitFunction_call(self, ctx:gramatykaParser.Function_callContext):
        pass


    # Enter a parse tree produced by gramatykaParser#arguments.
    def enterArguments(self, ctx:gramatykaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by gramatykaParser#arguments.
    def exitArguments(self, ctx:gramatykaParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by gramatykaParser#argument_list.
    def enterArgument_list(self, ctx:gramatykaParser.Argument_listContext):
        pass

    # Exit a parse tree produced by gramatykaParser#argument_list.
    def exitArgument_list(self, ctx:gramatykaParser.Argument_listContext):
        pass


    # Enter a parse tree produced by gramatykaParser#parameterList.
    def enterParameterList(self, ctx:gramatykaParser.ParameterListContext):
        pass

    # Exit a parse tree produced by gramatykaParser#parameterList.
    def exitParameterList(self, ctx:gramatykaParser.ParameterListContext):
        pass


    # Enter a parse tree produced by gramatykaParser#scope_body.
    def enterScope_body(self, ctx:gramatykaParser.Scope_bodyContext):
        pass

    # Exit a parse tree produced by gramatykaParser#scope_body.
    def exitScope_body(self, ctx:gramatykaParser.Scope_bodyContext):
        pass


    # Enter a parse tree produced by gramatykaParser#function_scope_body.
    def enterFunction_scope_body(self, ctx:gramatykaParser.Function_scope_bodyContext):
        pass

    # Exit a parse tree produced by gramatykaParser#function_scope_body.
    def exitFunction_scope_body(self, ctx:gramatykaParser.Function_scope_bodyContext):
        pass


    # Enter a parse tree produced by gramatykaParser#type.
    def enterType(self, ctx:gramatykaParser.TypeContext):
        pass

    # Exit a parse tree produced by gramatykaParser#type.
    def exitType(self, ctx:gramatykaParser.TypeContext):
        pass



del gramatykaParser