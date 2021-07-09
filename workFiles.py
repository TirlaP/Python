# File Objects

# Context manager

with open('kaizen.jpg', 'rb') as rf:
    with open('kaizen_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)





