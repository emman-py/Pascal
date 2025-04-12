grammar PascalSubset;

program: 'program' ID ';' declarations? mainBlock '.' EOF;

declarations: (varDecl | funcDecl | procDecl)+;

varDecl: 'var' varSection+;
varSection: ID (',' ID)* ':' type ';';
type: 'integer' | 'char' | 'boolean' | arrayType;
arrayType: 'array' '[' range ']' 'of' simpleType;
range: intRange | charRange;
intRange: INT '..' INT;
charRange: CHAR_LITERAL '..' CHAR_LITERAL;
simpleType: 'integer' | 'char' | 'boolean';

funcDecl: 'function' ID '(' params? ')' ':' type ';' declarations? funcBody ';';
procDecl: 'procedure' ID '(' params? ')' ';' declarations? procBody ';';
params: param (',' param)*;
param: ID (',' ID)* ':' type;
funcBody: 'begin' statementList 'end';
procBody: 'begin' statementList 'end';

mainBlock: 'begin' statementList 'end';

statementList: (statement ';'?)*;

statement: assignment
         | ifStatement
         | forStatement
         | whileStatement
         | repeatStatement
         | writeStatement
         | readStatement
         | funcCall
         | compoundStmt
         ;

assignment: ID ':=' expr | arrayAccess ':=' expr;
ifStatement: 'if' expr 'then' statement ('else' statement)?;
forStatement: 'for' ID ':=' expr 'to' expr 'do' statement;
whileStatement: 'while' expr 'do' statement;
repeatStatement: 'repeat' statementList 'until' expr;
writeStatement: ('Write'|'WriteLn') '(' (expr | STRING) (',' (expr | STRING))* ')';
readStatement: ('Read'|'ReadLn') '(' ID (',' ID)* ')';
funcCall: ID '(' (expr (',' expr)*)? ')';
compoundStmt: 'begin' statementList 'end';

arrayAccess: ID '[' expr ']';

expr: simpleExpr (('='|'<>'|'<'|'<='|'>'|'>=') simpleExpr)?;
simpleExpr: term (('+'|'-'|'or') term)*;
term: factor (('*'|'/'|'div'|'mod'|'and') factor)*;
factor: ID | INT | CHAR_LITERAL | '(' expr ')' | ('+'|'-'|'not') factor | funcCall | arrayAccess;

CHAR_LITERAL: '\'' . '\'';
STRING: '\'' (~['\\] | '\\' ['\\])* '\'';
ID: [a-zA-Z][a-zA-Z0-9_]*;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;