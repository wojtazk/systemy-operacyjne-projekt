class Page:
    def __init__(self, page_num: int):
        self._page_num: int = page_num
        self._page_faults: int | None = None
        self._page_frequency: int = 0

    # override < operator (needed for my LFU implementation :))
    def __lt__(self, other):
        return self._page_frequency < other.page_frequency

    @property
    def page_num(self) -> int:
        return self._page_num

    @property
    def page_faults(self) -> int | None:
        return self._page_faults

    @page_faults.setter
    def page_faults(self, value: int):
        if value < 0:
            raise ValueError("Page faults cannot be less than 0")
        self._page_faults = value

    @property
    def page_frequency(self) -> int | None:
        return self._page_frequency

    @page_frequency.setter
    def page_frequency(self, value: int):
        if value < 0:
            raise ValueError("Page frequency cannot be less than 0")
        self._page_frequency = value
