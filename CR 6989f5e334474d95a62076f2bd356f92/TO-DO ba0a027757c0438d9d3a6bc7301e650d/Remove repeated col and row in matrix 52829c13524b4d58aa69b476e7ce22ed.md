# Remove repeated col and row in matrix

Status: Done

```python
mx[42 - 1][10] = 2
mx[42][10] = 2
mx[42 + 1][10] = 2

mx[42 - 1][42] = 3
mx[42][42] = 3
mx[42 + 1][42] = 3

mx[42][9] = 4
mx[42][10] = 4
mx[42][11] = 4

mx[10-1][42] = 5
mx[10][42] = 5
mx[10+1][42] = 5
```

To avoid overlooping and remove repeated columns and rows in a matrix using a symmetric hash column removal approach, you can use the above and following basic code implementation

## First Implementation on `evaluate_matrix()`

To connect stations using a flag up and above logic that avoids creating repeated columns and rows, we can use a slightly different approach. Instead of simply removing the repeated columns and rows, we can modify the original matrix in such a way that the repeated columns and rows have the same value, and this value can be used to calculate the hash function.

```python
def evaluate_matrix(self):

        mx_cols = self.__columns
        mx_lines = self.__columns

        if (mx_cols == None) or (mx_lines == None):
            cols = self.get_columns()
            lines = cols

        mx = RelationshipTable.generate_matrix_object(len(mx_cols), len(mx_lines))

        for idx_col, col in enumerate(mx_cols):
            for idx_lines, line in enumerate(mx_lines):
    
                station_line = mx_cols[idx_col]
                station_col = mx_lines[idx_lines]
              
                if (station_line == station_col):
                    
                    mx[idx_col][idx_lines] = 1

                    if (len(mx[idx_col]) != idx_lines + 1):
                        mx[idx_col][idx_lines + 1] = 1
                        mx[idx_col + 1][idx_lines] = 1
                    if (idx_lines != 0):
                        mx[idx_col][idx_lines - 1] = 1
                        mx[idx_col - 1][idx_lines] = 1
```

## Warning

<aside>
❗ We are not sure how this would be impacted with other dataset diferent than ours, but if follow the same rules, other matrix can be generated if the dataset follow the same rules.

When working with any algorithm or method, it's important to note that its effectiveness may depend on the specific dataset being used. This is also true for the method we have described for connecting stations in a matrix using the flag up and above logic.

While we have described a specific approach for generating a matrix that connects stations using this logic, we cannot guarantee that this method will work equally well for all datasets. If the dataset follows the same rules as our example, with a specific format for the input and output, then the method should work well.

However, if the dataset has different rules or different input/output formats, then the method may need to be adapted or modified to work effectively. Additionally, the specific values used for the flag up and above may also need to be adjusted for different datasets, as they may not be optimal for all cases.

In general, it's important to test any method or algorithm on a range of different datasets to ensure that it is effective and robust across a variety of scenarios. If issues or inconsistencies arise, then the method may need to be adjusted or refined to better suit the specific dataset or problem at hand.

</aside>

# Method: `merge_duplicated()`

```python
def merge_duplicated(self):

        repeated = self.get_repeated_columns_index()
        arr = []

        for key in list(repeated.keys()):
            arr.extend(repeated[key][1:])

        arr = sorted(arr, reverse=True)

        for index in arr:
            del self.__matrix[index]
            for x in self.__matrix:
                del x[index] 
            del self.__columns[index]

        return self
```