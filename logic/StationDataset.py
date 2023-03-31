import json
from logic.Dataset import Dataset

class StationDataset(Dataset):

    def __init__(self, format: str, location="./") -> None:
        super().__init__(format, location)

    def get_dictionary(self) -> dict:
        ## other implementations can be here
        d = {}
        if "json" in self.format:
            d = json.loads(self.data)
        
        return d