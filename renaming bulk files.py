import os

def main():
    i = 0
    path = "C:/Users/a/OneDrive/Desktop/New folder (2)/rename the file/Prof. Anju Goswami/"
    for filename in os.listdir(path):
        my_dest = "ppt" + str(i) + ".pdf"
        my_source = path + filename
        my_dest =path + my_dest
        os.rename (my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()