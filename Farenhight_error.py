class FahrenheitError(Exception):
    min_f = 32
    max_f = 212
   
    def __init__(self, *args: object, f) -> None:
        super().__init__(args)
        self.f = f
   
    def __str__(self) -> str:
        """
            Returna ett rimligt felmeddelande.
        """
        return f""
   
def fahrenheit_to_celsius(f: float):
    if f < FahrenheitError.min_f or f> FahrenheitError.max_f:
        raise FahrenheitError(f)
    return (f - 32)/ 5 * 9

if __name__ == "__main__":
    pass
