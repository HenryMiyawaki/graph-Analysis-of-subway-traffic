

KEYWORDS = {
    "line": "Linha",
    "station": "Estacoes",
    "station_name": "Estação"
}


class RelationshipTable():
    
    __dataset = None
    __columns = None
    __keywords = None
    __matrix = None

    def __init__(self, dataset, columns = None, keyword = None):
        self.__dataset = dataset

        if keyword == None:
            self.__keywords = KEYWORDS

        if columns == None:
            self.__columns = self.get_columns()

    def get_columns(self):
        
        if self.__columns != None:
            return self.__columns

        cols = []
        for line in self.__dataset:
            for station in line[self.__keywords["station"]]:
                cols.append(station[self.__keywords["station_name"]])

        return cols

    def get_matrix(self):
        if self.__matrix == None:
            self.__matrix = self.evaluate_matrix()
        
        return self.__matrix

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

        self.__matrix = mx
        return self

    def get_repeated_columns_index(self) -> dict:

        itens = {}

        for index, string in enumerate(self.__columns):
            if string not in list(itens.keys()):
                itens[string] = []
            itens[string].append(index)

        for index, key in enumerate(list(itens.keys())):
            if len(itens[key]) == 1:
                del itens[key]


        return itens 

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
    


    def get_matrix(self):
        if self.__matrix == None:
            self.evaluate_matrix()
        return self.__matrix

    def transform_text(self, mx: list, top_columns: False) -> str:

        cols = self.__columns
        text = ""

        if (cols is None) or len(cols) == 0:
            return text

        for i, c in enumerate(cols):
            
            mx_line = ",".join( map(lambda x: str(x), mx[i]) )
            line = f'{c},{mx_line}\n'
            text += line
            
        if top_columns:
            columns = ",".join(cols)
            text = f",{columns}\n{text}"
            
        return text

    def turnoff_interception(self):
        for index, _ in enumerate(self.__columns):
            self.__matrix[index][index] = 0
        return self


    @staticmethod
    def generate_matrix_object(lines: int, cols: int, format = 0) -> list:
        mx = []
        for i in range(lines):
            mx.append([])
            for l in range(cols):
                mx[i].append(0)

        return mx
        
        
