# Import needed packages
from alexnet_model import AlexNet

def create_model(model_name):
    """


    Parameters
    ----------
    model_name : TYPE
        DESCRIPTION.

    Returns
    -------
    model : TYPE
        DESCRIPTION.

    """
    if model_name == "AlexNet":
        # create model
        model = AlexNet(num_classes=7) # since score can range from 0-7
        model.to(curr_device) # move the model to GPU
    return model