import numpy

def mse(predictions:numpy.ndarray, y:numpy.ndarray)->float:
    return ((predictions-y)**2).mean()

def rmse(predictions:numpy.ndarray, y:numpy.ndarray)->float:
    return numpy.sqrt(((predictions-y)**2).mean())

def get_eval(predictions:numpy.ndarray, y:numpy.ndarray, type:str):
    match type:
        case "mse":
            return mse(predictions, y)
        case "rmse":
            return rmse(predictions, y)
        
        case _:
            raise(NotImplementedError)