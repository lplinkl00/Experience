from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import vis
iris = datasets.load_iris()


X = [[d[1],d[2]] for d in iris.data]
names = [iris.target_names[1],iris.target_names[2]]
Y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.8)



scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


mlp = MLPClassifier(hidden_layer_sizes=(2), max_iter=1000)

mlp.fit(X_train, y_train)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

vis.vis2d(ax, mlp, X_train, y_train, X_test, y_test)