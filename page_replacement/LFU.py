from models.Page import Page


def simulate_lfu_page_replacement(
        page_reference_array: list[int], num_of_page_frames, max_page_num
) -> list[list[int]]:
    """Simulates a LFU page replacement algorithm"""
    pages = [Page(x) for x in range(max_page_num)]
    page_frames_memory = []  # max len -> num_of_page_frames

    for page_num in page_reference_array:
        page = pages[page_num]

        # if page is in memory continue
        if page in page_frames_memory:
            page.page_frequency += 1
            continue

        # if memory is still available -> add the page to the memory
        if len(page_frames_memory) < num_of_page_frames:
            page_frames_memory.append(page)
            page.page_frequency = 1
            page.page_faults = 1
            continue

        # if all the available memory is taken
        # get the index of the least frequently used page
        lfu_page_index = min(range(len(page_frames_memory)), key=page_frames_memory.__getitem__)

        # page_frames_memory[lfu_page_index].page_frequency = 0  # when removing page from memory -> reset its frequency
        page_frames_memory[lfu_page_index] = page
        page.page_frequency += 1
        if page.page_faults is None:
            page.page_faults = 1
        else:
            page.page_faults += 1

    page_faults = [[page.page_faults] for page in pages if page.page_faults is not None]
    # print(f'LFU total page faults: {sum([x[0] for x in page_faults])}')
    # print(f'LFU avg page faults: {sum([x[0] for x in page_faults]) / len(page_faults)}')

    return page_faults
