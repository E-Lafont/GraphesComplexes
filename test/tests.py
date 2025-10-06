import GraphesComplexes as gc
import numpy as np

gph = gc.Graphe(1, 2)
id = gc.Fonction(lambda z:z)

gph.trace(id, 0, 0)
gph.trace(id, 1, 0, res=50)
gph.affiche()