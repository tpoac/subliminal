# -*- coding: utf-8 -*-
# Some settings to show a JS animation
import matplotlib.pyplot as plt
import seagull as sg
import seagull.lifeforms as lf

# Initialize board
plt.rcParams["animation.html"] = "jshtml"
board = sg.Board(size=(40,40))

# Add three Pulsar lifeforms in various locations
board.add(lf.Pulsar(), loc=(1,1))
board.add(lf.Pulsar(), loc=(1,22))
board.add(lf.Pulsar(), loc=(20,1))
board.add(lf.Pulsar(), loc=(20,22))
board.view()

# Simulate board
sim = sg.Simulator(board)
sim.run(sg.rules.conway_classic, iters=100)

#%%capture
anim = sim.animate()
anim.save('animation.gif', writer='imagemagick', fps=60)
