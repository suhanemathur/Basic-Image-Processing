from pdf2image import convert_from_path

#to extract all the images and store them in pages array
pdf_file = "19032019107327.pdf"
pfile=pdf_file.split(".")
pages = convert_from_path(pdf_file, poppler_path = r"C:/Users/acer/Desktop/poppler-0.68.0/bin")

#p is the desired page we want from the pdf
p=30
pp=p-1
pages[pp].save(r'output'+str(p)+ pfile[0]+".jpg", 'JPEG')

# TASK- to extract all the pages from the file, save it as images and crop to get the middle part

from pdf2image import convert_from_path
pdf_file="01012021100742.pdf"
pages=convert_from_path(pdf_file, poppler_path="C:/Users/acer/Desktop/poppler-0.68.0/bin")
#all pages saved in a page list

#getting the dimensions pf the page
(height, width) = pages[1].size
print(height)
print(width)

crop_width = 1000  # The desired width of the cropped portion
crop_height = 1400  # The desired height of the cropped portion

#setting rop dimensions
left = (width - crop_width) // 2
top = (height - crop_height) // 2
right = left + crop_width
bottom = top + crop_height
pagesout=[]
#looping over all the images and performing image operations
for pg,img in enumerate(pages):
    im = pages[pg].crop((left, top, right, bottom))
    print(im.size)
    pagesout.append(im)
# im[0].save("outputcropped.pdf",pdf)

#same task using threading 

from pdf2image import convert_from_path
from threading import Thread

def crop_and_save_image(img, image_number):
    # Getting the dimensions of the page
    (height, width) = img.size

    # Setting crop dimensions
    crop_width = 1000  # The desired width of the cropped portion
    crop_height = 1400  # The desired height of the cropped portion
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height

    # Cropping and saving the image
    cropped_image = img.crop((left, top, right, bottom))
    # cropped_image.save("cropped_image{}.jpg".format(image_number), "JPEG")
    return cropped_image

def process_pages(pages):
    # Create a list to hold the threads
    threads = []

    # Process each page in a separate thread
    for pg, img in enumerate(pages):
        thread = Thread(target=crop_and_save_image, args=(img, pg + 1))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Convert PDF to images
pdf_file = "01012021100742.pdf"
pages = convert_from_path(pdf_file, poppler_path="C:/Users/acer/Desktop/poppler-0.68.0/bin")

# Process pages concurrently
process_pages(pages)

#using threaading when fn is not saving any image and returning it instead

from pdf2image import convert_from_path
from threading import Thread

def crop_and_save_image(img, image_number):
    # Getting the dimensions of the page
    (height, width) = img.size

    # Setting crop dimensions
    crop_width = 1000  # The desired width of the cropped portion
    crop_height = 1400  # The desired height of the cropped portion
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height

    # Cropping and saving the image
    cropped_image = img.crop((left, top, right, bottom))
    # cropped_image.save("cropped_image{}.jpg".format(image_number), "JPEG")
    return cropped_image

def process_pages(pages):
    # Create a list to hold the cropped images
    cropped_images = []

    # Create a list to hold the threads
    threads = []

    # Process each page in a separate thread
    for pg, img in enumerate(pages):
        thread = Thread(target=lambda: cropped_images.append(crop_and_save_image(img, pg + 1)))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return cropped_images

# Convert PDF to images
pdf_file = "01012021100742.pdf"
pages = convert_from_path(pdf_file, poppler_path="C:/Users/acer/Desktop/poppler-0.68.0/bin")

# Process pages concurrently and get the cropped images
cropped_images = process_pages(pages)

# Access the cropped images for further processing or display
# Example: Save the cropped images to disk
for image_number, image in enumerate(cropped_images):
    image.save("cropped_image{}.jpg".format(image_number + 1), "JPEG")

