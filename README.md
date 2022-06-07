First, all the required libraries were imported namely, NumPy, Pandas, TensorFlow and TensorFlow_hub were required to build the NLP model. 
Then we first imported the Google’s Universal Sentence Encoder (USE) which is used to convert the input text into higher dimensional vectors. USE module is imported from the link available online; https://tfhub.dev/google/universal-sentence-encoder/4 and is loaded using Tensorflow_hub into a variable ‘encoder’. 
Next, we defined an ‘embed’ function which takes the input and converts it into USE code. 
Then we imported the csv file “Precily_Text_Similarity.csv” which contains 2 columns of ‘text1’ānd ‘text2’. Now for all of the rows in the csv file we convert the pair of text1 and text2 into encoded message, temporarily stored in the ‘message_embeddings’ variables for each instance. 
Next, we converted the embedded message for each list of rows into a NumPy array using tf. make_tensor_proto and then we make a NumPy array ‘t’ for all these tensors. 
The approach we have taken to find out the similarity between two texts is by using ‘Cosine Similarity’. Cosine similarity finds the cosine value between two vectors using the following formula:

![image](https://user-images.githubusercontent.com/60060568/172063301-fd1da133-f488-460a-80a7-bc0dd422fd61.png)

Then we appended all the ‘cos_sim’ value to a list ‘sim_score’ and further created the dataframe column ‘Similarity_Score’. Now, we normalised the values of the Similarity_Score that was originally from [-1,1] to [0,1]. Then the ‘mycsvfile.csv’ is created with the values from the ‘Similarity_Score’ column.
Next, to implement the model to AWS, etc., we first build a model class with a ‘predict’ function and perform similar steps such that model. predict (text1, text2) returns us a similarity value from [0,1]. 
Then we created a pickle file for the model using the pickle library available. A pickle file is a binary representation of our model and is only computer readable.
 After the model is ready, we proceeded to the next step to create an application to deploy. We have used Flask to create the app in python.
First, import the required libraries, flask and request in our case. Next we created an application variable named ‘app’ and imported the .pkl file as model. 
Then we defined the route for home and the prediction webpage. For that we created an html file ‘index.html’ which specifies all the components used in this section. 
The predict route used the “POST” HTTP method as we need the user to enter the ‘text1’ and ‘text2’ data. Then we take the input and use the model.predict() to find the cosine similarity which is also displayed using index.html by ‘render_template’ feature.
At last, we specified the host and port for the deployment on the MS Azure cloud service. 
Then we move to the cloud service, Azure. First, we created a web app resource. Then provide the web app name, runtime stack (Python 3.8, in our case) and the region. Next, we added the files, model.py, index.html, app.py and a requirements.txt (which contains the versions of all the libraries used in the entire project to allow Azure to download them while deployment). Once everything’s done, we added the GitHub repository under the ‘Deployment Centre’. 
Once done, take the URL from the ‘Overview’ section and go to any web browser and paste it. The form will ask you for the text1 and text2 and on hitting the submit button provides you a similarity score between [0,1].
 

