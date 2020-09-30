import click
import joblib

CLASSIFER = joblib.load("data/trained_classifer.pkl")


def is_korean_name_batch(names):
    return CLASSIFER.predict(names)


def is_korean_name(name):
    return CLASSIFER.predict([name])[0]


@click.command()
@click.argument("name")
def main(name):
    if is_korean_name(name):
        print(f'"{name}" 은/는 한국인 이름입니다.')
    else:
        print(f'"{name}" 은/는 외국인 이름입니다.')


if __name__ == "__main__":
    main()
