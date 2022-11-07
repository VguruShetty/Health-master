def d_pred(l):
    
    import pandas as pd
    import numpy as np
    from sklearn import decomposition
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    import os.path
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'diabetes.csv')
    data=pd.read_csv(filename)


    f=list(data.columns)[:-1]
    x=data[f]
    y=data["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=4)
    X_train=X_train.values.reshape(-1,7)
    y_train=y_train.values.reshape(-1,1)
    X_test=X_test.values.reshape(-1,7)
    y_test=y_test.values.reshape(-1,1)

    clf = KNeighborsClassifier(n_neighbors=5)
    clf = clf.fit(X_train, y_train)
    l=np.array(l)
    l=l.reshape(1,7)
    y_pred = clf.predict(l)
    return y_pred

def c_pred(l):
    import pandas as pd
    import numpy as np
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import decomposition
    from sklearn.model_selection import train_test_split
    import os.path
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'Breast_cancer_data.csv')
    data=pd.read_csv(filename)
    f=list(data.columns)[:-1]
    x=data[f]
    y=data["diagnosis"]
    X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=4)
    X_train=X_train.values.reshape(-1,5)
    y_train=y_train.values.reshape(-1,1)
    X_test=X_test.values.reshape(-1,5)
    y_test=y_test.values.reshape(-1,1)

    clf = KNeighborsClassifier(n_neighbors=5)
    clf = clf.fit(X_train, y_train)
    l=np.array(l)
    l=l.reshape(1,5)
    y_pred = clf.predict(l)
    return y_pred
def h_pred(l):
    import pandas as pd
    import numpy as np
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import decomposition
    from sklearn.model_selection import train_test_split
    import os.path
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'heart.csv')
    data=pd.read_csv(filename)
    f=list(data.columns)[:-1]
    x=data[f]
    y=data["target"]
    X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=4)
    X_train=X_train.values.reshape(-1,13)
    y_train=y_train.values.reshape(-1,1)
    X_test=X_test.values.reshape(-1,13)
    y_test=y_test.values.reshape(-1,1)

    clf = KNeighborsClassifier(n_neighbors=5)
    clf = clf.fit(X_train, y_train)
    l=np.array(l)
    l=l.reshape(1,13)
    y_pred = clf.predict(l)
    return y_pred
    