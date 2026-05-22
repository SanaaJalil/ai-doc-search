from services.embeddings import store_embeddings
from services.qa import answer_question

# Step 1 - Store some test text
print("Storing embeddings...")
store_embeddings("test.pdf", "Ansible is an open source automation tool used for configuration management and deployment.")
print("Embeddings stored!")

# Step 2 - Ask question
print("Asking question...")
answer = answer_question("What is Ansible?")
print("Answer:", answer)