import json

class IWorldImport:
    def __init__(self, data_path: str) -> None:
        ...

    #@staticmethod
    #def data_to_dict(path: str) -> bool:
    #    ...
        

class JsonWorld(IWorldImport):
    def __init__(self, data_path: str) -> None:
        super().__init__(data_path)

    def data_to_dict(self, path: str):
        with open(path, "r") as file:
            world_dict = json.loads(str(file))
        return type(world_dict)
