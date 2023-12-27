def write_data_to_file(data: list, filename: str) -> None:
    """Writes data from an array to a file"""
    with open(filename, 'w') as file:
        for sample in data:
            new_line = ';'.join(str(x) for x in sample) + '\n'
            file.write(new_line)
