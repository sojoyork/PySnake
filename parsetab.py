
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMMA DIVIDE DOT ELSE ENJOY EQUALS FALSE FOREVER ID IF INPUT IS LBRACE LBRACKET LPAREN MAIN MINUS NOT NUMBER OR PLUS PRINT RBRACE RBRACKET RPAREN SEMICOLON STRING THEN TIMES TOML_END TOML_START TRUE UNTILprogram : ENJOY MAIN LPAREN RPAREN LBRACE statements RBRACEstatements : statements statement\n                  | statementstatement : ID DOT ID EQUALS boolean SEMICOLONboolean : TRUE\n               | FALSEstatement : IS ID SEMICOLONstatement : PRINT LPAREN STRING RPAREN SEMICOLONstatement : ID EQUALS expression SEMICOLONstatement : PRINT LPAREN ID RPAREN SEMICOLONexpression : expression PLUS term\n                  | expression MINUS termexpression : termterm : term TIMES factor\n            | term DIVIDE factorterm : factorfactor : NUMBERfactor : IDstatement : IF LPAREN boolean RPAREN LBRACE statements RBRACE else_partelse_part : ELSE LBRACE statements RBRACE\n                 | emptystatement : UNTIL LPAREN boolean RPAREN LBRACE statements RBRACEstatement : FOREVER LBRACE statements RBRACEstatement : ID EQUALS LBRACKET elements RBRACKET SEMICOLONelements : expression COMMA elements\n                | expression COMMA\n                | expressionexpression : ID LBRACKET expression RBRACKETexpression : LBRACKET elements RBRACKETstatement : ENJOY ID LPAREN RPAREN LBRACE statements RBRACEstatement : ID LPAREN RPAREN SEMICOLONempty :statement : TOML_START toml_content TOML_ENDtoml_content : toml_line toml_content\n                    | toml_linetoml_line : ID EQUALS STRING\n                 | ID EQUALS booleanstatement : ID EQUALS INPUT LPAREN STRING RPAREN SEMICOLONstatement : IF boolean THEN statementstatement : IF boolean THEN statement ELSE statementboolean : boolean OR boolean\n               | boolean AND boolean\n               | NOT boolean'
    
