from PIL import Image as im

def grey_scale_image(image):
    pixels = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pix = pixels[x, y]
            new_color = int((pix[0] + pix[1] + pix[2]) / 3)
            pixels[x, y] = (new_color, new_color, new_color)
    return image

def blur_image(image):
    pixels = image.load()
    kernel = [
        [1, 4, 4],
        [4, 16, 4],
        [1, 4, 1]
    ]
    for times in range(10):
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                kernelised = apply_kernel(get_pixels_in_range(pixels, x, y), kernel)
                res_pixel = sum_matrix(kernelised)
                for v in range(len(res_pixel)):
                    res_pixel[v] = int(res_pixel[v] / kernel_sum(kernel))
                pixels[x, y] = tuple(res_pixel)
    return image

def kernel_sum(kernel):
    sum_val = 0
    for x in range(len(kernel)):
        sum_val += sum(kernel[x])
    return sum_val

def multiply_matrix(matrix, value):
    for x in range(len(matrix)):
        tup[x] = matrix[x] * value
    return matrix

def apply_kernel(matrix, kernel):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = list(matrix[i][j])
            for index in range(len(matrix[i][j])):
                matrix[i][j][index] *= kernel[i][j]
            matrix[i][j] = tuple(matrix[i][j])
    return matrix

def sum_matrix(matrix_arr):
    res = []
    for line in matrix_arr[0]:
        res.append(0)
    for arr in matrix_arr:
        for value in arr:
            for index in range(len(value)):
                res[index] += value[index]
    return res

def get_pixels_in_range(pixels, x, y):
    return [
        [pixels[x - 1, y - 1], pixels[x, y - 1], pixels[x + 1, y - 1]],
        [pixels[x - 1, y], pixels[x, y], pixels[x + 1, y]],
        [pixels[x - 1, y + 1], pixels[x, y + 1], pixels[x + 1, y + 1]]
    ]

matrix = [
        [(1, 2, 3), (1, 2, 3), (1, 2, 3)],
        [(1, 2, 3), (1, 2, 3), (1, 2, 3)],
        [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
    ]
kernel = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

image = im.open('pic.png')
print("scale: " + str(image.size))
image = grey_scale_image(image)
image.save('new_image.png')