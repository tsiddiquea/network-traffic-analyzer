class Report:
    def __init__(self, filename="report.txt"):
        self.filename = filename
        self.lines = []

    def add(self, *text):
        line = " ".join(str(t) for t in text)
        self.lines.append(line)

    def add_summary(self, summary_lines):
        self.lines.append("")
        self.lines.append("===== TRAFFIC SUMMARY =====")

        for line in summary_lines:
            self.lines.append(line)

    def print(self):
        for line in self.lines:
            print(line)

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for line in self.lines:
                f.write(line + "\n")

        print("\nReport saved to", self.filename)