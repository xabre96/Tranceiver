import base64

with open("resc/receipt.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print str


# Output:
#
# iVBORw0KGgoAAAANSUhEUgAAAuAAAACFCAIAAACVGtqeAAAAA3
# NCSVQICAjb4U/gAAAAGXRFWHRTb2Z0d2FyZQBnbm9tZS1zY3Jl
# ZW5zaG907wO/PgAAIABJREFUeJzsnXc81d8fx9+fe695rYwIaa
# ...
#
#
fh = open("resc/imageToSave.png", "wb")
fh.write(str.decode('base64'))
fh.close()