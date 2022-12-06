def create_model(model_name):
  if model_name == "AlexNet":
    # create model 
    model = AlexNet(num_classes=7) # since score can range from 0-7
    model.to(curr_device) # move the model to GPU
    return model