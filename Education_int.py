from sklearn.base import BaseEstimator, TransformerMixin


class EducationGroup(BaseEstimator, TransformerMixin):
    """
    This class is responsible for categorizing the education features into correct
    format and finally returns
    """
    def __init__(self):
        pass
    
    def fit(self, x_dataset, y=None):
        return self
    
    def transform(self, x_dataset):
        education = {'Preschool': 1, '1st-4th': 2, '5th-6th': 3, '7th-8th': 4, '9th': 5,
                     '10th': 6, '11th': 7, '12th': 8, 'Hs-grad': 9, 'Some-college': 10,
                     'Assoc-acdm': 12, 'Assoc-voc': 11, 'Bachelors': 13, 'Masters': 14,
                     'Prof-school': 15, 'Doctorate': 16}
        x_dataset.replace({'Education': education}, inplace=True)
        x_dataset['Education'] = x_dataset['Education'].astype('int64')
        return x_dataset