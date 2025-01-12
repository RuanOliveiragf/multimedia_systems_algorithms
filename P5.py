def rgb_to_ycbcr(r, g, b):
    e_r = r / 255.0
    e_g = g / 255.0
    e_b = b / 255.0

    y = 219 * (0.299 * e_r + 0.587 * e_g + 0.114 * e_b) + 16
    cb = 224 * (-0.169 * e_r - 0.331 * e_g + 0.5 * e_b) + 128
    cr = 224 * (0.5 * e_r - 0.419 * e_g - 0.081 * e_b) + 128

    return int(round(y)), int(round(cb)), int(round(cr))


rgb_values = list(map(int, input().split()))

ycbcr_values = rgb_to_ycbcr(*rgb_values)

print(*ycbcr_values)
