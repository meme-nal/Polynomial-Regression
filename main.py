from src import preprocessing
from src import model # not implemented now
from src import evaluations

import yaml
with open("./config/config1.yml") as stream:
    try:
        options = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


data = preprocessing.get_dataset(options['dataset']['name'])
data = data.to_numpy()
# spliting
# scalling

poly_reg_model = model.PolynomialRegression(options['model'])

# training
# validation
# testing

# evaluation
# results

