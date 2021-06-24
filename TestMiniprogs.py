from FunctionCreator import functions
from FunctionCreator import preCompResults
from gplearn.genetic import SymbolicRegressor
import numpy as np
from ImageDecoderSmall import drawImage
from gplearn.fitness import make_fitness
import math

def makePrograms(funcSet):
    programs = []
    for func in funcSet:
        programs.append([func, 0, 1])
        programs.append([func, 0, 0])
        programs.append([func, 1, 1])
    return programs

def imgEvaluate(predicted, mappedProg):
    #convert to a number
    mapping = int("".join([str(p) for p in predicted]),4)
    mappings[mapping] = mappedProg

preCompResults(2)
programs = makePrograms(functions)

def diversityFunc(y, y_pred, sample_weight):
    newVal = int("".join([str(int(p)) for p in y_pred]),4)
    keys = mappings.keys()
    
    #first mapping, can't get it a score
    if len(keys) == 0:
        mappings[newVal] = True
        return 45.0
    
    dis = min([abs(newVal - x) for x in keys if newVal != x])
    dis = math.log(dis)
    dis *= max(1,math.log(len(keys)))
    #minIndex = a.index(min(a))
    
    if newVal in mappings.keys():
        mappings[newVal] += 1
        return dis / mappings[newVal]
    else:
        mappings[newVal] = 1
        print(len(mappings.keys()))
        return dis
    
    

fitFunc = make_fitness(function=diversityFunc, greater_is_better= True, wrap = False)

#run one generation as seems to be most convenient way of creating programs

est_gp = SymbolicRegressor(population_size=10000,tournament_size=2,
                           generations=300, init_depth=(2, 6), stopping_criteria=1000,
                           p_crossover=0.7, p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05, const_range=(1,2), p_point_mutation=0.1,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.01, random_state=0, function_set=functions,
                           metric = fitFunc)
imgData = np.array(np.meshgrid(range(0,4), range(0,4))).T.reshape(-1,2)



imgLbls = [0] * 16

est_gp.fit(imgData, imgLbls)

andFunc = functions[0]

#add constants
def addConsToProgs(funcSet, progs):
    outProgs = []
    for prog in progs:
        for func in funcSet:
            for i in range(1, 3):
                prog = [func] + prog + [andFunc, float(i), float(i)]
                outProgs.append(prog)
    return outProgs    

for i in range(0,len(programs)):
    est_gp._programs[0][i].program = programs[i]
    outGrid = est_gp._programs[0][i].execute(imgData)
    imgEvaluate(outGrid, programs[i])
    #drawImage(outGrid, "port" + str(i))
   
programs = addConsToProgs(functions, programs)

i2 = 0
for i in range(0,len(programs)):
    est_gp._programs[0][0].program = programs[i]
    outGrid = est_gp._programs[0][0].execute(imgData)
    imgEvaluate(outGrid, programs[i])
    
print(programs)