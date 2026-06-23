from config import model

response = model.generate_content(
    "Say Hello"
)

print(response.text)