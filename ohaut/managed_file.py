class ManagedFile:
    """This class manages files with entries enclosed by comments."""
    def __init__(self, filename):
        self._filename = filename

    def _read(self):
        try:
            with open(self._filename, 'r') as f:
                return f.read()
        except IOError:
            return ""

    def _write(self, data):
        with open(self._filename, 'w') as f:
            f.write(data)

    @staticmethod
    def _entry_marks(entry):
        return ("// OHAUT_ITEM({}):START //\n".format(entry),
                "// OHAUT_ITEM({}):END //\n".format(entry))

    def update_entry(self, data, marks, value):
        start = data.find(marks[0])
        end = data.find(marks[1])
        start += len(marks[0])
        self._write(data[:start] + value + "\n" + data[end:])

    def add_entry(self, data, marks, value):
        self._write(data + "\n" + marks[0] + value + "\n" + marks[1])

    def get_entry(self, entry):
        data = self._read()
        marks = self._entry_marks(entry)
        start = data.find(marks[0])
        end = data.find(marks[1])
        if start >= 0:
            start += len(marks[0])
            return data[start:end-1]

    def set_entry(self, entry, value):
        data = self._read()
        marks = self._entry_marks(entry)
        if data.find(marks[0])>=0:
            self.update_entry(data, marks, value)
        else:
            self.add_entry(data, marks, value)
