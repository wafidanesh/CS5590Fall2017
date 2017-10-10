from sklearn.datasets import load_breast_cancer
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn import svm

# Loading the dataset
breastcancerdataset = load_breast_cancer()

# Obtaining observations and responses
x = breastcancerdataset.data
y = breastcancerdataset.target

# Splitting the dataset into train and test sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

# Creating the linear model
linear_model = svm.SVC(kernel='linear')

# Model fit and testing
lin_fit = linear_model.fit(x_train,y_train)

# Prediction with test data
lin_pred = lin_fit.predict(x_test)

# Calculating the accuracy
print(metrics.accuracy_score(y_test,lin_pred))

# Creating the rbf model
rbf_model = svm.SVC(kernel='rbf')

# Model fit and testing
rbf_fit = rbf_model.fit(x_train,y_train)

# Prediction with test data
rbf_pred = rbf_fit.predict(x_test)

# Calculating the accuracy
print(metrics.accuracy_score(y_test,rbf_pred))