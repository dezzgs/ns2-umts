from Run import *

gamma   = 0.99
noSteps = 10**4
noRuns  = 1000
exp     = "egreedy1divn^0.5"
lrs     = [ "1divn^0.8", "1divn" ]

widths = [ 22 ]
for lr in lrs:
    for width in widths:
        World   = Grid( 3, 3, width )
        runExperiment(World, gamma, noSteps, noRuns, exp, lr)

