# 로지스틱회귀
#%%
from numpy.core.fromnumeric import mean
from numpy.lib.polynomial import poly
from scipy.sparse.construct import random
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures
import warnings
import pandas as pd  
warnings.simplefilter(action="ignore", category=FutureWarning)

boston_data = load_boston()
transformer = PolynomialFeatures(2)
poly_data = transformer.fit_transform(boston_data.data)
poly_name = transformer.get_feature_names(boston_data.feature_names)

X = pd.DataFrame(poly_data, columns=poly_name)
y = pd.DataFrame(boston_data.target, columns=["MEDV"])

X_trian, X_test, y_trian, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
y_train = y_trian.values.ravel()

model = RandomForestRegressor()
model.fit(X_trian, y_trian)

y_predict = model.predict(X_test)

spec = mean_squared_error(y_test, y_predict) ** 0.5 
print(spec)


# %%
