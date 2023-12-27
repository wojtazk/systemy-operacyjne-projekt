from models.Page import Page


def simulate_fifo_page_replacement(
        page_reference_array: list[int], num_of_page_frames, max_page_num
) -> list[list[int]]:
    """Simulates a FIFO page replacement algorithm"""
    pages = [Page(x) for x in range(max_page_num)]
    page_frames_memory = []  # max len -> num_of_page_frames
    oldest_page_index = 0

    for page_num in page_reference_array:
        page = pages[page_num]

        # if page is in memory continue
        if page in page_frames_memory:
            continue

        # if memory is still available -> add the page to the memory
        if len(page_frames_memory) < num_of_page_frames:
            page_frames_memory.append(page)
            page.page_faults = 1
            continue

        # if all the available memory is taken
        page_frames_memory[oldest_page_index] = page
        if page.page_faults is None:
            page.page_faults = 1
        else:
            page.page_faults += 1
        oldest_page_index += 1

        # if oldest_page_index is larger than page_frames_memory size -> make it start from the beginning again
        if oldest_page_index == num_of_page_frames:
            oldest_page_index = 0

    page_faults = [[page.page_faults] for page in pages if page.page_faults is not None]
    print(f'FIFO total page faults: {sum([page.page_faults for page in pages if page.page_faults is not None])}')

    return page_faults
