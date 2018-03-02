from word_count import word_count

root_path = "./resource/"
file_list = ["Alice in Wonderland.txt", "Little Women.txt", "Siddhartha.txt","yamade.txt"]
for fileName in file_list:
    word_count(root_path+fileName)
