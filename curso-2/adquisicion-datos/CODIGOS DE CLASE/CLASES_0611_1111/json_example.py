import json

def example():
    data = {
        "nombre": "Alvaro",
        "gatos": ["puma", "león"]
    }
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    print(json_data)
    obj = json.loads(json_data)
    print(obj)

if __name__ == "__main__":
    example()