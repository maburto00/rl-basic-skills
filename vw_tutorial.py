from vowpalwabbit import pyvw

model = pyvw.vw(quiet=False)
train_examples = [
  "0 | price:.23 sqft:.25 age:.05 2006",
  "1 | price:.18 sqft:.15 age:.35 1976",
  "0 | price:.53 sqft:.32 age:.87 1924",
]

for example in train_examples:
    model.learn(example)

test_example = "| price:.46 sqft:.4 age:.10 1924"

prediction = model.predict(test_example)
print(prediction)