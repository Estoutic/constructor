class Triangle:

    def __init__(self) -> None:
        super().__init__()
        self.bars_data = []
        self.available_bars = {}
        self.available_triangle = 0

    def enter_data(self):
        count_bars = int(input())
        while count_bars != 0:
            bar_length = input(int())
            self.bars_data.append(bar_length)
            count_bars -= 1

    def get_count_of_triples(self):
        for element in self.bars_data:
            self.available_bars[element] = self.bars_data.count(element)

    def get_variables_of_triangle(self):
        for element in self.available_bars.values():
            if int(element) // 3 != 0:
                self.available_triangle += int(element) // 3
        print(self.available_triangle)