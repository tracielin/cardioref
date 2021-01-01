#!/usr/bin/env python3

# Useful introduction to Graphviz:
# https://www.worthe-it.co.za/blog/2017-09-19-quick-introduction-to-graphviz.html

# need "pip install pygraphviz"
# which requires a local installation of graphviz
from pygraphviz import AGraph
# https://pygraphviz.github.io/documentation/latest/reference/agraph.html


# import generate_graphviz as gg
if __name__ == "__main__":
    use_case = AGraph(directed=True, comment="an example")#, ratio="0.5")#, compound=True)
    use_case.clear()

    width=40

    use_case.add_node("TOF repair with PR",shape="rectangle")
    use_case.add_node("lv_or_rv", label="severly decreased LV or RV systolic function")
    use_case.add_edge("TOF repair with PR","lv_or_rv")
    use_case.add_node("achd_class_1",label="evaluation by an ACHD cardiologist and \nadvanced HF team (class I)",shape="rectangle", constraint=False)
    use_case.add_edge("lv_or_rv","achd_class_1",label="yes",color="green")
    use_case.add_edge("achd_class_1","symptoms?",style="invis")
    use_case.add_edge("lv_or_rv","PR severity",label="no",color="red")
    use_case.add_node("follow_cardio",label="follow-up with ACHD cardiologist (class I)",shape="rectangle")
    use_case.add_node("PR severity", constraint=False, shape="invhouse")
    use_case.add_edge("PR severity","follow_cardio",label="mild PR",color="green")
    use_case.add_node("symptoms?",label="symptoms? dyspnea, \nchest pain, exercise \nintolerance referable to PR or \notherwise unexplained", shape="invhouse")
    use_case.add_edge("PR severity","symptoms?",label="moderate or more PR",color="red")
    use_case.add_node("pulmonary valve\nreplacement (class I)",shape="rectangle")
    use_case.add_edge("symptoms?","pulmonary valve\nreplacement (class I)",label="yes",color="green")
    use_case.add_node("two_of",label="two of\n- mild or moderate RV or\n LV systolic dysfunction\n- severe RV dilation \n(RVEDVI >=160 mL/m^2 or \nRVESVI >=80 mL/m^2 or \nRVEDV >=2x LVEDV)\n- RVSP due to RVOT \nobstruction >=2/3 systemic pressure\n-progressive reduction in \nobjective exercise tolerance", shape="rectangle")
    use_case.add_edge("symptoms?","two_of",label="no",color="red")
    use_case.add_node("pulmonary valve\nreplacement (class IIa)",shape="rectangle")
    use_case.add_node("pulmonary valve\nreplacement (class IIb)",shape="rectangle")
    use_case.add_edge("two_of","pulmonary valve\nreplacement (class IIa)",label="yes",color="green")
    use_case.add_node("sustained tachyarrhythmias",shape="invtrapezium")
    use_case.add_edge("two_of","sustained tachyarrhythmias",color="red")
    use_case.add_edge("sustained tachyarrhythmias","pulmonary valve\nreplacement (class IIb)",label="yes",color="green")
    use_case.add_node("residual_lesions",label="residual lesions requiring surgical intervention")
    use_case.add_edge("sustained tachyarrhythmias","residual_lesions",label="no",color="red")
    use_case.add_edge("residual_lesions","pulmonary valve\nreplacement (class IIb)",label="yes",color="green")
    use_case.add_edge("residual_lesions","follow_cardio",label="no",color="red")


    use_case.write("stout.dot")
    use_case.draw("stout.png", format="png", prog="dot")
