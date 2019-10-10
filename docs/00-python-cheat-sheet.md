# Python tips and tricks for machine learning

## Data access

### Read data from csv file
Using panda
```python
dataset = pd.read_csv('mydatafile.csv')
```
## Data exploration

### Show average, mean, etc per column
Using the describe method
```python
dataset.describe()
```

### Show correlation between different features of a dataset

#### By numbers in a grid
Use the corr() method, you get a table with all values.
```python
dataset.corr()
```

#### By a heatmap with colors
A heatmap will make things more visual
```python
f, ax = plt.subplots(figsize=(10, 8))
corr = dataset.corr()
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True), square=True, ax=ax,annot=True)
```
<img src="./imgs/cheat-heatmap.png" height="200" />

#### By a pairplot, visually showing how fields behave around each other
```python
sns.pairplot(dataset)
```
<img src="./imgs/cheat-pairplot.png" height="200" />

## Data cleaning

### Remove a column from a dataset
```python
#inplace updates the dataframe 
# axis=1 means column (axis=0 means row)
dataset.drop('COLUMN_NAME', axis=1, inplace=True) 
```

### Remove outliers
Using the '3-sigma' rule, saying that typically 99,7% of all data is between mean and 3*stddev.

```python
from scipy import stats
dataset = dataset[(np.abs(stats.zscore(dataset)) < 3).all(axis=1)]
dataset.describe()
```

### Create features and output sets of dataframe
Easiest is to take the column for the output as y and drop it to keep the X
```python
y = dataset.OutputColumn.values
X = dataset.drop(['OutputColumn'],axis=1)
```

### Split data in training and test set
Using the standard function train_test_split:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
```

## Machine learning models

### Linear regression
Fitting the model:
```python
regression_model = linear_model.LinearRegression()
regression_model.fit(X_train,y_train)
```

Predicting the output, using the model:
```python
feature_values = np.array([0.3, 4, 5])
output = regression_model.predict(feature_values.reshape(1,-1))
# This returns an numpy.ndarray with all output values
```

## Machine learning model evaluation

```python
# Evaluate the model
y_predicted = model.predict(X_test)

## Mean Absolute Error
from sklearn.metrics import mean_absolute_error
MAE = mean_absolute_error(y_test,y_predicted)

## Mean Squared Error
from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_test,y_predicted)

## coefficient of determination = r2 score
from sklearn.metrics import r2_score
r2 = r2_score(y_test,y_predicted)
```