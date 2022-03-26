# fc_numbers_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def sacar_honores_corazones_conocidos(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('numbers', 'honores_corazones', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('puntos_max') < 6:
          if context.lookup_data('puntos_min') > -1:
            if context.lookup_data('puntos_max') == context.lookup_data('puntos_min'):
              phrase_explained = "El jugador %s tiene %d PH en corazones\n" % (context.lookup_data('player'), context.lookup_data('puntos_min'))
              f = open("conclusiones.txt", "a")
              f.write(phrase_explained)
              f.close()
              engine.assert_('numbers', 'honores_corazones_new',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def evaluar_honores_corazones_conocidos(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('numbers', 'honores_corazones_conocidos', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        tot = 0
        with engine.lookup('numbers', 'honores_corazones_new', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            tot = tot + context.lookup_data('puntos')
        mark4 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                int(tot)):
          context.end_save_all_undo()
          phrase_explained = "\nSe conocen %d PH en corazones\n" % (context.lookup_data('tot'))
          f = open("conclusiones.txt", "a")
          f.write(phrase_explained)
          f.close()
          engine.assert_('numbers', 'honores_corazones_conocidos_new',
                         (rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark4)
  finally:
    context.done()

def sacar_honores_corazones_desconocidos_minimos(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('numbers', 'honores_corazones', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('puntos_max') < 6:
          if context.lookup_data('puntos_min') > -1:
            if context.lookup_data('puntos_max') != context.lookup_data('puntos_min'):
              phrase_explained = "El jugador %s tiene %d PH en corazones como minimo\n" % (context.lookup_data('player'), context.lookup_data('puntos_min'))
              f = open("conclusiones.txt", "a")
              f.write(phrase_explained)
              f.close()
              engine.assert_('numbers', 'honores_corazones_min',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def evaluar_honores_corazones_desconocidos_minimos(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('numbers', 'honores_corazones_desconocidos_min', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        tot_min = 0
        with engine.lookup('numbers', 'honores_corazones_min', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            tot_min = tot_min + context.lookup_data('puntos')
        mark4 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                int(tot_min)):
          context.end_save_all_undo()
          phrase_explained = "Se conocen %d PH en corazones como minimo\n" % (context.lookup_data('tot_min'))
          f = open("conclusiones.txt", "a")
          f.write(phrase_explained)
          f.close()
          engine.assert_('numbers', 'honores_corazones_desconocidos_min_new',
                         (rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark4)
  finally:
    context.done()

def conclusiones_honores_corazones(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('numbers', 'honores_corazones_conocidos_new', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('numbers', 'honores_corazones_desconocidos_min_new', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            num = context.lookup_data('tot')
            if (5-context.lookup_data('tot')-context.lookup_data('tot_min')) == 0:
              phrase = "\nSE CONOCEN TODOS LOS PH EN CORAZONES!!!!!\nEsto es porque se conocen de seguro %d y como minimo %d, y el total debe ser 5.\n\n" % (context.lookup_data('tot'), context.lookup_data('tot_min'))
              f = open("conclusiones.txt", "a")
              f.write(phrase)
              f.close()
              print phrase
              engine.assert_('numbers', 'honores_corazones_FINAL',
                             ()),
              engine.assert_('numbers', 'honores_corazones_conocidos_new',
                             (rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def cerrar_honores_corazones_desconocidos(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('numbers', 'honores_corazones_FINAL', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('numbers', 'honores_corazones_min', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            phrase_explained = "El jugador %s tiene %d PH en corazones\n" % (context.lookup_data('player'), context.lookup_data('puntos'))
            f = open("conclusiones.txt", "a")
            f.write(phrase_explained)
            f.close()
            engine.assert_('numbers', 'honores_corazones_new_post',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_numbers')
  
  fc_rule.fc_rule('sacar_honores_corazones_conocidos', This_rule_base, sacar_honores_corazones_conocidos,
    (('numbers', 'honores_corazones',
      (contexts.variable('player'),
       contexts.variable('puntos_min'),
       contexts.variable('puntos_max'),),
      False),),
    (contexts.variable('player'),
     contexts.variable('puntos_min'),))
  
  fc_rule.fc_rule('evaluar_honores_corazones_conocidos', This_rule_base, evaluar_honores_corazones_conocidos,
    (('numbers', 'honores_corazones_conocidos',
      (contexts.variable('known'),),
      False),
     ('numbers', 'honores_corazones_new',
      (contexts.variable('player'),
       contexts.variable('puntos'),),
      True),),
    (contexts.variable('tot'),))
  
  fc_rule.fc_rule('sacar_honores_corazones_desconocidos_minimos', This_rule_base, sacar_honores_corazones_desconocidos_minimos,
    (('numbers', 'honores_corazones',
      (contexts.variable('player'),
       contexts.variable('puntos_min'),
       contexts.variable('puntos_max'),),
      False),),
    (contexts.variable('player'),
     contexts.variable('puntos_min'),))
  
  fc_rule.fc_rule('evaluar_honores_corazones_desconocidos_minimos', This_rule_base, evaluar_honores_corazones_desconocidos_minimos,
    (('numbers', 'honores_corazones_desconocidos_min',
      (contexts.variable('known'),),
      False),
     ('numbers', 'honores_corazones_min',
      (contexts.variable('player'),
       contexts.variable('puntos'),),
      True),),
    (contexts.variable('tot_min'),))
  
  fc_rule.fc_rule('conclusiones_honores_corazones', This_rule_base, conclusiones_honores_corazones,
    (('numbers', 'honores_corazones_conocidos_new',
      (contexts.variable('tot'),),
      False),
     ('numbers', 'honores_corazones_desconocidos_min_new',
      (contexts.variable('tot_min'),),
      False),),
    (pattern.pattern_literal(5),))
  
  fc_rule.fc_rule('cerrar_honores_corazones_desconocidos', This_rule_base, cerrar_honores_corazones_desconocidos,
    (('numbers', 'honores_corazones_FINAL',
      (),
      False),
     ('numbers', 'honores_corazones_min',
      (contexts.variable('player'),
       contexts.variable('puntos'),),
      False),),
    (contexts.variable('player'),
     contexts.variable('puntos'),))


Krb_filename = '../fc_numbers.krb'
Krb_lineno_map = (
    ((13, 17), (7, 7)),
    ((18, 18), (9, 9)),
    ((19, 19), (10, 10)),
    ((20, 20), (11, 11)),
    ((21, 21), (14, 14)),
    ((22, 22), (16, 16)),
    ((23, 23), (17, 17)),
    ((24, 24), (18, 18)),
    ((25, 27), (21, 21)),
    ((36, 40), (26, 26)),
    ((41, 41), (27, 27)),
    ((42, 45), (30, 30)),
    ((46, 46), (32, 32)),
    ((49, 49), (34, 34)),
    ((51, 51), (38, 38)),
    ((52, 52), (40, 40)),
    ((53, 53), (41, 41)),
    ((54, 54), (42, 42)),
    ((55, 56), (45, 45)),
    ((67, 71), (51, 51)),
    ((72, 72), (53, 53)),
    ((73, 73), (54, 54)),
    ((74, 74), (55, 55)),
    ((75, 75), (58, 58)),
    ((76, 76), (60, 60)),
    ((77, 77), (61, 61)),
    ((78, 78), (62, 62)),
    ((79, 81), (65, 65)),
    ((90, 94), (70, 70)),
    ((95, 95), (71, 71)),
    ((96, 99), (74, 74)),
    ((100, 100), (76, 76)),
    ((103, 103), (78, 78)),
    ((105, 105), (81, 81)),
    ((106, 106), (83, 83)),
    ((107, 107), (84, 84)),
    ((108, 108), (85, 85)),
    ((109, 110), (88, 88)),
    ((121, 125), (94, 94)),
    ((126, 130), (95, 95)),
    ((131, 131), (96, 96)),
    ((132, 132), (99, 99)),
    ((133, 133), (107, 107)),
    ((134, 134), (109, 109)),
    ((135, 135), (110, 110)),
    ((136, 136), (111, 111)),
    ((137, 137), (112, 112)),
    ((138, 139), (115, 115)),
    ((140, 141), (116, 116)),
    ((150, 154), (124, 124)),
    ((155, 159), (125, 125)),
    ((160, 160), (128, 128)),
    ((161, 161), (130, 130)),
    ((162, 162), (131, 131)),
    ((163, 163), (132, 132)),
    ((164, 166), (135, 135)),
)
