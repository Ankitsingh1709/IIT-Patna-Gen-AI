import ollama

client = ollama.Client()

#define the model name and the prompt
model_name = "deepseek-r1:latest"  # replace with your model name
prompt = "What is the capital of France?"

#generate a response from the model
response = client.generate(model=model_name, prompt=prompt) 

#print the response
print(response.response)  # should print "The capital of France is Paris."