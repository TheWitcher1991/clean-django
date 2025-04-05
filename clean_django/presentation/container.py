class Container:
    def __init__(self):
        self._providers = {}

    def register(self, name: str, provider):
        self._providers[name] = provider

    def resolve(self, name: str):
        if name not in self._providers:
            raise Exception(f"Dependency {name} not found.")
        return self._providers[name]()


container = Container()
