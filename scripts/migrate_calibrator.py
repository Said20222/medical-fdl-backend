import pickle

class _Redirector(pickle.Unpickler):
    def find_class(self, module, name):
        if name == "PlattCalibrator":
            from app.calibration import PlattCalibrator
            return PlattCalibrator
        return super().find_class(module, name)

with open("artifacts/platt_calibrator.pkl", "rb") as f:
    cal = _Redirector(f).load()   # works even with __main__ in the pkl

with open("artifacts/platt_calibrator.pkl", "wb") as f:
    pickle.dump(cal, f)           # re-saved with correct module path