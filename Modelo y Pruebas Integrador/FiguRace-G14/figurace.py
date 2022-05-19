import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.join(dir_path,"."))
print(os.getcwd())

