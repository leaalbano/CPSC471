def split_to_file_size_and_payload_helper(splitheader):
    fileName = splitheader[1].split(':')[1]
    size = splitheader[2].split(':')[1]
    payload = splitheader[3].split(':')[1]
    return fileName, size, payload