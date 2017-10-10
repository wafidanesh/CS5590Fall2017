from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split

# Loading the dataset
data_boston = load_boston()
print(data_boston.data.shape)

x = data_boston.data
y = data_boston.target
print(x.shape,y.shape)

# Splitting the data into train and test sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

# Creating the linear regression model
model = LinearRegression()
mod_fit = model.fit(x_train,y_train,sample_weight=None)

# Predicting using the linear regression model
train_pred = mod_fit.predict(x_train)  # Prediction on the training set
print(mod_fit.score(x_train,y_train))

test_pred = mod_fit.predict(x_test)  # Prediction on the test set
print(mod_fit.score(x_test,y_test))


