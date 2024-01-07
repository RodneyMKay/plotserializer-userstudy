def read_plot(name: str) -> str:
    with open(f"tests/plots/{name}.json", "r") as file:
        return file.read()
