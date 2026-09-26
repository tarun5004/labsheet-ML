"""Question 32: load a dataset directly from Scikit-learn."""

from sklearn.datasets import load_iris


def main() -> None:
    iris = load_iris()
    print(f"Samples: {iris.data.shape[0]}")
    print(f"Features: {iris.feature_names}")
    print(f"Targets: {list(iris.target_names)}")


if __name__ == "__main__":
    main()