import json
import io


def get_data_from_json(filename: str) -> list[dict]:
    if type(filename) is not str:
        return []

    file = io.open(filename, encoding='utf-8')
    data = json.load(file)
    file.close()

    return data
