from models.Page import Page


def simulate_fifo_page_replacement(
        page_reference_array: list[int], memory_capacity, max_page_num
) -> list[list[int]]:
    """Simulates a FIFO page replacement algorithm"""
    # initialize array with Pages
    pages = [Page(x) for x in range(max_page_num)]
    page_frames_memory = []  # max len -> num_of_page_frames
    oldest_page_index = 0  # initialize variable holding the index of the oldest page in the memory

    for page_num in page_reference_array:
        page = pages[page_num]

        # if page is in memory
        if page in page_frames_memory:
            # continue to the next page reference
            continue

        # if memory is still available
        if len(page_frames_memory) < memory_capacity:
            # add page to the memory
            page_frames_memory.append(page)
            # set page's faults to 1
            page.page_faults = 1
            # continue to the next page reference
            continue

        # if all the available memory is taken
        # replace the page that was in the memory for the longest time with the new one
        page_frames_memory[oldest_page_index] = page
        # increase page's faults
        if page.page_faults is None:
            page.page_faults = 1
        else:
            page.page_faults += 1
        # increase index of the oldest page
        oldest_page_index += 1

        # if oldest_page_index is larger than page frames memory size
        if oldest_page_index == memory_capacity:
            # make oldest_page_index start from the beginning
            oldest_page_index = 0

    # get all page faults
    page_faults = [[page.page_faults] for page in pages if page.page_faults is not None]

    # print(f'FIFO total page faults: {sum([x[0] for x in page_faults])}')
    # print(f'FIFO avg page faults: {sum([x[0] for x in page_faults]) / len(page_faults)}')

    return page_faults
