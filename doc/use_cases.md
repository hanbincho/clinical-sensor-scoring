# Use Cases

## Obtain score
* User can open a file explorer interface to navigate to and select a .csv file of choice
* Interface provides list of possible machine learning models to provide score
* User selects model(s) of choice
* [if no error] Interface outputs score(s) for loaded data
* [if error encountered] Interface outputs error message

## Import/export machine learning model
* User can choose to open a file explorer to load in a file with a custom machine learning model'sparameters
* Interface now provides this newly imported model prior to scoring
* After training a model, users can export the current model for future use

## Data quality check
* User can select a .csv file to load 
* User can choose to run a test to check format and components of .csv file
* [if no error] Interface notifies user and confirms that the .csv file is properly formatted
* [if error] Interface outputs error message and notifies user that .csv file needs to be formatted
