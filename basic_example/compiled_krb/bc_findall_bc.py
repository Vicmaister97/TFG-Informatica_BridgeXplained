# bc_findall_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def collect_siblings(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'child_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_findall.collect_siblings: got unexpected plan from when clause 1"
            siblings = []
            with engine.prove('family', 'child_of', context,
                              (rule.pattern(3),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "bc_findall.collect_siblings: got unexpected plan from when clause 3"
                if context.lookup_data('sibling') != context.lookup_data('child'):
                  siblings.append(context.lookup_data('sibling'))
            mark6 = context.mark(True)
            if rule.pattern(4).match_data(context, context,
                    tuple(siblings)):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def collect_cousins(rule, arg_patterns, arg_context):
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
        with engine.prove('family', 'child_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_findall.collect_cousins: got unexpected plan from when clause 1"
            cousins = []
            with engine.prove(rule.rule_base.root_name, 'siblings_of', context,
                              (rule.pattern(1),
                               rule.pattern(3),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "bc_findall.collect_cousins: got unexpected plan from when clause 3"
                for python_ans in \
                     context.lookup_data('father_siblings'):
                  mark4 = context.mark(True)
                  if rule.pattern(4).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    with engine.prove('family', 'child_of', context,
                                      (rule.pattern(5),
                                       rule.pattern(4),
                                       rule.pattern(6),)) \
                      as gen_5:
                      for x_5 in gen_5:
                        assert x_5 is None, \
                          "bc_findall.collect_cousins: got unexpected plan from when clause 5"
                        cousins.append(context.lookup_data('cousin'))
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                for python_ans in \
                     context.lookup_data('father_siblings'):
                  mark7 = context.mark(True)
                  if rule.pattern(4).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    with engine.prove('family', 'child_of', context,
                                      (rule.pattern(5),
                                       rule.pattern(6),
                                       rule.pattern(4),)) \
                      as gen_8:
                      for x_8 in gen_8:
                        assert x_8 is None, \
                          "bc_findall.collect_cousins: got unexpected plan from when clause 8"
                        cousins.append(context.lookup_data('cousin'))
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark7)
            with engine.prove(rule.rule_base.root_name, 'siblings_of', context,
                              (rule.pattern(2),
                               rule.pattern(7),)) \
              as gen_10:
              for x_10 in gen_10:
                assert x_10 is None, \
                  "bc_findall.collect_cousins: got unexpected plan from when clause 10"
                for python_ans in \
                     context.lookup_data('mother_siblings'):
                  mark11 = context.mark(True)
                  if rule.pattern(8).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    with engine.prove('family', 'child_of', context,
                                      (rule.pattern(5),
                                       rule.pattern(6),
                                       rule.pattern(8),)) \
                      as gen_12:
                      for x_12 in gen_12:
                        assert x_12 is None, \
                          "bc_findall.collect_cousins: got unexpected plan from when clause 12"
                        cousins.append(context.lookup_data('cousin'))
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark11)
                for python_ans in \
                     context.lookup_data('mother_siblings'):
                  mark14 = context.mark(True)
                  if rule.pattern(8).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    with engine.prove('family', 'child_of', context,
                                      (rule.pattern(5),
                                       rule.pattern(8),
                                       rule.pattern(6),)) \
                      as gen_15:
                      for x_15 in gen_15:
                        assert x_15 is None, \
                          "bc_findall.collect_cousins: got unexpected plan from when clause 15"
                        cousins.append(context.lookup_data('cousin'))
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark14)
            mark17 = context.mark(True)
            if rule.pattern(9).match_data(context, context,
                    tuple(cousins)):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark17)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_findall')
  
  bc_rule.bc_rule('collect_siblings', This_rule_base, 'siblings_of',
                  collect_siblings, None,
                  (contexts.variable('child'),
                   contexts.variable('siblings'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('sibling'),
                   contexts.variable('siblings'),))
  
  bc_rule.bc_rule('collect_cousins', This_rule_base, 'cousins_of',
                  collect_cousins, None,
                  (contexts.variable('child'),
                   contexts.variable('cousins'),),
                  (),
                  (contexts.variable('child'),
                   contexts.variable('father'),
                   contexts.variable('mother'),
                   contexts.variable('father_siblings'),
                   contexts.variable('father_sibling'),
                   contexts.variable('cousin'),
                   contexts.anonymous('_'),
                   contexts.variable('mother_siblings'),
                   contexts.variable('mother_sibling'),
                   contexts.variable('cousins'),))


Krb_filename = '../bc_findall.krb'
Krb_lineno_map = (
    ((16, 20), (4, 4)),
    ((22, 29), (6, 6)),
    ((30, 30), (7, 7)),
    ((31, 38), (9, 9)),
    ((39, 39), (10, 10)),
    ((40, 40), (11, 11)),
    ((43, 43), (12, 12)),
    ((59, 63), (15, 15)),
    ((65, 72), (17, 17)),
    ((73, 73), (19, 19)),
    ((74, 80), (21, 21)),
    ((82, 82), (23, 23)),
    ((86, 93), (24, 24)),
    ((94, 94), (25, 25)),
    ((98, 98), (28, 28)),
    ((102, 109), (29, 29)),
    ((110, 110), (30, 30)),
    ((113, 119), (33, 33)),
    ((121, 121), (36, 36)),
    ((125, 132), (37, 37)),
    ((133, 133), (38, 38)),
    ((137, 137), (41, 41)),
    ((141, 148), (42, 42)),
    ((149, 149), (43, 43)),
    ((154, 154), (45, 45)),
)
