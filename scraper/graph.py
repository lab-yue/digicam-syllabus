from graphviz import Digraph
import store

syllabus_db = store.Instance()
syllabus_db.load()

search_db = store.Instance()
search_db.load("../data/search.json")

dot = Digraph(comment='DHU')

titleMap = {}

for s in syllabus_db.data:
    generalTitle = s['generalTitle']
    code = s['code']

    titleMap[generalTitle] = code
    dot.node(code, generalTitle)

titles = [*titleMap]

for x in titles:
    x_code = titleMap[x]
    for y in titles:
        for search_data in search_db.data:
            if search_data['id'] == x_code and y in search_data['text'] and x != y:
                dot.edge(titleMap[y], titleMap[x])

dot.render('../data/graph.gv')
