
The following user groups have been identified as potential users for the `**Clinical Sensor Scoring**` tool. The user stories, use cases and component design for each of these users are also described in the text below. 

> ## User 1: Clinician
>> ### User story
>> A user of this tool would be a clinican. They would be able to obtain clinically relevant scores to assess patient motor behaviors. They would use this tool as a more consistent and efficient means to assess motor behavior symptoms. They are familiar with context behind score values and can confirm whether or not it aligns with what they would have expected
>
>> ### Use case(s)
>> #### Obtain score
>> * **User**: can convert a .csv file with sensor data into images.
>> * **User**: can use a pre-trained model for clinical score prediction.
>> * **Algorithm**: goes through uploaded images and assigns clinical scores.
>> * **Interface**: outputs scores for loaded data and user can download.
>> * **Interface**: outputs error message pointing to issue.
>>
>> #### Experience feedback
>> * User can leave feedback about the performance of model(s) or interface.
>> * Feedback can be stored and reviewed to guide future updates.
>
>> ### Component design
>> #### `Obtain score`
>> * Loading functionality for raw data contained in .csv file.
>> * Converting functionality to take loaded data and create images to be fed into the model.
>> * Access to pretrained machine learning model(s)  .
>> * Interface that takes processed data and uses model of choice to output score.
>> #### `Experience feedback`
>> * Interface that allows user to enter text for qualitative feedback on model performance.


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
>> #### `Verify data format`
>> * Functionality to check the structure of uploaded data, such as valid data types
>> * Functionality to identify specific errors if uploaded data is unproperly formatted
>> #### Database Management Systems (DBMS)
>> * Functionality to update data (i.e. models) accessible on database
>> * Monitoring cloud storage and database security issues
>> * Backup the storage if there is any issues or errors
>> * Conversant with SQL and relevant database technologies


> ## User 3: UX Designer
>> 
>> ### User story
>> Another user would be a UX designer. They would be able to provide updates to the user inter feedback. They would be able to update documentation that guides the use of the interface and have access to the UI framework. They would be familiar with user experience research and have good user design practices to ensure comfortable use for all possible users.
>
>> ### Use case(s)
>> #### Configure UI Framework
>> * **User**: modifies the user interface based on feedback with toolkits (wxPyhton, Ttinker, PyQT)
>> * **Interface**: updates interface elements including input control and navigation components
>> * **Interface**: prompts a message informing UI that has been updated and stores changes in changelog
>
>> ### Component design
>> #### `Update UI`
>> * Toolkit that manages and edits UI directly
>> * Changelog that keep a history of modifications

> ## User 4: Researcher
>> ### User story
>> Another user would be a researcher. They would be able to obtain clinically relevant scores for assessing patient motor behaviors, but have some more customization by selecting their machine learning model(s) of choice and modifying hyperparameters for model training. They would use this tool to assess patient's motor symptoms, but also build on current models by performing additional training with model(s) of interest and looking at performance metrics of the model. They would be familiar with the context of the data, understand if a score is reflective of the patient's motor behavior, and have a broad understanding of machine learning and neural networks.
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
>> * Functionality to import custom machine learning models.
>> * User interface to summarize outputs such as images/plots of performance of used models and time-series data. 
>>
>> #### Components for `Hyperparemeter tuning` use case
>> * Take in particular hyperparameter values from user.
>> * Specific hyperparameter values are used for model training and prediction.
>> * User interface to describe model performance after specific set of hyperparameters..
>>
>> #### Components for `Serve trained models` use case.
>> * Pipeline for transmiting model results to `ML Scientist`.


