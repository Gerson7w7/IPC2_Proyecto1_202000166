import graphviz

def graficaG(terreno):
    g = graphviz.Graph('G', filename='process.gv')

    g.edge('run', 'intr')
    g.edge('intr', 'runbl')
    g.edge('runbl', 'run')
    g.edge('run', 'kernel')
    g.edge('kernel', 'zombie')
    g.edge('kernel', 'sleep')
    g.edge('kernel', 'runmem')
    g.edge('sleep', 'swap')
    g.edge('swap', 'runswap')
    g.edge('runswap', 'new')
    g.edge('runswap', 'runmem')
    g.edge('new', 'runmem')
    g.edge('kernel', 'sleep')
    g.edge('kernel', 'runmem')
    g.edge('sleep', 'swap')
    g.edge('swap', 'runswap')
    g.edge('runswap', 'new')
    g.edge('runswap', 'runmem')
    g.edge('new', 'runmem')
    g.edge('sleep', 'runmem')
    g.edge('sleep', 'runmem')
    g.view()

graficaG("")