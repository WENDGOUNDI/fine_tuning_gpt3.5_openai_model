# Fine-Tuning OpenAI's GPT-3.5 Turbo Model for Clothes Shop Chatbot
In this project, we will explore how to leverage the full capabilities of GPT-3.5 turbo model, by improving its performance for specialized tasks through fine-tuning. We will create a custom gpt model that can be used for building a chatbot to provide assistance to a clothing store customers. The goal of implementating such solution is to improve customers experience by providing them with fast and accuracte assistance.

# DATASET
The dataset used for fine tuning the chatgpt-3.5-turbo model has been downloaded from kaggle. The main purpose of this dataset is to train a chatbot to provide fast assistance to a clothing store customers. The dataset is large of 1185 rows, with three columns: **Contex, Question and Answer**. We will only use two columns **Question** and **Answer** to train our custom chatgpt model. The dataset in the csv format will be later preprocess to meet OpenAI training data format.

# STEPS:
1. Load and Read the csv file data.
2. Perform EDA on the data to remove duplicates, NAN values or any unwanted value if exist.
3. Prepare the dataset to meet OpenAI fine tuning data format. Each example in the dataset should be a conversation in the same format as OpenAI ChatCompletions API function.
   - conversation example:  **{'messages': [{'role': 'system', 'content': 'You are an ecommerce assistant with the purpose of taking customers questions and providing them with relevant response. Customers can report incidents, request services, seek guidance, or seek assistance. You only respond to ecommerce related questions. Do not respond to questions not related to ecommerce.'}, {'role': 'user', 'content': 'How long do I have to cancel my order?'}, {'role': 'assistant', 'content': 'Orders can be canceled within 8 hours. Follow steps on our website under "Order History" for a cancellation.'}]}**
4. Upload the data into OpenAI platform and launch the training. In the notebook, there are some functions allowing to check the training status but once the training is completed, OpenAI will send a notification email. The model has been trained with default values.
5. Test your custom model. If needed, add more data and retrain.


# INFERENCE
 - Conversation 1
![inference2](https://github.com/WENDGOUNDI/fine_tuning_gpt3.5_openai_model/assets/48753146/3ddcb310-afde-4f35-a205-c522c2c8f137)

 - Conversation 2
![inference](https://github.com/WENDGOUNDI/fine_tuning_gpt3.5_openai_model/assets/48753146/39833fc3-f314-4180-9887-9ecc560d49e7)

# REFERENCE
https://www.kaggle.com/datasets/quangnguyen711/clothes-shop-chatbot-dataset

https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset

