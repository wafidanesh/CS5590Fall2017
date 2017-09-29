import numpy as np
import matplotlib.pyplot as plt

X = np.array([0,1,2,3,4,5,6,7,8,9])
Y = np.array([1,3,2,5,7,8,8,9,10,12])

X_bar = np.mean(X)
Y_bar = np.mean(Y)

# Determination of beta1_hat
num = sum((X-X_bar)*(Y-Y_bar).T)
den = sum(pow((X-X_bar),2))

beta1_hat = num/den
print(beta1_hat)

# Determination of beta0_hat
beta0_hat = Y_bar - (beta1_hat*X_bar)
print(beta0_hat)

# Estimating the output
Y_hat = beta0_hat + beta1_hat*X

plt.scatter(X,Y)
plt.plot(X,Y_hat,color='red')
plt.show()