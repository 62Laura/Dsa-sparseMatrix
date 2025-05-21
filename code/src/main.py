import os
from sparseMatrix import SparseMatrix

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    firstmatrixFilePath = os.path.join(base_dir, 'sample_input', 'matrix1.txt')
    secondmatrixFilePath = os.path.join(base_dir, 'sample_input', 'matrix2.txt')
    outputAddPath = os.path.join(base_dir, 'sample_results', 'addition_result.txt')
    outputSubPath = os.path.join(base_dir, 'sample_results', 'subtraction_result.txt')
    outputMultPath = os.path.join(base_dir, 'sample_results', 'multiplication_result.txt')

    try:
        matrix1 = SparseMatrix(firstmatrixFilePath)
        matrix2 = SparseMatrix(secondmatrixFilePath)

        print(f"✅ Loaded matrices successfully.")
        print(f"🔢 Matrix1: {matrix1.rows}x{matrix1.cols}")
        print(f"🔢 Matrix2: {matrix2.rows}x{matrix2.cols}")

        # Addition
        try:
            resultAdd = matrix1.add(matrix2)
            resultAdd.save_to_file(outputAddPath)
            print(f"➕ Addition saved to: {outputAddPath}")
        except Exception as e:
            print(f"⚠️ Could not perform addition: {e}")

        # Subtraction
        try:
            resultSub = matrix1.subtract(matrix2)
            resultSub.save_to_file(outputSubPath)
            print(f"➖ Subtraction saved to: {outputSubPath}")
        except Exception as e:
            print(f"⚠️ Could not perform subtraction: {e}")

        # Multiplication
        try:
            if matrix1.cols != matrix2.rows:
                raise ValueError(f"Cannot multiply: matrix1.cols ({matrix1.cols}) != matrix2.rows ({matrix2.rows})")

            resultMult = matrix1.multiply(matrix2)
            resultMult.save_to_file(outputMultPath)
            print(f"✖️ Multiplication saved to: {outputMultPath}")
        except Exception as e:
            print(f"⚠️ Could not perform multiplication: {e}")

        print("\n✅ All valid operations completed.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    main()





