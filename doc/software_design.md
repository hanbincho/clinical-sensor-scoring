The following users have been identified as potential users for the **Clinical Sensor Scoring** tool. The user stories, use cases and component design for each of these users are also described in the text below. 

## User 1: Clinician
### User story
A user of this tool would be a clinican. They would be able to obtain clinically relevant scores to assess patient motor behaviors. They would use this tool as a more consistent and efficient means to assess motor behavior symptoms. They are familiar with context behind score values and can confirm whether or not it aligns with what they would have expected
### Use case(s)
#### Obtain score
* User can open a file explorer interface to navigate to and select a .csv file of choice
* Interface provides list of possible machine learning models to provide score
* User selects model(s) of choice
* [if no error] Interface outputs score(s) for loaded data
* [if error encountered] Interface outputs error message
#### Experience survey
* User can leave feedback about the performance of model(s) or interface
* Feedback can be stored and reviewed to guide future updates
### Component design
#### Obtain score
* Loading functionality for raw data
* Signal processing functionality of loaded data
* Database with machine learning model(s)
* Interface that takes processed data and uses model of choice to output score

## User 2: Database administrator
### User story
Another user would be a database administrator. They would want to format the data and make sure it has all the necessary components for future training or evaluation. They would want to be able to run tests on the data to make sure that it is in the proper format for interpretation. They would be familiar with what the data means and what types of data should be used with this tool.
### Use case(s)
#### Verify data format
* **User**: Uploads a `.csv`, `.txt`, `.dat` or `.xlsx` file containing recorded data from sensors.
* **Algorithm**: Checks if the data in uploaded file is compatible for use with the Clinical Scoring Software. 
* **Interface**:
	* _If file is well formatted_: Notifies user and confirms that the uploaded file is properly formatted for use with software.
	* _Otherwise_: Outputs error message and notifies user that uploaded file needs to be formatted.
#### Database Management Systems(DBMS)
* A database access language is required for interacting with a database from creating database to simply inserting data.
* A proper DBMS must support several query languages, which are Structured query language (SQL) and MOngoDB Query Language (MQL), to interact with the database.
* [if no error] DBMS can monitor the performance of databases using integrated tools and enable users to tune databases by creating optimized indexes.
* [if error] DBMS provides a recovery platform with the necessary tools to fully or partially restore databases to their previous state.
### Component design
* Monitoring cloud storage and database security issues
* backup the storage if there is any issues or errors
* conversant with SQL and relevant database technologies

## User 3: UX Designer
### User story
Another user would be a UX designer. They would be able to provide updates to the user inter feedback. They would be able to update documentation that guides the use of the interface and have access to the UI framework. They would be familiar with user experience research and have good user design practices to ensure comfortable use for all possible users.
### Use case(s)
### Component design

## User 4: Researchers
### User story
Another user would be a researcher. They would be able to obtain clinically relevant scores for assessing patient motor behaviors, but with some more customization by selecting their machine learning model(s) of choice. They would use this tool to assess patient's motor symptoms, but also build on current models by performing additional training with model(s) of interest. They would be able familiar with the context of the data, understand if a score is reflective of the patient's motor behavior, and have a broad understanding of machine learning and neural networks.
### Use case(s)
### Verify data format
Simialar to the `Verify data format` use case described for the `Database administrator` above.
#### Import/export machine learning model
* User can choose to open a file explorer to load in a file with a custom machine learning model'sparameters
* Interface now provides this newly imported model prior to scoring
* After training a model, users can export the current model for future use
### Component design

## User 5: ML Scientist
### User story
Another user would be a machine learning scientist. They would want to be able to choose or import machine learning model of choice. Be able to incorporate feedback to retrain the model based off of clinican input. They would also want to be able to export the model for future use. They would also want to have access to performance metrics of the models that have been trained to decide on which model to move forward with. Data analysts would be very familiar with Python machine learning packages and neural networks, understanding of the dataset, and good software design practices.
### Use case(s)
### Component design
