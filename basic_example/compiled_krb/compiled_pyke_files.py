# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_findall.krb'):
           [1646690861.895939, 'bc_findall_bc.py'],
         ('', '', 'bc_numbers.krb'):
           [1647800565.258052, 'bc_numbers_bc.py'],
         ('', '', 'fc_numbers.krb'):
           [1647803049.936769, 'fc_numbers_fc.py'],
         ('', '', 'numbers.kfb'):
           [1646690861.969036, 'numbers.fbc'],
        },
        compiler_version)