_lr_action_items = {'ENJOY':([0,6,8,9,19,31,45,49,54,55,61,70,74,78,81,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[2,7,7,-3,-2,7,-7,7,7,-33,-9,-31,-39,-23,7,-8,-10,7,7,7,7,-4,-24,7,-40,7,-30,-38,-32,-22,-19,-21,7,7,-20,]),'$end':([1,18,],[0,-1,]),'MAIN':([2,],[3,]),'LPAREN':([3,10,12,13,14,17,40,],[4,22,24,25,30,35,67,]),'RPAREN':([4,22,27,28,35,46,47,48,52,53,75,76,90,],[5,44,-5,-6,58,71,72,73,-43,77,-41,-42,104,]),'LBRACE':([5,15,58,73,77,113,],[6,31,81,95,97,115,]),'ID':([6,7,8,9,11,16,19,20,21,24,27,28,31,33,39,45,49,52,54,55,60,61,62,63,64,68,69,70,74,75,76,78,79,80,81,89,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[10,17,10,-3,23,34,-2,36,37,47,-5,-6,10,34,37,-7,10,-43,10,-33,37,-9,85,85,37,85,85,-31,-39,-41,-42,-23,-36,-37,10,37,-8,-10,10,10,10,10,-4,-24,10,-40,10,-30,-38,-32,-22,-19,-21,10,10,-20,]),'IS':([6,8,9,19,31,45,49,54,55,61,70,74,78,81,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[11,11,-3,-2,11,-7,11,11,-33,-9,-31,-39,-23,11,-8,-10,11,11,11,11,-4,-24,11,-40,11,-30,-38,-32,-22,-19,-21,11,11,-20,]),'PRINT':([6,8,9,19,31,45,49,54,55,61,70,74,78,81,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[12,12,-3,-2,12,-7,12,12,-33,-9,-31,-39,-23,12,-8,-10,12,12,12,12,-4,-24,12,-40,12,-30,-38,-32,-22,-19,-21,12,12,-20,]),'IF':([6,8,9,19,31,45,49,54,55,61,70,74,78,81,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[13,13,-3,-2,13,-7,13,13,-33,-9,-31,-39,-23,13,-8,-10,13,13,13,13,-4,-24,13,-40,13,-30,-38,-32,-22,-19,-21,13,13,-20,]),'UNTIL':([6,8,9,19,31,45,49,54,55,61,70,74,78,81,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[14,14,-3,-2,14,-7,14,14,-33,-9,-31,-39,-23,14,-8,-10,14,14,14,14,-4,-24,14,-40,14,-30,-38,-32,-22,-19,-21,14,14,-20,]),'FOREVER':([6,8,9,19,31,45,49,54,55,61,70,74,78,81,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[15,15,-3,-2,15,-7,15,15,-33,-9,-31,-39,-23,15,-8,-10,15,15,15,15,-4,-24,15,-40,15,-30,-38,-32,-22,-19,-21,15,15,-20,]),'TOML_START':([6,8,9,19,31,45,49,54,55,61,70,74,78,81,93,94,95,96,97,98,99,102,105,106,107,108,109,110,111,112,114,115,116,117,],[16,16,-3,-2,16,-7,16,16,-33,-9,-31,-39,-23,16,-8,-10,16,16,16,16,-4,-24,16,-40,16,-30,-38,-32,-22,-19,-21,16,16,-20,]),'RBRACE':([8,9,19,45,54,55,61,70,74,78,93,94,98,99,102,105,106,107,108,109,110,111,112,114,116,117,],[18,-3,-2,-7,78,-33,-9,-31,-39,-23,-8,-10,108,-4,-24,110,-40,111,-30,-38,-32,-22,-19,-21,117,-20,]),'DOT':([10,],[20,]),'EQUALS':([10,34,36,],[21,57,59,]),'TRUE':([13,25,29,30,50,51,57,59,],[27,27,27,27,27,27,27,27,]),'FALSE':([13,25,29,30,50,51,57,59,],[28,28,28,28,28,28,28,28,]),'NOT':([13,25,29,30,50,51,57,59,],[29,29,29,29,29,29,29,29,]),'LBRACKET':([21,37,39,60,64,89,],[39,60,64,64,64,64,]),'INPUT':([21,],[40,]),'NUMBER':([21,39,60,62,63,64,68,69,89,],[43,43,43,43,43,43,43,43,43,]),'SEMICOLON':([23,27,28,37,38,41,42,43,44,52,71,72,75,76,82,84,85,86,88,91,92,100,104,],[45,-5,-6,-18,61,-13,-16,-17,70,-43,93,94,-41,-42,99,-11,-18,-12,102,-14,-15,-28,109,]),'STRING':([24,57,67,],[46,79,90,]),'THEN':([26,27,28,52,75,76,],[49,-5,-6,-43,-41,-42,]),'OR':([26,27,28,48,52,53,75,76,80,82,],[50,-5,-6,50,50,50,50,50,50,50,]),'AND':([26,27,28,48,52,53,75,76,80,82,],[51,-5,-6,51,51,51,51,51,51,51,]),'TOML_END':([27,28,32,33,52,56,75,76,79,80,],[-5,-6,55,-35,-43,-34,-41,-42,-36,-37,]),'TIMES':([37,41,42,43,84,85,86,91,92,],[-18,68,-16,-17,68,-18,68,-14,-15,]),'DIVIDE':([37,41,42,43,84,85,86,91,92,],[-18,69,-16,-17,69,-18,69,-14,-15,]),'PLUS':([37,38,41,42,43,66,83,84,85,86,88,91,92,100,101,],[-18,62,-13,-16,-17,62,62,-11,-18,-12,-29,-14,-15,-28,-29,]),'MINUS':([37,38,41,42,43,66,83,84,85,86,88,91,92,100,101,],[-18,63,-13,-16,-17,63,63,-11,-18,-12,-29,-14,-15,-28,-29,]),'COMMA':([37,41,42,43,66,84,85,86,91,92,100,101,],[-18,-13,-16,-17,89,-11,-18,-12,-14,-15,-28,-29,]),'RBRACKET':([37,41,42,43,65,66,83,84,85,86,87,89,91,92,100,101,103,],[-18,-13,-16,-17,88,-27,100,-11,-18,-12,101,-26,-14,-15,-28,-29,-25,]),'ELSE':([45,55,61,70,74,78,93,94,99,102,106,108,109,110,111,112,114,117,],[-7,-33,-9,-31,96,-23,-8,-10,-4,-24,-40,-30,-38,113,-22,-19,-21,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([6,31,81,95,97,115,],[8,54,98,105,107,116,]),'statement':([6,8,31,49,54,81,95,96,97,98,105,107,115,116,],[9,19,9,74,19,9,9,106,9,19,19,19,9,19,]),'boolean':([13,25,29,30,50,51,57,59,],[26,48,52,53,75,76,80,82,]),'toml_content':([16,33,],[32,56,]),'toml_line':([16,33,],[33,33,]),'expression':([21,39,60,64,89,],[38,66,83,66,66,]),'term':([21,39,60,62,63,64,89,],[41,41,41,84,86,41,41,]),'factor':([21,39,60,62,63,64,68,69,89,],[42,42,42,42,42,42,91,92,42,]),'elements':([39,64,89,],[65,87,103,]),'else_part':([110,],[112,]),'empty':([110,],[114,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> ENJOY MAIN LPAREN RPAREN LBRACE statements RBRACE','program',7,'p_program','parser.py',12),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',17),
  ('statements -> statement','statements',1,'p_statements','parser.py',18),
  ('statement -> ID DOT ID EQUALS boolean SEMICOLON','statement',6,'p_statement_boolean_assign','parser.py',26),
  ('boolean -> TRUE','boolean',1,'p_boolean','parser.py',31),
  ('boolean -> FALSE','boolean',1,'p_boolean','parser.py',32),
  ('statement -> IS ID SEMICOLON','statement',3,'p_statement_is','parser.py',37),
  ('statement -> PRINT LPAREN STRING RPAREN SEMICOLON','statement',5,'p_statement_print','parser.py',42),
  ('statement -> ID EQUALS expression SEMICOLON','statement',4,'p_statement_assign','parser.py',47),
  ('statement -> PRINT LPAREN ID RPAREN SEMICOLON','statement',5,'p_statement_print_var','parser.py',51),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','parser.py',61),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','parser.py',62),
  ('expression -> term','expression',1,'p_expression_term','parser.py',66),
  ('term -> term TIMES factor','term',3,'p_term_binop','parser.py',70),
  ('term -> term DIVIDE factor','term',3,'p_term_binop','parser.py',71),
  ('term -> factor','term',1,'p_term_factor','parser.py',75),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser.py',79),
  ('factor -> ID','factor',1,'p_factor_id','parser.py',83),
  ('statement -> IF LPAREN boolean RPAREN LBRACE statements RBRACE else_part','statement',8,'p_statement_if','parser.py',88),
  ('else_part -> ELSE LBRACE statements RBRACE','else_part',4,'p_else_part','parser.py',92),
  ('else_part -> empty','else_part',1,'p_else_part','parser.py',93),
  ('statement -> UNTIL LPAREN boolean RPAREN LBRACE statements RBRACE','statement',7,'p_statement_until','parser.py',98),
  ('statement -> FOREVER LBRACE statements RBRACE','statement',4,'p_statement_forever','parser.py',102),
  ('statement -> ID EQUALS LBRACKET elements RBRACKET SEMICOLON','statement',6,'p_statement_assign_array','parser.py',107),
  ('elements -> expression COMMA elements','elements',3,'p_elements','parser.py',112),
  ('elements -> expression COMMA','elements',2,'p_elements','parser.py',113),
  ('elements -> expression','elements',1,'p_elements','parser.py',114),
  ('expression -> ID LBRACKET expression RBRACKET','expression',4,'p_expression_array_access','parser.py',123),
  ('expression -> LBRACKET elements RBRACKET','expression',3,'p_expression_array','parser.py',147),
  ('statement -> ENJOY ID LPAREN RPAREN LBRACE statements RBRACE','statement',7,'p_function_definition','parser.py',153),
  ('statement -> ID LPAREN RPAREN SEMICOLON','statement',4,'p_function_call','parser.py',158),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',167),
  ('statement -> TOML_START toml_content TOML_END','statement',3,'p_toml_block','parser.py',183),
  ('toml_content -> toml_line toml_content','toml_content',2,'p_toml_content','parser.py',198),
  ('toml_content -> toml_line','toml_content',1,'p_toml_content','parser.py',199),
  ('toml_line -> ID EQUALS STRING','toml_line',3,'p_toml_line','parser.py',206),
  ('toml_line -> ID EQUALS boolean','toml_line',3,'p_toml_line','parser.py',207),
  ('statement -> ID EQUALS INPUT LPAREN STRING RPAREN SEMICOLON','statement',7,'p_statement_input','parser.py',213),
  ('statement -> IF boolean THEN statement','statement',4,'p_statement_if_then','parser.py',219),
  ('statement -> IF boolean THEN statement ELSE statement','statement',6,'p_statement_if_then_else','parser.py',227),
  ('boolean -> boolean OR boolean','boolean',3,'p_boolean_expression','parser.py',235),
  ('boolean -> boolean AND boolean','boolean',3,'p_boolean_expression','parser.py',236),
  ('boolean -> NOT boolean','boolean',2,'p_boolean_expression','parser.py',237),
]
