import map


def sanitize (str_ar):
    val = len(str_ar[0].split())
    map_data = map.Map(val, len(str_ar), [])
    for line in str_ar:
        line_s = line.split()
        if len(line_s) != val:
            print("File not formatted correctly")
            return None
        map_data.array.extend(line_s)
    if map_data.height * map_data.width > 50:
        print("You are not allowed more than 50 data points")
        return None
    for val in map_data.array:
        if not val.isdigit():
            print("The file can only contain integers")
            return None
    return map_data
