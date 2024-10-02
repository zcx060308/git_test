import os
def visit_dir(test_dir):
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


if __name__ == '__main__':
    visit_dir("D:\PycharmProjects")