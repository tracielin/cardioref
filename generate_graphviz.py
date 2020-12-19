#!/usr/bin/env python3

# need "pip install pygraphviz"
# which requires a local installation of graphviz
from pygraphviz import AGraph
# https://pygraphviz.github.io/documentation/latest/reference/agraph.html

# import generate_graphviz as gg
if __name__ == "__main__":
    use_case = AGraph(directed=True, comment="an example")#, compound=True)
    use_case.clear()

    use_case.add_node(early_hsPDA, label="Consider early targeted hsPDA prophylaxis with indomethacin (<24 hours) in selected infants by predefined criteria (e.g., male sex, ELBW, GA<26 weeks, low unit spontaneous closure rate)")
    use_case.add_node(done_after_hsPDA, label="done!")
    use_case.add_edge(early_hsPDA, done_after_hsPDA, label="effective")
    use_case.add_node(ecg_assess, label="Perform screening echocardiography and conduct clinical assessment in all infants with ELBW and GA < 28 weeks")
    use_case.add_edge(early_hsPDA, ecg_assess, label="no prophylaxis or not effective")
    use_case.add_node(pda_ib, label="consider early targeted treatment of infants with PDA with ibuprofen or indomethacin (<6 days postnatally and >2 L/minute, >0.25 FiO2)")
    use_case.add_edge(ecg_assess, pda_ib)
    use_case.add_node(done_after_pda, label="done!")
    use_case.add_edge(pda_ib, done_after_pda)
    use_case.add_node(ecg_vlbw, label="Perform clinical assessment and echocardiography in all infants with VLBW")
    use_case.add_edge(pda_ib, ecg_vlbw, label="no treatment or not effective")
    use_case.add_edge(ecg_vlbw, "no hsPDA", color="green")
    use_case.add_edge(ecg_vlbw, "hsPDA", color="red")
    use_case.add_node(wait, label="consider watchful waiting and symptomatic treatment (>= 6 days postnatally)")
    use_case.add_edge("hsPDA", wait)
    use_case.add_node(hsPDA_ib, label="consider treatment of symptomatic (> 2L/minute, >0.25 FiO2) infants with hsPDA with ibuprofen (>=6 days postnatally)")
    use_case.add_edge("hsPDA". hsPDA_ib)
    use_case.add_node(ecg_repeat, label="reassess clinical status and echocardiography and consider repeating treatment")
    use_case.add_edge(wait, ecg_repeat)
    use_case.add_edge(hsPDA_ib, ecg_repeat)
    use_case.add_edge(ecg_repeat, "effective")
    use_case.add_edge(ecg_repeat, "not effective")
    use_case.add_edge("not effective", "consider rescue treatment (paracetamol")
    use_case.add_node(close_duct, label="consider definite ductal closure by catheter intervention or surgical ligation if persistent and symptomatic over time")
    use_case.add_edge( "consider rescue treatment (paracetamol", close_duct, label="if not effective")
    use_case.add_edge("not effective", close_duct)
    use_case.add_edge(hsPDA, close_duct, label="option")
    
    

    use_case.write()
    use_case.draw("pda_preterm.png", format="png", prog="dot")
