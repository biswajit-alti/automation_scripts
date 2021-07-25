import fitz
import re
import os


def pdf2pic(path, pic_path):
    '''
         # Extract pictures from pdf
         :param path: pdf path
         :param pic_path: The path where the picture is saved
    :return:
    '''
    # Open pdf
    doc = fitz.open(path)
    nums = doc.xref_length()
    imgcount = 0  # Image count

    # Traverse every object
    for i in range(1, nums):
        text = doc.xref_object(i)
        # print(i, text)
        # Filter useless pictures
        if ('Width 2550' in text) and ('Height 3300' in text) or ('thumbnail' in text):
            continue

            # Use regular expressions to find pictures
        checkXO = r"/Type(?= */XObject)"
        checkIM = r"/Subtype(?= */Image)"

        isXObject = re.search(checkXO, text)
        isImage = re.search(checkIM, text)

        # Does not meet the conditions, continue
        if not isXObject or not isImage:
            continue
        print(i)
        pix = fitz.Pixmap(doc, i)
        imgcount += 1
        # Generate image
        # Save image name
        img_name = "img{}.png".format(imgcount)

        # If pix.n<5, you can directly save as PNG
        if pix.n < 5:
            try:
                pix.writePNG(os.path.join(pic_path, img_name))
                pix = None
            except:
                pix0 = fitz.Pixmap(fitz.csRGB, pix)
                pix0.writePNG(os.path.join(pic_path, img_name))
                pix0 = None

if __name__ == '__main__':
    # pdf path
    path = r'/Users/biswajitmohapatra/Downloads/test.pdf'
    # Saved image path
    pic_path = '/Users/biswajitmohapatra/Desktop/biswa'
    pdf2pic(path, pic_path)


# import fitz
# file = '/Users/biswajitmohapatra/Downloads/test.pdf'
# doc = fitz.open(file)
# # print(dir(doc))
# nums = doc.xref_length()
# # print(nums)
# for i in range(1, nums):
#     # Define object string
#     text = doc.xref_object(i)
#     print(i, text)
#     if ('Width 2550' in text) and ('Height 3300' in text) or ('thumbnail' in text):
#         continue
