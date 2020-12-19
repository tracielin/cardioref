#!/usr/bin/env python3

# need "pip install pygraphviz"
# which requires a local installation of graphviz
from pygraphviz import AGraph
# https://pygraphviz.github.io/documentation/latest/reference/agraph.html

# import generate_graphviz as gg
if __name__ == "__main__":
    use_case = AGraph(directed=True, comment="an example")#, compound=True)
    use_case.clear()

    use_case.add_node("is chicken?", label="is the patient a chicken or human?")
    use_case.add_edge("is chicken?","does the human \nhave three arms?", label="human")
    use_case.add_edge("is chicken?","is the chicken happy?", label="chicken")
    use_case.add_edge("is chicken?","neither human\n nor chicken", label="other")

    use_case.add_node("eggs per day?", label="how many eggs per day?")
    use_case.add_edge("is the chicken happy?", "eggs per day?", label="yes, happy")
    use_case.add_edge("is the chicken happy?", "eggs per day?", label="no, unhappy")

    use_case.write()
    use_case.draw("best_graph.png", format="png", prog="dot")
