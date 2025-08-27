from sklearn.base import BaseEstimator, TransformerMixin
class CreateCustomFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass 

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X.copy()
        X["IsEffectiveTutoring"] = X['Tutoring'] * (X['ParentalSupport'] != 0).astype(int)
        return X