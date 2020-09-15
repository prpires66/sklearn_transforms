from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class SimpleOne(BaseEstimator):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()

        si = SimpleImputer(missing_values=np.nan,
                           strategy='constant',
                           fill_value=1,verbose=0,
                           copy=True
                           )
        data[['INGLES']] = si.fit_transform(X=data[['INGLES']])
        return data

class SimpleTwo(BaseEstimator):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
   
        data['NOTA_GO'].fillna((data['NOTA_DE']+data['NOTA_EM']+data['NOTA_MF'])/3,inplace=True)
        return data

class LabelTrans (BaseEstimator):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
   
        le = LabelEncoder ()
        # aplicar le em colunas de características categóricas 
        data['PERFIL'] = le.fit_transform(data['PERFIL'])
        return data

class StdScaler (BaseEstimator):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        features = ["MATRICULA", "NOTA_DE", "NOTA_EM", "NOTA_MF", "NOTA_GO","INGLES", "H_AULA_PRES", "TAREFAS_ONLINE", "FALTAS",]
        std = StandardScaler()
        # aplicar le em colunas de características categóricas 
        data[features] = pd.DataFrame(std.fit_transform (data[features]),columns=[features]) 
        return data