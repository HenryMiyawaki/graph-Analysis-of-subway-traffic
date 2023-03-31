

class Dataset():

    def __init__(self, format: str, location = "./") -> None:
        self.format = format
        self.location = location
        self.data = None
        self.read()

    def read(self) -> bool:
        try:
            with open(f"{self.location}.{self.format}", 'r', encoding="utf-8") as file:
                data = file.read()
                self.data = data
            return True
        except Exception as e:
            print(e)
            return False