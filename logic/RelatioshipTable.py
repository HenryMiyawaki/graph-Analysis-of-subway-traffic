
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

        first_stations = []
        last_stations = []

        idx_count = 0

        for idy, line in enumerate(self.__dataset):
            
            first_stations.append(idx_count)
            for idx, station in enumerate(line[self.__keywords["station"]]):
                cols.append(station[self.__keywords["station_name"]])
                idx_count += 1
            last_stations.append(idx_count - 1)

        self.__first_stations = first_stations
        self.__last_stations = last_stations

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

        arrow_links = set()

        for idx_lines, line in enumerate(mx_lines):
            for idx_col, col in enumerate(mx_cols):
    
                station_line = mx_cols[idx_lines]
                station_col = mx_lines[idx_col]

                if (station_line == station_col):
                    
                    mx[idx_col][idx_lines] = 1
                    arrow_link = None

                    if idx_col not in self.__first_stations:
                        arrow_link = f"{self.__columns[idx_col - 1]}->{self.__columns[idx_lines]}"
                        mx[idx_lines][idx_col - 1] = 1
                    if idx_col not in self.__last_stations:
                        arrow_link = f"{self.__columns[idx_lines]}->{self.__columns[idx_col + 1]}"
                        mx[idx_lines][idx_col + 1] = 1
                    if idx_lines not in self.__first_stations:
                        arrow_link = f"{self.__columns[idx_lines - 1]}->{self.__columns[idx_col]}"
                        mx[idx_lines - 1][idx_col] = 1 
                    if idx_lines not in self.__last_stations:
                        arrow_link = f"{self.__columns[idx_lines + 1]}->{self.__columns[idx_col]}"
                        mx[idx_lines + 1][idx_col] = 1 
                    
                    if arrow_link != None:
                        arrow_links.add(arrow_link)

        self.__matrix = mx
        self.__arrow_links = arrow_links
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

        self.__enhance()
        return self

    def __enhance(self):
        for arrow_link in self.__arrow_links:
            self.arrow_link(arrow_link)

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
    
    def arrow_link(self, arrow:str):
        
        arr = arrow.split("->")
        index_1 = self.__columns.index(arr[0])
        index_2 = self.__columns.index(arr[1])

        self.__matrix[index_1][index_2] = 1
        self.__matrix[index_2][index_1] = 1

        return self

    @staticmethod
    def generate_matrix_object(lines: int, cols: int, format = 0) -> list:
        mx = []
        for i in range(lines):
            mx.append([])
            for l in range(cols):
                mx[i].append(0)

        return mx
        
        
