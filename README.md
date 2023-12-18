This sample repository contains the procedure and the code files for generating vector embeddings using VertexAI Palm2 API on data in a MongoDB collection (movies), setting up Atlas Search index on the vectorized data, and performing the vectorSearch queries using a Python script.

#The code
triggerfunction.js - JavaScript function that generates plot embeddings using OpenAI API and updates documents in a MongoDB collection with the embeddings.
vectorIndex.json - JSON definition for setting up an Atlas Search index with the necessary configuration for the plot_embedding field.
searchVertexAI.py - Python script to run queries against the MongoDB Atlas vector search index and data.
settings.py : MongoDb Atlas cluster definitions and other settings needed by your python code. 

#Pre-requisites
Before running the code in this repository, make sure you have the following prerequisites:

* MongoDB Atlas Cluster - Set up a MongoDB Atlas cluster where the sample_mflix database and movies collection exist. Replace the placeholders in the code with your actual database and collection names.

* GCP account - Make sure you have an account with some free credits on Google Cloud Platform (GCP).

* Enable the VertexAi API in GCP. See screen shot.

* Install the gcloud CLI : 

* Install python3 using


---
## Execution steps

__1. Configure the MongoDB Atlas Environment__
* Log-on to your [Atlas account](http://cloud.mongodb.com) If you do not have a MongoDB Atlas cluster, you can create an account for free.
* In the project's Security tab, choose to add a new user, e.g. __main_user__, and for __User Privileges__ specify __Read and write to any database__ (make a note of the password you specify)
* In the Security tab, add a new __IP Whitelist__ and allow access from everywhere.
* Create an __M10__ or a free M0 cluster based 3 node replica-set in a single cloud provider region of your choice.
* In the Atlas console, for the database cluster you deployed, click the __Connect button__, select __Connect Your Application__, and for the __latest Node.js version__ copy the __Connection String Only__ - make a note of this MongoDB URL address to be used in the next step
* Edit the settings.py file , change the URL_STRING with the value noted above.Do not change the value of data base and collection.

__2. Load sample data on MongoDB Atlas__

<table><tr><td><img src='/images/load.png' alt=“” height="150" width="fit"></td></tr></table>

__3. How to auhthenticate to your VertexAI API__
* Once you have configured the gcloud CLI run the following command to login using Application Default Credentiels from the machine where you are going to run the code:
```
gcloud auth application-default login
```
A webpage will open and you will be asked to login to your account. Login using the email you use on your GCP account as shown:

<table><tr><td><img src='/images/gcloudlogin.png' alt=“” height="350" width="fit"></td></tr></table>
Your application can now login and use your GCP resources which you have access to and have been enabled.

__4. Generate embeddings__
Run the createEmbeddings.py to generate vector embeddings on the "plot" field on your "movies" collection in the sample_mflix data base.
You will see a new field "plot_embedding" in your documents.
This step will take some time to run when you run it the first time on all documents.

__5. Create Vector Index__
* Copy the index definition from the vectorIndex.json file. Go to your "movies" collectiona nd click on the "SearchIndex" tab.
* Create a new search index using the JSON editor by pasting the contents of vectorIndex.json.
Once the index is finished you are ready to execute your Vector Search queries.

__6. Run vector searches__
Run the vectorSearchVertexAI.py. You will be asked to enter a text string to search, the text string is then passed to VertexAI using the Palm2 API to generate vector embedding and then the vectorised query is passed to the $vectorSearch to compare with the embeddings in your collection.

Note: For detailed information and troubleshooting, refer to the official GCP and MongoDB documentations.
