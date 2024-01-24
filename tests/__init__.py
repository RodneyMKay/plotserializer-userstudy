def read_plot(name: str) -> str:
    with open(f"tests/plots/{name}.json", "r", encoding="utf-8") as file:
        return file.read()
