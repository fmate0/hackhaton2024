import numpy as np

def read_input_file(filename):
    matrices = {}
    operations = []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')
        
        mode = None
        matrix_name = None
        matrix_data = []
        
        for line in lines:
            if line == "matrices":
                mode = "matrices"
            elif line == "operations":
                mode = "operations"
            elif mode == "matrices":
                if line.isalpha():
                    if matrix_name and matrix_data:
                        matrices[matrix_name] = np.array(matrix_data, dtype=object)
                    matrix_name = line
                    matrix_data = []
                else:
                    matrix_data.append(list(map(int, line.split())))
            elif mode == "operations":
                operations.append(line)
        
        if matrix_name and matrix_data:
            matrices[matrix_name] = np.array(matrix_data, dtype=object)
    
    return matrices, operations

def add_matrices(A, B):
    return A + B

def multiply_matrices(A, B):
    return np.dot(A, B)

def main():
    input_filename = 'input.txt'
    matrices, operations = read_input_file(input_filename)
    
    for operation in operations:
        result = None  
        if '+' in operation:
            operands = operation.split(' + ')
            if len(operands) == 2:
                op1, op2 = operands
                if op1 in matrices and op2 in matrices:
                    result = add_matrices(matrices[op1], matrices[op2])
                else:
                    print(f"Error: Undefined matrices in operation '{operation}'")
                    continue
            else:
                print(f"Error: Invalid operation format '{operation}'")
                continue
        elif '*' in operation:
            operands = operation.split(' * ')
            if len(operands) == 2:
                op1, op2 = operands
                if op1 in matrices and op2 in matrices:
                    result = multiply_matrices(matrices[op1], matrices[op2])
                else:
                    print(f"Error: Undefined matrices in operation '{operation}'")
                    continue
            else:
                print(f"Error: Invalid operation format '{operation}'")
                continue
        
        print(operation)
        if result is not None:
            for row in result:
                print(' '.join(map(str, row)))
        print()

if __name__ == '__main__':
    main()
