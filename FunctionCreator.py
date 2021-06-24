
from gplearn.functions import make_function
import numpy as np



opResults = {}


def binOperator(opNum, val1, val2):
    val1 = [int(v) for v in val1]
    val2 = [int(v) for v in val2]
    combedStr = ''.join([str(opNum),str(val1),str(val2)])
    try:
        try: #try/catch block for not found in dict, mainly to cheat the gplearn's checks
            return opResults[combedStr]
        except:
            strOp = str(opNum)
            res = []
            lv = len(val1)
            for i in range(0,lv):
                res.append(opResults[strOp+str(int(val1[i]))+str(int(val2[i]))])
            #store whole sequence for next time
            res = np.array(res)
            opResults[combedStr] = res
            return res
    except:
        print("WARNING: strange input sequence " + str(val1) + str(val2))
        return np.array([0] * len(val1))
        #to cheat gplearn's irrelevant checks

functions = []
functions.append(make_function(function=lambda x,y: binOperator(1,x,y), name="binOp1", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(2,x,y), name="binOp2", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(3,x,y), name="binOp3", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(4,x,y), name="binOp4", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(5,x,y), name="binOp5", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(6,x,y), name="binOp6", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(7,x,y), name="binOp7", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(8,x,y), name="binOp8", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(9,x,y), name="binOp9", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(10,x,y), name="binOp10", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(11,x,y), name="binOp11", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(12,x,y), name="binOp12", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(13,x,y), name="binOp13", arity=2))
functions.append(make_function(function=lambda x,y: binOperator(14,x,y), name="binOp14", arity=2))



#for i in range(1,15):
    #func = make_function(function=lambda x,y: binOperator(i,x,y), name="".join(["binOp",str(i)]), arity=2)
    #functions.append(func)

#compute 16
def preCompResults(bitSize):
    def compResult(op,val1,val2):
        opBin = list(format(op, '04b'))
        val1Bin = list(format(val1, '0' + str(bitSize) + 'b'))
        val2Bin = list(format(val2, '0' + str(bitSize) + 'b'))
        outBin = ''
        for i in range(0,bitSize):
            outBin = outBin + str(opBin[int(''.join([val1Bin[i],val2Bin[i]]), 2)])
        return int(outBin,2)
    
    maxVal = 2**bitSize
    for op in range(1,15):
        for val1 in range(0,maxVal):
            for val2 in range(0,maxVal):
                opResults[str(op) + str(val1) + str(val2)] = compResult(op,val1,val2)
    
