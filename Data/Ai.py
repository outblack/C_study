#%%
import pandas as pd   
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("/Users/jhkim/Downloads/score.csv")

# %%
X = pd.DataFrame(df["Time"], columns=["Time"])
X
# %%
y = pd.DataFrame(df["Korean"], columns=["Korean"])
y
# %%
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=5)

# %%
model = LinearRegression()
model.fit(x_train, y_train)
# %%
y_test_pred = model.predict(x_test)
y_test_pred
# %%
x_test
# %%
