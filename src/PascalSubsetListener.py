# Generated from PascalSubset.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PascalSubsetParser import PascalSubsetParser
else:
    from PascalSubsetParser import PascalSubsetParser

# This class defines a complete listener for a parse tree produced by PascalSubsetParser.
class PascalSubsetListener(ParseTreeListener):

    # Enter a parse tree produced by PascalSubsetParser#program.
    def enterProgram(self, ctx:PascalSubsetParser.ProgramContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#program.
    def exitProgram(self, ctx:PascalSubsetParser.ProgramContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#declarations.
    def enterDeclarations(self, ctx:PascalSubsetParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#declarations.
    def exitDeclarations(self, ctx:PascalSubsetParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#varDecl.
    def enterVarDecl(self, ctx:PascalSubsetParser.VarDeclContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#varDecl.
    def exitVarDecl(self, ctx:PascalSubsetParser.VarDeclContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#varSection.
    def enterVarSection(self, ctx:PascalSubsetParser.VarSectionContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#varSection.
    def exitVarSection(self, ctx:PascalSubsetParser.VarSectionContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#type.
    def enterType(self, ctx:PascalSubsetParser.TypeContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#type.
    def exitType(self, ctx:PascalSubsetParser.TypeContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#arrayType.
    def enterArrayType(self, ctx:PascalSubsetParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#arrayType.
    def exitArrayType(self, ctx:PascalSubsetParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#range.
    def enterRange(self, ctx:PascalSubsetParser.RangeContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#range.
    def exitRange(self, ctx:PascalSubsetParser.RangeContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#intRange.
    def enterIntRange(self, ctx:PascalSubsetParser.IntRangeContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#intRange.
    def exitIntRange(self, ctx:PascalSubsetParser.IntRangeContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#charRange.
    def enterCharRange(self, ctx:PascalSubsetParser.CharRangeContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#charRange.
    def exitCharRange(self, ctx:PascalSubsetParser.CharRangeContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#simpleType.
    def enterSimpleType(self, ctx:PascalSubsetParser.SimpleTypeContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#simpleType.
    def exitSimpleType(self, ctx:PascalSubsetParser.SimpleTypeContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#funcDecl.
    def enterFuncDecl(self, ctx:PascalSubsetParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#funcDecl.
    def exitFuncDecl(self, ctx:PascalSubsetParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#procDecl.
    def enterProcDecl(self, ctx:PascalSubsetParser.ProcDeclContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#procDecl.
    def exitProcDecl(self, ctx:PascalSubsetParser.ProcDeclContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#params.
    def enterParams(self, ctx:PascalSubsetParser.ParamsContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#params.
    def exitParams(self, ctx:PascalSubsetParser.ParamsContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#param.
    def enterParam(self, ctx:PascalSubsetParser.ParamContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#param.
    def exitParam(self, ctx:PascalSubsetParser.ParamContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#funcBody.
    def enterFuncBody(self, ctx:PascalSubsetParser.FuncBodyContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#funcBody.
    def exitFuncBody(self, ctx:PascalSubsetParser.FuncBodyContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#procBody.
    def enterProcBody(self, ctx:PascalSubsetParser.ProcBodyContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#procBody.
    def exitProcBody(self, ctx:PascalSubsetParser.ProcBodyContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#mainBlock.
    def enterMainBlock(self, ctx:PascalSubsetParser.MainBlockContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#mainBlock.
    def exitMainBlock(self, ctx:PascalSubsetParser.MainBlockContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#statementList.
    def enterStatementList(self, ctx:PascalSubsetParser.StatementListContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#statementList.
    def exitStatementList(self, ctx:PascalSubsetParser.StatementListContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#statement.
    def enterStatement(self, ctx:PascalSubsetParser.StatementContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#statement.
    def exitStatement(self, ctx:PascalSubsetParser.StatementContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#assignment.
    def enterAssignment(self, ctx:PascalSubsetParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#assignment.
    def exitAssignment(self, ctx:PascalSubsetParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#ifStatement.
    def enterIfStatement(self, ctx:PascalSubsetParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#ifStatement.
    def exitIfStatement(self, ctx:PascalSubsetParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#forStatement.
    def enterForStatement(self, ctx:PascalSubsetParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#forStatement.
    def exitForStatement(self, ctx:PascalSubsetParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#whileStatement.
    def enterWhileStatement(self, ctx:PascalSubsetParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#whileStatement.
    def exitWhileStatement(self, ctx:PascalSubsetParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#repeatStatement.
    def enterRepeatStatement(self, ctx:PascalSubsetParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#repeatStatement.
    def exitRepeatStatement(self, ctx:PascalSubsetParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#writeStatement.
    def enterWriteStatement(self, ctx:PascalSubsetParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#writeStatement.
    def exitWriteStatement(self, ctx:PascalSubsetParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#readStatement.
    def enterReadStatement(self, ctx:PascalSubsetParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#readStatement.
    def exitReadStatement(self, ctx:PascalSubsetParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#funcCall.
    def enterFuncCall(self, ctx:PascalSubsetParser.FuncCallContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#funcCall.
    def exitFuncCall(self, ctx:PascalSubsetParser.FuncCallContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#compoundStmt.
    def enterCompoundStmt(self, ctx:PascalSubsetParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#compoundStmt.
    def exitCompoundStmt(self, ctx:PascalSubsetParser.CompoundStmtContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#arrayAccess.
    def enterArrayAccess(self, ctx:PascalSubsetParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#arrayAccess.
    def exitArrayAccess(self, ctx:PascalSubsetParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#expr.
    def enterExpr(self, ctx:PascalSubsetParser.ExprContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#expr.
    def exitExpr(self, ctx:PascalSubsetParser.ExprContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#simpleExpr.
    def enterSimpleExpr(self, ctx:PascalSubsetParser.SimpleExprContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#simpleExpr.
    def exitSimpleExpr(self, ctx:PascalSubsetParser.SimpleExprContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#term.
    def enterTerm(self, ctx:PascalSubsetParser.TermContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#term.
    def exitTerm(self, ctx:PascalSubsetParser.TermContext):
        pass


    # Enter a parse tree produced by PascalSubsetParser#factor.
    def enterFactor(self, ctx:PascalSubsetParser.FactorContext):
        pass

    # Exit a parse tree produced by PascalSubsetParser#factor.
    def exitFactor(self, ctx:PascalSubsetParser.FactorContext):
        pass



del PascalSubsetParser