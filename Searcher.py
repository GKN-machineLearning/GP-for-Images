from gplearn.genetic import SymbolicRegressor
from FunctionCreator import makeFunctions
from ImageDecoder import decodeImage

opResults = {}


func_set = makeFunctions()

IMAGE_SIZE = 8 #2^8 pixels by 2^8 pixels = 256 by 256
COLOUR_DEPTH = 4 #4 bits per tree
TREE_NUM = 3 # one for red, one for blue, one for green 




#make data

#get data
imgData, lbls = decodeImage("Portrait.png")

#TODO - params copied exactly from https://gplearn.readthedocs.io/en/stable/examples.html#example

est_gp = SymbolicRegressor(population_size=100,tournament_size=2,
                           generations=20, init_depth=(2, 6), stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05, p_point_mutation=0.1,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.01, random_state=0, function_set=func_set)


    
est_gp.fit(imgData, lbls)

print(est_gp._program)
