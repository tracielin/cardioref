#!/usr/bin/env python3

# Useful introduction to Graphviz:
# https://www.worthe-it.co.za/blog/2017-09-19-quick-introduction-to-graphviz.html

# need "pip install pygraphviz"
# which requires a local installation of graphviz
from pygraphviz import AGraph
# https://pygraphviz.github.io/documentation/latest/reference/agraph.html

def insert_newline(str_to_break: str, width: int) -> str:
    """
    given a long string,
    insert newline to limit displayed string length
    """
    new_str = ""
    this_line = ""
    for word in str_to_break.split(" "):
        this_line+=word+" "
        if len(this_line)>width:
            this_line+="\n"
            new_str+=this_line
            this_line=""
    new_str+=this_line
    return new_str


# import generate_graphviz as gg
if __name__ == "__main__":
    use_case = AGraph(directed=True, comment="an example", ratio="0.5")#, compound=True)
    use_case.clear()

    width=40

    use_case.add_node("early_hsPDA", label=insert_newline("Consider early targeted hsPDA prophylaxis with indomethacin (<24 hours) in selected infants by predefined criteria (e.g., male sex, ELBW, GA<26 weeks, low unit spontaneous closure rate)",width), shape="rectangle")
    use_case.add_node("done_after_hsPDA", label="done!")
    use_case.add_edge("early_hsPDA", "done_after_hsPDA", label="effective", color="green", constraint=False)
    use_case.add_node("ecg_assess", label=insert_newline("Perform screening echocardiography and conduct clinical assessment in all infants with ELBW and GA < 28 weeks",width), shape="rectangle")
    use_case.add_edge("early_hsPDA", "ecg_assess", label="no prophylaxis or not effective", color="red")
    use_case.add_node("pda_ib", label=insert_newline("consider early targeted treatment of infants with PDA with ibuprofen or indomethacin (<6 days postnatally and >2 L/minute, >0.25 FiO2)",width), shape="rectangle")
    use_case.add_edge("ecg_assess", "pda_ib")
    use_case.add_node("done_after_pda", label="done!")
    use_case.add_edge("pda_ib", "done_after_pda", color="green", constraint=False)
    use_case.add_node("ecg_vlbw", label=insert_newline("Perform clinical assessment and echocardiography in all infants with VLBW",width), shape="rectangle")
    use_case.add_edge("pda_ib", "ecg_vlbw", label="no treatment or not effective")
    use_case.add_edge("ecg_vlbw", "no hsPDA", color="green", constraint=False)
    use_case.add_edge("ecg_vlbw", "hsPDA", color="red")
    use_case.add_node("wait", label=insert_newline("consider watchful waiting and symptomatic treatment (>= 6 days postnatally)",width), shape="rectangle")
    use_case.add_edge("hsPDA", "wait")
    use_case.add_node("hsPDA_ib", label=insert_newline("consider treatment of symptomatic (> 2L/minute, >0.25 FiO2) infants with hsPDA with ibuprofen (>=6 days postnatally)",width), shape="rectangle")
    use_case.add_edge("hsPDA_ib", "wait", style="invis") # fake edge
    use_case.add_edge("hsPDA", "hsPDA_ib")
    use_case.add_node("ecg_repeat", label=insert_newline("reassess clinical status and echocardiography and consider repeating treatment",width), shape="rectangle")
    use_case.add_edge("wait", "ecg_repeat")
    use_case.add_edge("hsPDA_ib", "ecg_repeat")
    use_case.add_edge("ecg_repeat", "effective", color="green")
    use_case.add_edge("ecg_repeat", "not effective", color="red")
    use_case.add_edge("not effective", "consider rescue treatment (paracetamol)")
    use_case.add_node("close_duct", label=insert_newline("consider definite ductal closure by catheter intervention or surgical ligation if persistent and symptomatic over time",width), shape="rectangle")
    use_case.add_node("consider rescue treatment (paracetamol)", shape="rectangle")
    use_case.add_edge("consider rescue treatment (paracetamol)", "close_duct", label="if not effective", color="red", shape="rectangle")
    use_case.add_edge("not effective", "close_duct")
    use_case.add_edge("hsPDA", "close_duct", label="option")


    # https://groups.google.com/g/pygraphviz-discuss/c/t2KWtmpV-sc
    b = use_case.add_subgraph(["done_after_hsPDA", "ecg_assess"])
    b.graph_attr['rank']='same'
    c = use_case.add_subgraph(["done_after_pda", "ecg_vlbw"])
    c.graph_attr['rank']='same'
    d = use_case.add_subgraph(["no hsPDA", "hsPDA"])
    d.graph_attr['rank']='same'

    use_case.write("pda_preterm.dot")
    use_case.draw("pda_preterm.png", format="png", prog="dot")
