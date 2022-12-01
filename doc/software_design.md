
The following user groups have been identified as potential users for the `**Clinical Sensor Scoring**` tool. The user stories, use cases and component design for each of these users are also described in the text below. 

> ## User 1: Clinician
>> ### User story
>> A user of this tool would be a clinican. They would be able to obtain clinically relevant scores to assess patient motor behaviors. They would use this tool as a more consistent and efficient means to assess motor behavior symptoms. They are familiar with context behind score values and can confirm whether or not it aligns with what they would have expected
>
>> ### Use case(s)
>> #### Obtain score
>> * User can open a file explorer interface to navigate to and select a .csv file of choice
>> * Interface provides list of possible machine learning models to provide score
>> * User selects model(s) of choice
>> * [if no error] Interface outputs score(s) for loaded data
>> * [if error encountered] Interface outputs error message
>>
>> #### Experience feedback
>> * User can leave feedback about the performance of model(s) or interface
>> * Feedback can be stored and reviewed to guide future updates
>
>> ### Component design
>> #### `Obtain score`
>> * Loading functionality for raw data
>> * Selection of specific muscle/regions of upper extremities
>> * Conerting functionality to take loaded data and create images to be fed into the model
>> * Database with pretrained machine learning model(s) 
>> * 
>> * Interface that takes processed data and uses model of choice to output score
>> #### `Experience feedback`
>> * Interface that allows user to enter expected score if predicted score is significantly off from user's expectations
>> * Interface that allows user to enter text for qualitative feedback on model performance
>> * Interface that allows select users to access feedback and provide updates from collected feedback


> ## User 2: Database administrator
>> ### User story
>> Another user would be a database administrator. They would want to format the data and make sure it has all the necessary components for future training or evaluation. They would want to be able to run tests on the data to make sure that it is in the proper format for interpretation. They would be familiar with what the data means and what types of data should be used with this tool.
>
>> ### Use case(s)
>> #### Verify data format
>> * **User**: Uploads a `.csv`, `.txt`, `.dat` or `.xlsx` file containing recorded data from sensors.
>> * **Algorithm**: Checks if the data in uploaded file is compatible for use with the Clinical Scoring Software. 
>> * **Interface**:
>>    - _If file is well formatted_: Notifies user and confirms that the uploaded file is properly formatted for use with software.
>>    - _Otherwise_: Outputs error message and notifies user that uploaded file needs to be formatted.
>>
>> #### Database Management Systems(DBMS)
>>* A database access language is required for interacting with a database from creating database to simply inserting data.
>>* A proper DBMS must support several query languages, which are Structured query language (SQL) and MOngoDB Query Language (MQL), to interact with the database.
>>* [if no error] DBMS can monitor the performance of databases using integrated tools and enable users to tune databases by creating optimized indexes.
>>* [if error] DBMS provides a recovery platform with the necessary tools to fully or partially restore databases to their previous state.
>
>> ### Component design
>> * Monitoring cloud storage and database security issues
>> * backup the storage if there is any issues or errors
>> * conversant with SQL and relevant database technologies


> ## User 3: UX Designer
>> 
>> ### User story
>> Another user would be a UX designer. They would be able to provide updates to the user inter feedback. They would be able to update documentation that guides the use of the interface and have access to the UI framework. They would be familiar with user experience research and have good user design practices to ensure comfortable use for all possible users.
>
>> ### Use case(s)
> #### Configure UI Framework
>> * **User**: Modifies and edits the user interface based on feedback with toolkits (wxPyhton, Ttinker, PyQT)
>> * **Interface**: Updates interface elements including input control and navigation components
>> * [if no error] Interface prompts a message informing UI that has been updated and stores changes in changelog
>
>> ### Component design
>> * Toolkit that manages and edits UI directly
>> * Changelog that saves any modifications

