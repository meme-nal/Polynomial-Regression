import numpy
import pandas
import seaborn

wine_quality = pandas.read_csv("./data/raw/winequality-red.csv")

corr_matrix = wine_quality.corr(method='pearson')
seaborn.heatmap(corr_matrix, annot=False)

wine_quality = wine_quality.drop(columns='free sulfur dioxide')

def get_dataset(name:str)->pandas.DataFrame:
    match name:
        case "wine_quality":
            return wine_quality
        
        case _:
            raise(NameError)

def split(dataset:pandas.DataFrame):
    # It needs to split our data into subdatasets for training, validations and testing
    pass

def normalize(dataset:numpy.ndarray)->numpy.ndarray:
    # normalization of our data
    pass

def standardize(dataset:numpy.ndarray, mean:float, std:float)->numpy.ndarray:
    # move our data to standard normal distribution
    pass

def scalling(dataset:numpy.ndarray, type:str, mean=None, std=None):
    if type == "normalization":
        return normalize(dataset)
    elif type == "standardization":
        return standardize(dataset, mean, std)
    else:
        raise(TypeError)