import numpy as np
import pandas as pd
import random
random.seed(1104)


def generate_x_y(random_seed=1104):
    random.seed(random_seed)
    randX = random.sample(range(1,9), 8)
    mapping_dict = {1:[0,0,0],
                 2:[0,0,1],
                 3:[0,1,0],
                 4:[0,1,1],
                 5:[1,0,0],
                 6:[1,0,1],
                 7:[1,1,0],
                 8:[1,1,1]}
    X = []
    for r in randX:
        X.append(mapping_dict[r])

    y = []
    randy = random.sample(range(1,9), 8)
    for el in randy:
        if el % 2 == 0:
            y.append([0])
        else:
            y.append([1])


    X = np.array(X)
    y = np.array(y)

    df = pd.DataFrame(data=np.concatenate([X, y], axis=1),
                      columns=['X1', 'X2', 'X3', 'y'])

    return df, X, y
