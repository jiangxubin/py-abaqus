import sys
sys.path.append("D:\论文产出\小论文\py_thesis\src")
from auto_inp import PYXFEM

if __name__ == "__main__":
    PYXFEM.modify_inp(r"E:\workingspace\centrifuge\Job-centrifuge.inp", r"E:\workingspace\centrifuge\Job-centrifuge-modify.inp")