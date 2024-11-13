def compression(string: str) -> str:
    if len(string) == 0:
        return ""

    result = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            result = result + str(count) + string[i - 1]
            count = 1

    result = result + str(count) + string[-1]

    return result


assert compression("abbcccdddd") == "1a2b3c4d"
assert compression("ddffffee") == "2d4f2e"
