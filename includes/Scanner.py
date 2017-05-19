class Scanner:
    def __init__(self, url, kind, identifier, is_json=False):
        self.url = url
        self.kind = kind
        self.identifier = identifier
        self.is_json = is_json
