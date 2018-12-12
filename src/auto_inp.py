"""
For the size effect study of excavation, develop a script to simply the process of create a new model out of Abaqus CAE
from scratch.
Actually it is a simple text process script :Just some substitution and adding.
"""

import re

in_inp_path = r"E:\workingspace\centrifuge\Job-centrifuge.inp"
out_inp_path = r"E:\workingspace\centrifuge\Job-centrifuge-modify.inp"


class PYXFEM:
    @staticmethod
    def modify_inp(node_left, node_right, flow_rate=5e-5, origin_inp_path=in_inp_path, output_inp_path=out_inp_path):
        """
        For the python interface of Abaqus couldn't add surface with certain type, it's necessary to modify the inp file
        manually. Following steps are completed in this function:Add XFEM surface, Define the enrichment initial condition,
        Add XFEM boundary conditions, Add fluid injection,
        :param origin_inp_path: original inp file path
        :param output_inp_path: modified inp file path
        :return: None
        """
        # xfem_surf_pat = re.compile(r"\*Enrichment")
        xfem_surf_pat = re.compile(r"\*Surface, type=ELEMENT, name=penetration-surface")
        phantom_pat = re.compile("\*\* BOUNDARY CONDITIONS")
        phantom_count = 0
        crack_modify_count = False
        cflow_pat = re.compile(r"0.05, 100., 1e-12, 5., ")
        output_pat = re.compile(r"CDISP, CSTRESS")
        step_control_modify = False
        start_cflow = False
        step_control_pat = re.compile(r"\*Step, name=injection, nlgeom=YES, unsymm=YES")
        fo = open(output_inp_path, 'w')
        with open(origin_inp_path, 'r') as f:
            for line in f:
                if re.match(xfem_surf_pat, line):
                    crack_modify_count = True
                    fo.write("*Surface, type=ELEMENT, name=penetration-surface, type=XFEM\n")
                    fo.write("Crack-1\n")
                    continue
                if crack_modify_count:
                    crack_modify_count = False
                    continue
                if re.match(step_control_pat, line):
                    step_control_modify = True
                    fo.write(line)
                    fo.write("*Soils, consolidation, end=PERIOD, utol=1e+09,stabilize=0.0002, allsdtol=0.05, continue=NO\n")
                    continue
                if step_control_modify:
                    step_control_modify = False
                    continue
                fo.write(line)
                if re.match(cflow_pat, line):
                    fo.write("*cflow,amplitude=volumerate,phantom=edge\n")
                    fo.write("soil-1.{0}, soil-1.{1}, {2}\n".format(node_left, node_right, flow_rate))
                if re.match(output_pat, line):
                    fo.write("*element output,elset=xfem-ele-set\n")
                    fo.write("PFOPENXFEM\n")
                    fo.write("PORPRES\n")
                    fo.write("PFOPENXFEMCOMP\n")
                    fo.write("PORPRESCOMP\n")
                if re.match(phantom_pat, line):
                    phantom_count += 1
                    if phantom_count>=2:
                        continue
                    else:
                        fo.write("*Boundary, phantom=node\n")
                        fo.write("soil-1.{}, 2,2\n".format(node_left))
                        fo.write("soil-1.{}, 2,2\n".format(node_right))


if __name__ == "__main__":
    PYXFEM.modify_inp(123, 234)