from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             precision_score, recall_score, roc_auc_score)
from sklearn.model_selection import KFold, cross_val_score


def print_clf_eval(y_test, pred):

    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    roc_auc = roc_auc_score(y_test, pred)
    print(
        "정확도: {0:.4f}, AUC:{4:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f}, F1: {3:.4f}".format(
            accuracy, roc_auc, precision, recall, f1
        )
    )

    confusion = confusion_matrix(y_test, pred)
    print("오차 행렬")
    print(confusion)


def print_kfold(model, X, Y):
    kf = KFold(n_splits=10, shuffle=True)

    cv_results = cross_val_score(
        model,
        X,
        Y,
        cv=kf,
        scoring="roc_auc",
        n_jobs=-1,
    )

    print("k-폴드", cv_results.mean())
