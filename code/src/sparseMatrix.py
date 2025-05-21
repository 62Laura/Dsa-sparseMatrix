import os

class SparseMatrix:
    def __init__(self, file_path=None, rows=0, cols=0):
        self.elements = {}
        self.rows = rows
        self.cols = cols
        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Matrix file not found: {path}")

        with open(path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        try:
            self.rows = int(lines[0].split('=')[1])
            self.cols = int(lines[1].split('=')[1])
        except Exception:
            raise ValueError("Matrix file must start with 'rows=' and 'cols=' lines")

        for line in lines[2:]:
            if line.startswith('(') and line.endswith(')'):
                try:
                    row, col, val = map(int, line.strip('()').split(','))
                    if val != 0:
                        self.elements[(row, col)] = val
                except ValueError:
                    raise ValueError(f"Invalid element format in line: {line}")
            else:
                raise ValueError(f"Invalid matrix element line: {line}")

    def get(self, row, col):
        return self.elements.get((row, col), 0)

    def set(self, row, col, val):
        if val != 0:
            self.elements[(row, col)] = val
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        self._check_same_size(other, "addition")
        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.elements = self.elements.copy()

        for (r, c), val in other.elements.items():
            result.set(r, c, result.get(r, c) + val)

        return result

    def subtract(self, other):
        self._check_same_size(other, "subtraction")
        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.elements = self.elements.copy()

        for (r, c), val in other.elements.items():
            result.set(r, c, result.get(r, c) - val)

        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError(f"Matrix sizes don't match for multiplication: "
                             f"{self.rows}x{self.cols} cannot be multiplied with {other.rows}x{other.cols}")

        result = SparseMatrix(rows=self.rows, cols=other.cols)

        for (i, k), val1 in self.elements.items():
            for j in range(other.cols):
                val2 = other.get(k, j)
                if val2 != 0:
                    result.set(i, j, result.get(i, j) + val1 * val2)

        return result

    def save_to_file(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            for (r, c), v in sorted(self.elements.items()):
                f.write(f"({r}, {c}, {v})\n")

    def _check_same_size(self, other, operation):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"Matrix size mismatch for {operation}: "
                             f"{self.rows}x{self.cols} vs {other.rows}x{other.cols}")
