from models.Page import Page


def simulate_lfu_page_replacement(
        page_reference_array: list[int], num_of_page_frames, max_page_num
) -> list[list[int]]:
    """Simulates a LFU page replacement algorithm"""
    # initialize array with Pages
    pages = [Page(x) for x in range(max_page_num)]
    memory = []  # max len -> num_of_page_frames

    for page_num in page_reference_array:
        page = pages[page_num]

        # if page is in memory
        if page in memory:
            # move page at the end of the array
            # (we want to first remove pages that are present in the memory for the longest)
            # remove page from the memory
            memory.remove(page)
            # append the page at the end of the memory
            memory.append(page)
            # increase page's frequency
            page.page_frequency += 1
            # sort memory
            _sort_memory_on_pages_frequency(memory)
            # continue to the next page reference
            continue

        # if memory is still available
        if len(memory) < num_of_page_frames:
            # add page to memory
            memory.append(page)
            # increase page frequency
            page.page_frequency += 1
            # set page faults to 1 (instead of None)
            page.page_faults = 1
            # sort memory
            _sort_memory_on_pages_frequency(memory)
            # continue to the next page reference
            continue

        # if all the available memory is taken
        # first element should be least frequently used and older than other pages with the same frequency
        # decrease frequency of first element in memory
        # we could also reset elements frequency to 0, but we will stick to decreasing
        memory[0].page_frequency -= 1
        # remove first element from memory
        memory.pop(0)
        # add new element at the end of the memory
        memory.append(page)
        # increase page's frequency
        page.page_frequency += 1
        # increase page's faults
        if page.page_faults is None:
            page.page_faults = 1
        else:
            page.page_faults += 1

        # sort memory
        _sort_memory_on_pages_frequency(memory)

    # get all pages faults
    page_faults = [[page.page_faults] for page in pages if page.page_faults is not None]

    # print(f'LFU total page faults: {sum([x[0] for x in page_faults])}')
    # print(f'LFU avg page faults: {sum([x[0] for x in page_faults]) / len(page_faults)}')

    return page_faults


def _sort_memory_on_pages_frequency(memory: list[Page]) -> None:
    """Sorts pages in memory from least to most frequent"""
    """AKA bubble sort lite"""
    # we insert at most one element at every loop pass (in LFU simulation),
    # so one sorting pass should be enough

    # sort pages starting from the penultimate page, based on theirs frequency
    for i in range(len(memory) - 2, -1, -1):
        # if pages frequency is the same, the page arriving first should be placed first
        # else we swap pages in memory
        if memory[i].page_frequency > memory[i + 1].page_frequency:
            memory[i], memory[i + 1] = memory[i + 1], memory[i]
        else:
            # In LFU new elements are inserted at the end of the memory
            # when comparison above fails, it means the array is sorted
            break
