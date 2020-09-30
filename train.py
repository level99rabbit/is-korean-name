import joblib
from sklearn.model_selection import train_test_split
from utils.dataframe import make_dataframe
from utils.features import get_features
from utils.pipeline import get_pipeline
from utils.score import print_clf_eval, print_kfold


def main():
    # dataframe 만들기
    df = make_dataframe()

    # 훈련 데이터, 테스트 데이터 분리
    train_names, test_names, train_labels, test_labels = train_test_split(
        df["name"], df["label"], test_size=0.2
    )

    # 파이프라인 만들기
    features = get_features()
    pipeline = get_pipeline(features)

    # 훈련 시키기
    pipeline.fit(train_names, train_labels)

    # 평가
    pred = pipeline.predict(test_names)
    print_clf_eval(test_labels, pred)

    # 평가 (kfold)
    print_kfold(pipeline, test_names, test_labels)

    # 저장
    joblib.dump(pipeline, "data/trained_classifer.pkl")


if __name__ == "__main__":
    main()
