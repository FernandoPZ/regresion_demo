import sklearn
from joblib import load

model = load("model.joblib")
while True:
    xs = []
    x = int(input("x:"))
    xs.append([x])
    prediction = self.model.predict(xs)
    print(prediction)
