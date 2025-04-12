from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl

from PascalSubsetLexer import PascalSubsetLexer
from PascalSubsetParser import PascalSubsetParser
from CustomErrorListener import CustomErrorListener
from colorama import init, Fore, Style

init()  # Инициализация colorama для цветного вывода


class ColoredASTPrinter:
    def __init__(self):
        self.output = ""
        self.indent_level = 0
        self.colors = {
            'TerminalNodeImpl': Fore.YELLOW,
            'ProgramContext': Fore.CYAN,
            'VarDeclContext': Fore.GREEN,
            'FuncDeclContext': Fore.MAGENTA,
            'ProcDeclContext': Fore.MAGENTA,
            'TypeContext': Fore.BLUE,
            'StatementContext': Fore.WHITE,
            'ExprContext': Fore.RED,
        }

    def get_color(self, node_type):
        return self.colors.get(node_type, Fore.WHITE)

    def visit(self, node):
        if isinstance(node, TerminalNodeImpl):
            node_type = type(node).__name__
            color = self.get_color(node_type)
            self.output += "  " * self.indent_level + color + node.getText() + Style.RESET_ALL + "\n"
        else:
            node_type = type(node).__name__
            color = self.get_color(node_type)
            self.output += "  " * self.indent_level + color + node_type + Style.RESET_ALL + "\n"
            self.indent_level += 1
            for child in node.getChildren():
                self.visit(child)
            self.indent_level -= 1

    def get_output(self):
        return self.output

    def print_to_console(self):
        print("\n" + "=" * 50 + " AST Tree " + "=" * 50)
        print(self.output)
        print("=" * 100 + "\n")


def main():
    try:
        input_stream = FileStream("input.pas", encoding='utf-8')
        lexer = PascalSubsetLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PascalSubsetParser(stream)

        parser.removeErrorListeners()
        error_listener = CustomErrorListener()
        parser.addErrorListener(error_listener)

        tree = parser.program()

        # Вывод AST в файл
        printer = ColoredASTPrinter()
        printer.visit(tree)

        with open("ast_output.txt", "w", encoding='utf-8') as f:
            f.write(printer.get_output())

        # Вывод AST в терминал с цветами
        printer.print_to_console()

        print(Fore.GREEN + "Parsing completed successfully!" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "Error: input.pas file not found" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
