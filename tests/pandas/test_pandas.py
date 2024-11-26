def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


import os
import pandas as pd

from sasviya.ml.linear_model import LogisticRegression
from sasviya.ml.tree import DecisionTreeClassifier, ForestClassifier, GradientBoostingClassifier

from sklearn.model_selection import train_test_split


def fit_model(X_train, y_train, X_test, y_test, model):
    model.fit(X_train, y_train)
    y_pred_test = model.predict(X_test)

    train_score =  model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    return y_pred_test, test_score


def test_decision_tree():
    workspace=f'{os.environ["WORKSPACE"]}/goodlist/data/'
    heart_df=pd.read_csv(workspace+'heart_disease.csv')
    heart_df.shape

    heart_df.info()
    cols_sum_null = heart_df.isnull().sum()
    hasnull_cols = cols_sum_null[cols_sum_null != 0]
    for col in hasnull_cols.index:
        mean = heart_df[col].mean()
        heart_df[col].fillna(mean, inplace=True)
    X = heart_df.drop('target', axis=1)
    y = heart_df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    logreg = LogisticRegression(
        solver='lbfgs',
        tol=1e-4,
        max_iter=1000)
    y_pred_test, score_logreg = fit_model(X_train, y_train, X_test, y_test, model=logreg)