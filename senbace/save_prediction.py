def save_prediction(data, output_data_path:str):
    """
    This task will save the prediction to an output file.

    If failed, this task will retry for n times and fail permenantly.

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    output_data_path : str
        DESCRIPTION.

    Returns
    -------
    None.

    """

    with open(output_data_path, 'w') as f:
      f.write(data)