from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if hasattr(offendingSymbol, 'line'):
            line = offendingSymbol.line
            column = offendingSymbol.column
        print(f"Syntax error at line {line}, column {column}: {msg}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        start = recognizer.getTokenStream().get(startIndex)
        stop = recognizer.getTokenStream().get(stopIndex)
        print(f"Ambiguity between lines {start.line}-{stop.line}")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass  # Можно добавить обработку при необходимости

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass  # Можно добавить обработку при необходимости
