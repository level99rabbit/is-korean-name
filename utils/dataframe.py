import pandas


def _get_names(filename):
    return pandas.read_csv(f"data/names/{filename}", encoding="utf-8", names=["name"])


def make_dataframe():
    #
    df = pandas.DataFrame()

    # name 설정
    korean_names = _get_names(filename="korean.txt")
    non_korean_names = _get_names(filename="non_korean.txt")
    df["name"] = korean_names["name"].tolist() + non_korean_names["name"].tolist()

    # label 설정
    # 1 = 한국인 이름
    # 0 = 외국인 이름
    df["label"] = (len(korean_names) * [1]) + (len(non_korean_names) * [0])

    return df
