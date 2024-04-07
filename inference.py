import openai

client = openai.OpenAI(api_key="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")

system_prompt = "You are an ecommerce assistant with the purpose of taking customers questions and providing them with relevant response. Customers can report incidents, request services, seek guidance, or seek assistance."

# Create a function for chatbot reponse
fine_tuned_model_id = "ft:gpt-3.5-turbo-0125:bizlink-international-corp::9AuzhrV9"

def chatbotResponse(user_question):
    completion = client.chat.completions.create(
        model=fine_tuned_model_id,
        messages=[{"role": "system", "content": system_prompt}, 
                {"role": "user", "content": user_question}, ]
    )
    return completion.choices[0].message.content


while True:

    user_question = input("user: ")
    if user_question in ['quit', 'exit', 'bye']:
        print(f"chatbot: {chatbotResponse(user_question)}")
        break
    else:
        print(f"chatbot: {chatbotResponse(user_question)}")

