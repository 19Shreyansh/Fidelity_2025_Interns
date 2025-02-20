import json

class Diff:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.json1 = self.load_json(self.file1)
        self.json2 = self.load_json(self.file2)

    def load_json(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    def compare(self):
        key1 = set(self.json1.keys())
        key2 = set(self.json2.keys())
        unique_keys = key1.symmetric_difference(key2)
        return unique_keys

file1 = "first.json"
file2 = "second.json"
diff_checker = Diff(file1, file2)
print("Keys that are unique to either of the JSONs are:", diff_checker.compare())
