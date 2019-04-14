import os


def scandir(target):
    bag_file = []
    for i in os.listdir(target):
        full_path = os.path.join(target, i)
        if not os.access(full_path, os.R_OK):
            continue
        if i[-4:] == '.bag':
            bag_file.append(full_path)
        elif os.path.isdir(full_path):
            bag_file += scandir(full_path)
    return bag_file


if __name__ == "__main__":
    for i in scandir('/home/shayennn'):
        print(i)
