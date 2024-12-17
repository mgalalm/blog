import os
title = input("Title: ")
# lower case remove spaces and replace with dashes, remove special characters
title = "".join([c if c.isalnum() else "-" for c in title]).lower()

# replace multiple spaces between words with a single dash
while "--" in title:
    title = title.replace("--", "-")
# remove leading and trailing dashes
title = title.strip("-")


# title = title.replace(" ", "-")

# while "--" in title:
#     title = title.replace("--", "-")
# title = title.replace(" ", "-") /

# title = title.lower().replace(" ", "-")
# loop over the folders in the content directory and let the user select one
folders = [f for f in os.listdir("content") if os.path.isdir(os.path.join("content", f))]
for i, folder in enumerate(folders):
    print(f"{i+1}. {folder}")
folder = folders[int(input("Select folder: "))-1]
# create the new post file
filename = os.path.join("content", folder, f"{title}.md")
print(filename)

# use hugo new content to create the new post

os.system(f"hugo new \"{filename}\"")
