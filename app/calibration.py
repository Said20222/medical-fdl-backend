import numpy as np
from sklearn.linear_model import LogisticRegression


class PlattCalibrator:
    """
    Post-hoc Platt scaling using 1D logistic regression on model scores.

    The backend expects predict_proba(...) to return the same shape as
    sklearn's predict_proba: (N, 2), where column 1 is P(class=1).
    """

    def __init__(self) -> None:
        self._lr = LogisticRegression(
            C=1.0,
            solver="lbfgs",
            max_iter=200,
        )
        self.fitted = False

    def fit(self, val_scores: np.ndarray, val_labels: np.ndarray) -> None:
        """
        val_scores: shape (N,) or (N,1)
            1D model scores used for calibration.
        val_labels: shape (N,)
            Binary ground-truth labels {0,1}.
        """
        x = np.asarray(val_scores, dtype=np.float64).reshape(-1, 1)
        y = np.asarray(val_labels, dtype=int).reshape(-1)

        self._lr.fit(x, y)
        self.fitted = True

        print(
            f"Platt scaling fitted  "
            f"a={self._lr.coef_[0][0]:.4f}  "
            f"b={self._lr.intercept_[0]:.4f}"
        )

    def predict_proba(self, scores: np.ndarray) -> np.ndarray:
        """
        Returns shape (N, 2), matching sklearn predict_proba.
        """
        if not self.fitted:
            raise RuntimeError("Call .fit() first.")

        x = np.asarray(scores, dtype=np.float64).reshape(-1, 1)
        return self._lr.predict_proba(x)