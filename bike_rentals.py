import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np



def assign_label(value):
    if (value>=6)&(value<12):
        return 1
    elif (value>=12)&(value<18):
        return 2
    elif (value>=18)&(value<24):
        return 3
    elif (value>=0)&(value<6):
        return 4
def data_processing():
    bike_rentals=pd.read_csv('bike_rental_hours.csv')
#  print(bike_rentals.head(10))
#    bike_rentals['cnt'].describe()
#    plt.hist(bike_rentals['cnt'])
#    correlation=bike_rentals.corr()['cnt'].sort_values(ascending=False)
    bike_rentals['time_label']=bike_rentals['hr'].apply(assign_label)

    train= bike_rentals.sample(frac=0.8,random_state=2)
    test=bike_rentals[~bike_rentals.index.isin(train.index)]
    
    features=['season', 'yr', 'mnth', 'holiday', 'weekday','workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'time_label','hr','instant']
    return train,test,features

def linear_regression(train,test,features):
	print('Linear Regression Model:')
	lr=LinearRegression()
	lr.fit(train[features],train['cnt'])
	predicted=lr.predict(test[features])
	error=np.mean((predicted-test['cnt'])**2)
	print('MSE:',error)
	return None

def decision_trees(train,test,features,min_samples_leaf=1,max_depth=None):
    print('Decision Tree Model:')
    print('Min samples per leaf:',min_samples_leaf)
    print('Maximum Depth of the Tree:',max_depth)
    dt=DecisionTreeRegressor(min_samples_leaf=min_samples_leaf,max_depth=max_depth)
    dt.fit(train[features],train['cnt'])
    predicted=dt.predict(test[features])
    error=np.mean((predicted-test['cnt'])**2)
    print('MSE:',error)
    return None

def random_forests(train,test,features,min_samples_leaf=5):
	print('Random Forest model:')
	print('Min samples per leaf:',min_samples_leaf)
	rf=RandomForestRegressor(min_samples_leaf=min_samples_leaf,n_estimators=100,random_state=1)
	rf.fit(train[features],train['cnt'])
	predicted=rf.predict(test[features])
	error=np.mean((predicted-test['cnt'])**2)
	print('MSE:',error)
	return None

if __name__=='__main__':
	train,test,features=data_processing()
	linear_regression(train,test,features)
	decision_trees(train,test,features,5)
	random_forests(train,test,features,min_samples_leaf=5)


    

    

    

