from antlr4.tree.Tree import TerminalNodeImpl


class ASTPrinter:
    def __init__(self):
        self.output = ""
        self.indent_level = 0

    def visit(self, node):
        if isinstance(node, TerminalNodeImpl):
            self.output += "  " * self.indent_level + node.getText() + "\n"
        else:
            self.output += "  " * self.indent_level + type(node).__name__ + "\n"
            self.indent_level += 1
            for child in node.getChildren():
                self.visit(child)
            self.indent_level -= 1

    def get_output(self):
        return self.output
