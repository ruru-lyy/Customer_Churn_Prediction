def label_encode_columns(X):
    from sklearn.preprocessing import LabelEncoder
    import pandas as pd
    X = X.copy()
    for i in range(X.shape[1]):
        le = LabelEncoder()
        X.iloc[:, i] = le.fit_transform(X.iloc[:, i])
    return X

