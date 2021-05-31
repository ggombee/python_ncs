from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

np.random.seed(0)  # 랜덤값을 고정시키는 목적
'''
>> DF의 컬럼들의 값 
Index(
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)'], dtype='object')
'''


class Iris(object):
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    def __init__(self):
        self._features = None
        self._train = None
        self._test = None

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, features):
        self._features = features

    @property
    def train(self):
        return self._train

    @train.setter
    def train(self, train):
        self._train = train

    @property
    def test(self):
        return self._test

    @features.setter
    def test(self, test):
        self._test = test

    def show_df(self):
        print(f'>> DF의 컬럼들의 값 {self.df.columns}')
        print(f'>> DF의 상단 5개의 값 {self.df.head()}')
        print(f'>> DF의 하단 5개의 값 {self.df.tail()}')

    def train(self):
        df = self.df
        iris = self.iris
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75  # train set 75%
        print(f'df.columns : {df.columns}')
        """Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
               'petal width (cm)', 'species', 'is_train']"""
        train, test = df[df['is_train'] == True], df[df['is_train'] == False]
        self.features = df.columns[:4]  # 앞에서부터 4번째 컬럼(피처)까지 추출
        print(f'features : {self.features}')
        """Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
               'petal width (cm)'],"""
        y = pd.factorize(train['species'])[0]
        print(f'y : {y}')

    def evaluate(self):
        iris = self.iris
        features = self.features
        train = self.train
        test = self.test
        clf = RandomForestClassifier(n_jobs=2, random_state=0)
        preds = iris.target_names[clf.predict(test[features])]
        print(preds[0:5])
        print(test['species'].head())
        print('크로스탭 결과')
        print(pd.crosstab(test['species'], preds, rownames=['Actual Species'], \
                          colnames=['Predicted Species']))
        print('피처별 중요도')
        print(list(zip(train[features], clf.feature_importances_)))

    @staticmethod
    def main():
        instance = Iris()
        while 1:
            menu = int(input('0.Exit 1.DF Info 2.Train'))
            if menu == 0:
                break
            elif menu == 1:
                instance.show_df()
            elif menu == 2:
                instance.train()


Iris.main()