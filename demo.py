from sklearn import tree
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
from sklearn.metrics import accuracy_score

#[height, weight, show size]
X = [[181, 80, 44],[177, 70, 43],[160, 60, 38],[154, 54, 37],
[166, 65, 40],[190, 90, 47],[175,64,39],[177, 70, 40],
[159, 55, 37],[171, 75, 42],[181, 85, 43]]

#[gender]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female'
,'female','female', 'male', 'male']

models = {"Decision Tree" : tree.DecisionTreeClassifier(), "Support Vector Machine" : svm.SVC(),
"Naive Bayes" : GaussianNB(), "K-Nearest Neighbors" : neighbors.KNeighborsClassifier()}

for name in models:
  models[name].fit(X,Y)

results = {}
for name in models:
  results[name] = accuracy_score(Y,models[name].predict(X))

highest = 0.0
modelName = ""
for name in results:
  if results[name] > highest:
    modelName = name
    highest = results[name]

print(modelName, "gave the highest score which is", highest)