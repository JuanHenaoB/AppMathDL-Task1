import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    se = 0
    for i in range(len(pred)):
        se = se + (tar[i] - pred[i])**2
    mse = se/len(predictions)
    rmse = np.sqrt(mse)
    return rmse