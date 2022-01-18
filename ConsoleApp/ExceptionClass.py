class CorporateError(RuntimeError):
    def __str__(self):
        return "Corporate Directory Error, Given data is invalid"