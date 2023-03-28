# Improve dataset data

Status: In progress

## New class to handle dataset

```jsx
import json

class StationDataset():

    def __init__(self, format: str, location = "./") -> None:
        self.__format = format
        self.__location = location
        self.__data = None
        self.read()

    def read(self) -> bool:
        try:
            with open(f"{self.__location}.{self.__format}", 'r', encoding="utf-8") as file:
                data = file.read()
                self.__data = data
            return True
        except Exception as e:
            return False
    
    def get_dictionary(self) -> dict:
        ## other implementations can be here
        d = {}
        if "json" in self.__format:
            d = json.loads(self.__data)
        return d
```