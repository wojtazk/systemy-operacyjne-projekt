class Process:
    def __init__(self, arrival_time: int, burst_time: int):
        if arrival_time < 0 or burst_time < 1:
            raise ValueError('Arrival time or Burst time is invalid')

        self._arrival_time: int = arrival_time
        self._burst_time: int = burst_time
        self._remaining_burst_time: int = burst_time

        self._completion_time: int | None = None
        self._turn_around_time: int | None = None
        self._waiting_time: int | None = None

    # get all properties in an array
    def get_properties_as_list(self) -> list:
        """Get all Process properties in an array"""
        return [
            self._arrival_time,
            self._burst_time,
            self._remaining_burst_time,
            self._completion_time,
            self._turn_around_time,
            self._waiting_time
        ]

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def burst_time(self):
        return self._burst_time

    @property
    def remaining_burst_time(self):
        return self._remaining_burst_time

    @remaining_burst_time.setter
    def remaining_burst_time(self, value: int):
        if value < 0:
            raise ValueError('Remaining burst time is less than 0')
        self._remaining_burst_time = value

    @property
    def completion_time(self):
        return self._completion_time

    @completion_time.setter
    def completion_time(self, value: int):
        if value < 1:
            raise ValueError('Completion time cannot be less than 1')
        self._completion_time = value

    @property
    def turn_around_time(self):
        return self._turn_around_time

    @turn_around_time.setter
    def turn_around_time(self, value: int):
        if value < 1:
            raise ValueError('Turn around time cannot be less than 1')
        self._turn_around_time = value

    def calculate_turn_around_time(self):
        if not self._completion_time:
            raise ValueError("Can't calculate turn around time, completion time or arrival time is invalid")

        self._turn_around_time = self._completion_time - self._arrival_time

    @property
    def waiting_time(self):
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, value: int):
        if value < 1:
            raise ValueError('Waiting time cannot be less than 1')
        self._waiting_time = value

    def calculate_waiting_time(self):
        if not (self._turn_around_time and self._burst_time):
            raise ValueError("Can't calculate waiting time, turn around time or burst time is invalid")
        self._waiting_time = self._turn_around_time - self._burst_time

# test
# test = Process(12, 45)
# test.completion_time = 80
# test.calculate_turn_around_time()
# test.calculate_waiting_time()
# test_arr = test.get_properties_as_list()
#
# print(test_arr)
