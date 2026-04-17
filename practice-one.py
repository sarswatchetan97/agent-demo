import enum
import json
from tkinter import scrolledtext


scores = [80.5, 90.0, 88.6, 75.9]

for score in scores:
    if score == 90.0:
        print(f"Outstanding, your mark is {score}")
    else:
        print("You need improvement")

#slicing
print(scores[:2])
print(scores[1:2])
print(scores[1:])

scores.append(74)
scores.insert(1, 85.6)
print(scores)
scores.sort()
print(f"Sorted - {scores}")
scores.reverse()
print(f"Reversed list - {scores}")

#enumerate - keeps track of index
for i, score in enumerate(scores):
    print(f"{i} - {score}")

models = ["Llama", "Siri"]
predictions = [99.6, 99.9]


for model in models:
    for prediction in predictions:
        print(f"{model} - {prediction}")

for i in range(5):
    print(f"{i} square is {i*i}")

print(f"Length - {len(scores)}")
print(f"Max - max(scores)")
print(f"Min - min(scores)")
print(f"Sum - sum(scores)")

total=0
for i in range(5):
    total+=i
print(total)

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(20)]
print(squares)

high_scores = [s for s in scores if s>80.0]
print(high_scores)

last = scores.pop()
print(f"last element {last}")

ai_models = ["GPT", "BERT", "LLaMA", "Claude"]
print("GPT" in ai_models)

#basic logic of checking spam email
spam_words = ["free", "winner", "click now"]
email_subject = "You are a winner!"

for word in spam_words:
    if word in email_subject.lower():
        print(f"Spam detected! Found: {word}")
        break

ranked = sorted(scores, reverse=True)
print(f"Ranked - {ranked}")

#Dictionary
model_scores = {"GPT": 0.95, "BERT": 0.88, "LLaMA": 0.91}

for model in model_scores:
    print(model)

for model_score in model_scores.values():
    print(model_score) 

for model, model_score in model_scores.items():
    print(f"{model} - {model_score}")

#Nested Dictionary
ai_models = {
    "gpt4": {
        "company":"OpenAI",
        "params": "1.7T",
        "type": "LLM"
    },
    "claude": {
        "company": "Anthropic",
        "params": "Unknown",
        "type": "LLM"
    }
}

print(ai_models["gpt4"]["params"])
print(ai_models["claude"]["type"])

squares = {x: x**2 for x in range(5)}
print(squares)

squares = {}
for x in range(5):
    squares[x] = x**2
print(squares)

cubes = {x: x**3 for x in range(10)}
print(cubes)

names = ["cat", "dog", "bird"]
scores = [0.95, 0.88, 0.72]

predictions = {name: score for name, score in zip(names, scores)}
print(predictions)

#JSON

# Dictionary → JSON string
data = {"model": "GPT-4", "accuracy": 0.95}
json_string = json.dumps(data)
print(json_string)

#JSON string → Dictionary
result = json.loads(json_string)
print(result)
