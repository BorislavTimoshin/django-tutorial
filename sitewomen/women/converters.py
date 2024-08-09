class FourDigitYearConverter:
    regex = r'\d{4}'

    def to_python(self, value) -> int:
        return int(value)

    def to_url(self, value) -> str:
        return str(value)
