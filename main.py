from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from joblib import dump

iris = load_iris()
x,y = iris.data,iris.target
model = RandomForestClassifier()
model.fit(x,y)

# Save the model to a file
dump(model,'model.joblib')
