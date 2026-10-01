import requests

def example():
    data = {
        "nombre": "María",
        "gatos": ["misu", "michi"]
    }
    result = requests.post("http://127.0.0.1:5000/echo?name=David", json=data)

    print(result.json())

if __name__ == "__main__":
    example()