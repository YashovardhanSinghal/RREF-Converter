## RREF

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Functions](#functions)
- [Example](#example)
- [File Input](#file-input)
- [License](#license)

## Introduction

The provided Python code consists of three main functions:

1. rref: Converts a given matrix to its Reduced Row-Echelon Form (RREF).
2. dict_val: Extracts information about variables and constants from the RREF matrix.
3. para_eq: Represents the system of linear equations based on the RREF matrix and variable information.

The code is designed to handle square and rectangular matrices.

## Usage

To use the code, you can call the rref function with a matrix as an argument. The resulting RREF matrix can be used with the dict_val and para_eq functions to obtain information about the system of linear equations.

python
# Example Usage
matrix_input =  [[4,4,4],[2,2,2],[1,1,1]]
rref_matrix = rref(matrix_input)
variable_info = dict_val(rref_matrix)
modified_dict = simp_dic(variable_info)
para_eq(modified_dict, rref_matrix)


## Functions

### rref(A)

Converts the input matrix A to its Reduced Row-Echelon Form (RREF).

- Input:
  - A: The input matrix as a list of lists.

- Output:
  - Returns the RREF matrix.

### dict_val(rref_mt)

Extracts information about variables and constants from the RREF matrix.

- Input:
  - rref_mt: The RREF matrix.

- Output:
  - Returns a dictionary containing information about variables and constants.

### simp_dic(dict_main)

Simplifies the variable information dictionary by setting coefficients to zero for variables corresponding to free columns.

- Input:
  - dict_main: The variable information dictionary.

- Output:
  - Returns the simplified variable information dictionary.

### para_eq(modify_dict, rref)

Represents the system of linear equations based on the RREF matrix and variable information.

- Input:
  - modify_dict: The simplified variable information dictionary.
  - rref: The RREF matrix.

- Output:
  - Prints the system of linear equations.

## Example

python
# Example Usage
matrix_input =  [[4,4,4],[2,2,2],[1,1,1]]
rref_matrix = rref(matrix_input)
variable_info = dict_val(rref_matrix)
modified_dict = simp_dic(variable_info)
para_eq(modified_dict, rref_matrix)


Output:


['X0', 'X1', 'X2']=[[-0.0, 1.0, -2.0]X2 + 0.0X0 + 0.0X1, 1.0X0 + 1.0X1 + 1.0X2, 0.0X0 + 0.0X1 + 0.0X2]


## File Input

You can also provide the input matrix via a text file. The file should have the following format:


Rows: <number_of_rows>
Cols: <number_of_columns>
<element_11> <element_12> ... <element_1n>
<element_21> <element_22> ... <element_2n>
...
<element_m1> <element_m2> ... <element_mn>


You can use the provided matrix_input.txt file as an example.

## License

This code is provided under the [MIT License](LICENSE).
