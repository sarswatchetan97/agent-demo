from sre_compile import dis
from turtle import speed


models = [
    {"name": "GPT-4", "accuracy": 0.95, "speed": 2.1, "cost": 0.06},
    {"name": "Claude", "accuracy": 0.93, "speed": 1.8, "cost": 0.04},
    {"name": "Gemini", "accuracy": 0.91, "speed": 2.5, "cost": 0.05},
    {"name": "LLaMA", "accuracy": 0.88, "speed": 3.2, "cost": 0.00},
    {"name": "BERT", "accuracy": 0.85, "speed": 0.5, "cost": 0.00},
]

# first_name = models[0]["name"]
# print(first_name)

#Best model
def find_best_model(models, metric):
    """Find the model with the highest value for a metric."""
    best = models[0]
    for model in models[1:]:
        if model[metric] > best[metric]:
            best = model
    return best

#calculate average
def find_average(models, metric):
    """Calculate average value of a metric"""
    total = sum(m[metric] for m in models)
    return total/len(models)

#filter models
def filter_models(models, metric, threshold):
    """Return models where metric exceeds threshold"""
    return (m for m in models if m[metric] >= threshold)


#Display report
def display_report(models):
    """Display a formatted report of all models."""
    print("=" * 50)
    print("🤖 AI Model Comparison Report")
    print("=" * 50)

    for model in models:
        status = "✅" if model["accuracy"] >= 0.9 else "⚠️"
        print(f"{status} {model['name']:10} | "
              f"Acc: {model['accuracy']:.0%} | "
              f"Speed: {model['speed']}s | "
              f"Cost: ${model['cost']}")

best = find_best_model(models, "accuracy")
avg = find_average(models, "accuracy")
print(f"Best model: {best['name']} ({best['accuracy']:.0%})") #The :.0% format specifier converts a decimal to a percentage with 0 decimal places. 0.95 × 100 = 95%.
print(f"Average accuracy: {avg:.0%}") 

display_report(models)
fast_models = filter_models(models, "speed", 0)

free_models = [m for m in models if m["cost"] == 0]
print(f"Free models: {len(free_models)}")

# Which free model is best?
if free_models:
    best_free = find_best_model(free_models, "accuracy")
    print(f"Best Free model: {best_free["name"]}")