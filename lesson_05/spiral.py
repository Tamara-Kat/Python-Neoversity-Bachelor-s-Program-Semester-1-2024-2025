def get_spiral_value(target_x, target_y):
    if target_x == 0 and target_y == 0:
        return 1
    layer = max(abs(target_x), abs(target_y))
    start_value = (2 * layer - 1) ** 2 + 1
    side_length = 2 * layer

    if target_x == layer and target_y != -layer:
        pos = target_y + layer - 1
    elif target_y == layer:
        pos = side_length + (layer - target_x) - 1
    elif target_x == -layer:
        pos = 2 * side_length + (layer - target_y) - 1
    else:
        pos = 3 * side_length + (target_x + layer) - 1

    value = start_value + pos

    return value


print(get_spiral_value(2, 2))
print(get_spiral_value(1, 0))
