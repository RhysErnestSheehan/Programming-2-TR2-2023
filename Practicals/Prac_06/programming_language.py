class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        pass

    def __str__(self):
        return f"{self.language}, {self.reflection}, First appear in {self.year}"
