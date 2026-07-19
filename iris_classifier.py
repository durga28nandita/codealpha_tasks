import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report
df=pd.read_csv(r"C:\internship\codalpha\data science\task1\Iris.csv")
print(df.head())
print(df.columns)
X=df[["SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]]
Y=df["Species"]
print(X.shape)
print(Y.shape)
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
model=KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:", accuracy)
print("Classification report:\n")
print(classification_report(y_test,y_pred))
