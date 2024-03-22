import numpy

def mse(predictions:numpy.ndarray, y:numpy.ndarray)->float:
    return ((predictions-y)**2).mean()

def mse_l2(predictions:numpy.ndarray, y:numpy.ndarray, weights:numpy.ndarray, lambda2:float)->float:
    return ((predictions-y)**2).mean() + lambda2 * (weights**2).sum()

def mse_elasticnet(predictions:numpy.ndarray, y:numpy.ndarray, weights:numpy.ndarray, lambda1:float, lambda2:float)->float:
    return ((predictions-y)**2).mean() + lambda1 * numpy.abs(weights).sum() + lambda2 * (weights**2).sum()

def get_loss(predictions:numpy.ndarray, y:numpy.ndarray, type:str, weights=None, lambda1=None, lambda2=None):
    match type:
        case "mse":
            return mse(predictions, y)
        case "mse_l2":
            return mse_l2(predictions, y, weights, lambda2)
        case "mse_elasticnet":
            return mse_elasticnet(predictions, y, weights, lambda1, lambda2)
        
        case _:
            raise(NotImplementedError)