> ## User 4: Researchers
>> ### User story
>> Another user would be a researcher. They would be able to obtain clinically relevant scores for assessing patient motor behaviors, but with some more customization by selecting their machine learning model(s) of choice. They would use this tool to assess patient's motor symptoms, but also build on current models by performing additional training with model(s) of interest. They would be able familiar with the context of the data, understand if a score is reflective of the patient's motor behavior, and have a broad understanding of machine learning and neural networks.
> 
>> ### Use case(s)
>> #### Verify data format
>> Similar to the `Verify data format` use case described above for a `Database administrator`.
>>
>>  #### Obtain score
>> Similar to the `Obtain Score` use case as described above for a `Clinician`.
>>
>> #### Import/export machine learning model
>> * **User**: Uploads preferred/customized machine learning model for training data.
>> * **Interface**: Uses user-provided model to train data and provide scoring. Also saves model and results.
>> * **User**: Exports the completed trained model for future use.
>>
>> #### Hyperparameter tuning
>> * **User**: Provides an array of hyperparameters for tuning the ML algorithm.
>> * **Algorithm**: Trains data using each value of hyperparamter in the supplied array and records performance.
>> * **Interface**: Shows user a summary of obtained results using each parameter.
>> * **User**: Based on results shown, user can infer the best performing hyperparameters for future training.
>>
>> #### Serve trained models
>> * **Interface**: Shows model performance of pre-loaded ML algorithms in comparison to the user-defined algorithm.
>> * **User**: If performance of user-defined algorithm is better, user exports model and serves to `ML scientist` for review and possible deployment in the main software to facilitate access by other users.
>
>> ### Component design
>> #### Components for `Import/export machine learning model` use case
>> * Storage for imported machine learnong models and their outputs.
>> * User interface to present summary data of the performance of user-defined models. 
>>
>> #### Components for `Hypaparemeter tuning` use case
>> * Database with values of hyperparameters
>> * Storage for model performance during hyperparameter tuning.
>> * User interface to describe model performance using each hyperparameter.
>>
>> #### Components for `Serve trained models` use case.
>> * Pipeline for transmiting model results to `ML Scientist`.


> ## User 5: ML Scientist
>> ### User story
>> Another user would be a machine learning scientist. They would want to be able to choose or import machine learning model of choice. Be able to incorporate feedback to retrain the model based off of clinican input. They would also want to be able to export the model for future use. They would also want to have access to performance metrics of the models that have been trained to decide on which model to move forward with. Data analysts would be very familiar with Python machine learning packages and neural networks, understanding of the dataset, and good software design practices.
>
>> ### Use case(s)
>> Provide a list of ML models to choose from as the best outcome.
>> Using the inerface obtain the model score
>> Provide feedback if score predicted has error
>> Provide some explainability of the model performance/ falling short.

>> ### Component design
 >> * Investigate existing solutions for the Fine-grain Image classification problem.
 >> * Try out existing solutions (POCs) by running open-source codebases, if any.
 >> * Evaluate existing solutions on open-source datasets.
 >> * Define train test datsets and clinical scores - essential 
 >> * Train and evaluate a model that can predict a clinical score. 
 >> * Incorporate a feedback loop to capture any discrepencies in the predicted score. 
 >> * Investigation/ Insights summary on why the model is (not) working well or how it can be improved. 
 >> * Summary of model results – what kind of false positives/negatives does it have? In which cases it fails?
 >> * Retrain the model for robust results. 
 >> * Capture the evaluation metrics in the newer models. Tweak model hyper parameters and make it a robust model.
 >> * Potentially identity the top performing model from the exploratory study
>> * Integrate with the webpage deploying the  ML model for clinical sensor scoring. This would be an interactive webpage/html page where a user can upload a csv file and the page will show the clinical sensor score from the model. 
>> * Potential results produced by the newer model
>> * Explainability around model performances. 


| Scenario                      | Expected Output                          |
|-------------------------------|------------------------------------------|
| File has stroke values        | Relevant score related to stroke values  |
| File has no stroke values     | Score outside the stroke threshold       |
| File has healthy values       | Score associated with healthy values     |


