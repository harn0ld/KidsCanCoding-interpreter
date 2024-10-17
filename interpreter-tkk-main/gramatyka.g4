grammar gramatyka;

start: EOL* (statement EOL+)* statement? EOF;

statement:
    write_statement
    | get_statement
    | logic_statement
    | loop_statement
    | variable_definition
    | function_definition
    | expression;

write_statement:
    'write' expression
    | 'write(' expression ')';

get_statement:
    'get' Identifier
    | 'get(' Identifier ')';

logic_statement: 
    logic_keyword expression scope_body EOL? ('else' logic_keyword expression scope_body EOL?)* ('else' scope_body)?;

logic_keyword: 'if' | 'unless';

comparison_operator:
    'equal' 'to'
    | 'not' 'equal' 'to'
    | 'less' 'than'
    | 'not' 'less' 'than'
    | 'less' 'or' 'equal' 'to'
    | 'greater' 'than'
    | 'not' 'greater' 'than'
    | 'greater' 'or' 'equal' 'to';

expression:
    function_call
    | Identifier
    | String_literal
    | Number_literal
    | Boolean_literal
    | '(' expression ')'
    | arithmetic_expression
    | expression 'is' comparison_operator expression
    | expression 'or' expression
    | expression 'and' expression
    ;

arithmetic_expression: term (('+' | '-') term)*;

term: factor (('*' | '/') factor)*;

factor:
    function_call
    | Identifier
    | String_literal
    | Number_literal
    | '(' expression ')'
    ;

loop_statement:
    'while' expression scope_body
    | 'until' expression scope_body
    | expression 'times' scope_body
    | Number_literal 'times' scope_body
    ;

variable_definition:
    type Identifier ('is' expression)?;

function_definition:
    'function' Identifier '(' parameterList? ')' 'returns' (type | 'nothing') function_scope_body;

function_call: Identifier arguments;

arguments:
    '(' argument_list? ')';

argument_list: expression (',' expression)*;

parameterList: type Identifier (',' type Identifier)*;

scope_body:
    ':' EOL? statement
    | EOL? '{' EOL* (statement EOL+)* statement? '}';

function_scope_body:
    ':' EOL? (statement | 'return' expression)
    | EOL? '{' EOL* ((statement | 'return' expression) EOL+)*  '}';

type: 
    'number'
    | 'string'
    | 'character'
    | 'boolean';

Identifier: [a-zA-Z]+;
String_literal: '"' ~["]* '"';
Number_literal: [0-9]+;
Boolean_literal: 'true' | 'false';

WS: [ \t]+ -> skip;
COMMENT: '#' ~['#']* '#' -> skip;
EOL: [\n\r];

