import numpy as np

def neural_net_pass(net, x, y):
    pred = net.forwardpass(x)
    loss = net.loss(pred, y)
    net.backpropogate(loss)
    return pred


def one_epoch(net, X, Y):
    '''
    Run one epoch an element at a time through the net.
    '''
    for index in range(X.shape[0]):
        x_batch = np.array(X[index], ndmin=2)
        y_batch = np.array(Y[index], ndmin=2)
        neural_net_pass(net, x_batch, y_batch)
        
    return net


def shuffle_data(X_train, Y_train):
    
    train_size = X_train.shape[0]
    indices = list(range(train_size))
    np.random.shuffle(indices)
    
    return X_train[indices], Y_train[indices]



def net_accuracy(net, X_test, Y_test, predict=True):
    P = net.forwardpass(X_test, predict)
    preds = [np.argmax(x) for x in P]
    actuals = [np.argmax(x) for x in Y_test]

    accuracy = sum(np.array(preds) == np.array(actuals)) * 1.0 / len(preds)
    print("Neural Net MNIST Classification Accuracy:", round(accuracy, 3) * 100, "percent")
    return accuracy