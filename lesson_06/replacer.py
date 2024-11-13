def my_replace(string: str) -> str:
    temp = string.replace("'", "**-temp-**")
    temp = temp.replace('"', "'")
    result = temp.replace("**-temp-**", '"')
    return result


assert my_replace("'hello'") == '"hello"'
assert my_replace('"hello"') == "'hello'"
assert my_replace("'") == '"'
