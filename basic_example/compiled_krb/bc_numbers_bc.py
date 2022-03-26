# bc_numbers_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def sacar_honores_corazones_conocidos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('numbers', 'honores_corazones', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_numbers.sacar_honores_corazones_conocidos: got unexpected plan from when clause 1"
            if context.lookup_data('puntos_max') < 6:
              if context.lookup_data('puntos_min') > -1:
                if context.lookup_data('puntos_max') == context.lookup_data('puntos_min'):
                  phrase_explained = "El jugador %s tiene %d PH en corazones\n" % (context.lookup_data('player'), context.lookup_data('puntos_min'))
                  rule1 = "INITIAL_FACT: honores_corazones(%s, %s, %s)\n" % (context.lookup_data('player'), context.lookup_data('puntos_min'), context.lookup_data('puntos_max'))
                  f = open("conclusiones_bc.txt", "a")
                  f.write(phrase_explained)
                  f.write(rule1)
                  f.close()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def evaluar_honores_corazones_conocidos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('numbers', 'honores_corazones_conocidos', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_numbers.evaluar_honores_corazones_conocidos: got unexpected plan from when clause 1"
            tot = 0
            with engine.prove('numbers', 'honores_corazones_new', context,
                              (rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "bc_numbers.evaluar_honores_corazones_conocidos: got unexpected plan from when clause 3"
                tot = tot + context.lookup_data('puntos')
                midRules = open("midRules.txt", "a")
                rule = "bc_numbers.honores_corazones_new(%s, %s)\n" % (context.lookup_data('player'), context.lookup_data('puntos'))
                midRules.write(rule)
                midRules.close()
            mark9 = context.mark(True)
            if rule.pattern(3).match_data(context, context,
                    int(tot)):
              context.end_save_all_undo()
              phrase_explained = "\nSe conocen %d PH en corazones\n" % (context.lookup_data('tot'))
              f = open("conclusiones_bc.txt", "a")
              f.write(phrase_explained)
              f.close()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark9)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sacar_honores_corazones_desconocidos_minimos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('numbers', 'honores_corazones', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_numbers.sacar_honores_corazones_desconocidos_minimos: got unexpected plan from when clause 1"
            if context.lookup_data('puntos_max') < 6:
              if context.lookup_data('puntos_min') > -1:
                if context.lookup_data('puntos_max') != context.lookup_data('puntos_min'):
                  phrase_explained = "El jugador %s tiene %d PH en corazones como minimo\n" % (context.lookup_data('player'), context.lookup_data('puntos_min'))
                  rule1 = "INITIAL_FACT: honores_corazones(%s, %s, %s)\n" % (context.lookup_data('player'), context.lookup_data('puntos_min'), context.lookup_data('puntos_max'))
                  f = open("conclusiones_bc.txt", "a")
                  f.write(phrase_explained)
                  f.write(rule1)
                  f.close()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def evaluar_honores_corazones_desconocidos_minimos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('numbers', 'honores_corazones_desconocidos_min', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_numbers.evaluar_honores_corazones_desconocidos_minimos: got unexpected plan from when clause 1"
            tot_min = 0
            midRules = open("midRules.txt", "a")
            with engine.prove('numbers', 'honores_corazones_min', context,
                              (rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_4:
              for x_4 in gen_4:
                assert x_4 is None, \
                  "bc_numbers.evaluar_honores_corazones_desconocidos_minimos: got unexpected plan from when clause 4"
                tot_min = tot_min + context.lookup_data('puntos')
                rule = "bc_numbers.honores_corazones_min(%s, %s)\n" % (context.lookup_data('player'), context.lookup_data('puntos'))
                midRules.write(rule)
            mark8 = context.mark(True)
            if rule.pattern(3).match_data(context, context,
                    int(tot_min)):
              context.end_save_all_undo()
              phrase_explained = "Se conocen %d PH en corazones como minimo\n" % (context.lookup_data('tot_min'))
              f = open("conclusiones_bc.txt", "a")
              f.write(phrase_explained)
              f.close()
              midRules.close()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark8)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def conclusiones_honores_corazones(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('numbers', 'honores_corazones_conocidos_new', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_numbers.conclusiones_honores_corazones: got unexpected plan from when clause 1"
            with engine.prove('numbers', 'honores_corazones_desconocidos_min_new', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_numbers.conclusiones_honores_corazones: got unexpected plan from when clause 2"
                num = context.lookup_data('tot')
                if (5-context.lookup_data('tot')-context.lookup_data('tot_min')) == 0:
                  phrase = "\nSE CONOCEN TODOS LOS PH EN CORAZONES!!!!!\nEsto es porque se conocen de seguro %d y como minimo %d, y el total debe ser 5.\n\n" % (context.lookup_data('tot'), context.lookup_data('tot_min'))
                  rule1 = "bc_numbers.honores_corazones_conocidos_new(%s)\n" % (context.lookup_data('tot'))
                  rule2 = "bc_numbers.honores_corazones_desconocidos_min_new(%s)\n" % (context.lookup_data('tot_min'))
                  f = open("conclusiones_bc.txt", "a")
                  midRules = open("midRules.txt", "a")
                  f.write(phrase)
                  midRules.write(rule1)
                  midRules.write(rule2)
                  f.close()
                  midRules.close()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def actualizar_honores_corazones_conocidos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'honores_corazones_FINAL', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_numbers.actualizar_honores_corazones_conocidos: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cerrar_honores_corazones_desconocidos(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('numbers', 'honores_corazones_FINAL', context,
                          ()) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_numbers.cerrar_honores_corazones_desconocidos: got unexpected plan from when clause 1"
            with engine.prove('numbers', 'honores_corazones_min', context,
                              (rule.pattern(0),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_numbers.cerrar_honores_corazones_desconocidos: got unexpected plan from when clause 2"
                phrase_explained = "El jugador %s tiene %d PH en corazones\n" % (context.lookup_data('player'), context.lookup_data('puntos'))
                rule1 = "bc_numbers.honores_corazones_min(%s, %s)\n" % (context.lookup_data('player'), context.lookup_data('puntos'))
                f = open("conclusiones_bc.txt", "a")
                midRules = open("midRules.txt", "a")
                f.write(phrase_explained)
                midRules.write("bc_numbers.honores_corazones_FINAL()\n")
                midRules.write(rule1)
                f.close()
                midRules.close()
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_numbers')
  
  bc_rule.bc_rule('sacar_honores_corazones_conocidos', This_rule_base, 'honores_corazones_new',
                  sacar_honores_corazones_conocidos, None,
                  (contexts.variable('player'),
                   contexts.variable('puntos_min'),),
                  (),
                  (contexts.variable('player'),
                   contexts.variable('puntos_min'),
                   contexts.variable('puntos_max'),))
  
  bc_rule.bc_rule('evaluar_honores_corazones_conocidos', This_rule_base, 'honores_corazones_conocidos_new',
                  evaluar_honores_corazones_conocidos, None,
                  (contexts.variable('tot'),),
                  (),
                  (contexts.variable('known'),
                   contexts.variable('player'),
                   contexts.variable('puntos'),
                   contexts.variable('tot'),))
  
  bc_rule.bc_rule('sacar_honores_corazones_desconocidos_minimos', This_rule_base, 'honores_corazones_min',
                  sacar_honores_corazones_desconocidos_minimos, None,
                  (contexts.variable('player'),
                   contexts.variable('puntos_min'),),
                  (),
                  (contexts.variable('player'),
                   contexts.variable('puntos_min'),
                   contexts.variable('puntos_max'),))
  
  bc_rule.bc_rule('evaluar_honores_corazones_desconocidos_minimos', This_rule_base, 'honores_corazones_desconocidos_min_new',
                  evaluar_honores_corazones_desconocidos_minimos, None,
                  (contexts.variable('tot_min'),),
                  (),
                  (contexts.variable('known'),
                   contexts.variable('player'),
                   contexts.variable('puntos'),
                   contexts.variable('tot_min'),))
  
  bc_rule.bc_rule('conclusiones_honores_corazones', This_rule_base, 'honores_corazones_FINAL',
                  conclusiones_honores_corazones, None,
                  (),
                  (),
                  (contexts.variable('tot'),
                   contexts.variable('tot_min'),))
  
  bc_rule.bc_rule('actualizar_honores_corazones_conocidos', This_rule_base, 'honores_corazones_conocidos_new',
                  actualizar_honores_corazones_conocidos, None,
                  (pattern.pattern_literal(5),),
                  (),
                  ())
  
  bc_rule.bc_rule('cerrar_honores_corazones_desconocidos', This_rule_base, 'honores_corazones_new_post',
                  cerrar_honores_corazones_desconocidos, None,
                  (contexts.variable('player'),
                   contexts.variable('puntos'),),
                  (),
                  (contexts.variable('player'),
                   contexts.variable('puntos'),))


Krb_filename = '../bc_numbers.krb'
Krb_lineno_map = (
    ((16, 20), (4, 4)),
    ((22, 29), (6, 6)),
    ((30, 30), (7, 7)),
    ((31, 31), (8, 8)),
    ((32, 32), (9, 9)),
    ((33, 33), (12, 12)),
    ((34, 34), (13, 13)),
    ((35, 35), (15, 15)),
    ((36, 36), (16, 16)),
    ((37, 37), (17, 17)),
    ((38, 38), (18, 18)),
    ((51, 55), (22, 22)),
    ((57, 62), (24, 24)),
    ((63, 63), (25, 25)),
    ((64, 70), (28, 28)),
    ((71, 71), (29, 29)),
    ((72, 72), (31, 31)),
    ((73, 73), (32, 32)),
    ((74, 74), (33, 33)),
    ((75, 75), (34, 34)),
    ((78, 78), (36, 36)),
    ((80, 80), (40, 40)),
    ((81, 81), (42, 42)),
    ((82, 82), (43, 43)),
    ((83, 83), (44, 44)),
    ((98, 102), (49, 49)),
    ((104, 111), (51, 51)),
    ((112, 112), (52, 52)),
    ((113, 113), (53, 53)),
    ((114, 114), (54, 54)),
    ((115, 115), (57, 57)),
    ((116, 116), (58, 58)),
    ((117, 117), (60, 60)),
    ((118, 118), (61, 61)),
    ((119, 119), (62, 62)),
    ((120, 120), (63, 63)),
    ((133, 137), (67, 67)),
    ((139, 144), (69, 69)),
    ((145, 145), (70, 70)),
    ((146, 146), (71, 71)),
    ((147, 153), (74, 74)),
    ((154, 154), (75, 75)),
    ((155, 155), (77, 77)),
    ((156, 156), (78, 78)),
    ((159, 159), (80, 80)),
    ((161, 161), (83, 83)),
    ((162, 162), (85, 85)),
    ((163, 163), (86, 86)),
    ((164, 164), (87, 87)),
    ((165, 165), (88, 88)),
    ((180, 184), (93, 93)),
    ((186, 191), (95, 95)),
    ((192, 197), (96, 96)),
    ((198, 198), (97, 97)),
    ((199, 199), (99, 99)),
    ((200, 200), (102, 102)),
    ((201, 201), (103, 103)),
    ((202, 202), (104, 104)),
    ((203, 203), (106, 106)),
    ((204, 204), (107, 107)),
    ((205, 205), (108, 108)),
    ((206, 206), (109, 109)),
    ((207, 207), (110, 110)),
    ((208, 208), (111, 111)),
    ((209, 209), (112, 112)),
    ((222, 226), (115, 115)),
    ((228, 233), (117, 117)),
    ((246, 250), (123, 123)),
    ((252, 257), (125, 125)),
    ((258, 264), (126, 126)),
    ((265, 265), (129, 129)),
    ((266, 266), (130, 130)),
    ((267, 267), (132, 132)),
    ((268, 268), (133, 133)),
    ((269, 269), (134, 134)),
    ((270, 270), (135, 135)),
    ((271, 271), (136, 136)),
    ((272, 272), (137, 137)),
    ((273, 273), (138, 138)),
)
