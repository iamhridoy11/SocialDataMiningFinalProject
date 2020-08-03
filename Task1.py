# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
from PIL import Image
from numpy import asarray



image = image.imread('dogs.jpeg')




# display the array of pixels as an image
pyplot.imshow(image)
pyplot.show()

# convert image to numpy array
data = asarray(image)

# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)


# # summarize image details 
# print(image2.mode)
# print("Numpy----")
# print(data)

print("Dog's Image Width and Height are: ")
print(image2.size)


def compute_average_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)

img = Image.open('dogs.jpeg')
img = img.resize((50,50))  # Small optimization
average_color = compute_average_image_color(img)
print("The three dominant color of the image RGB is: ")
print(average_color)



# temp=asarray(Image.open('dogs.jpeg'))
# x=temp.shape[0]
# y=temp.shape[1]*temp.shape[2]

# temp.resize((x,y)) # a 2D array
# print("The two dimentional array is: ")
# print(temp)

