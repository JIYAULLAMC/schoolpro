import os
import sys

def rm_mig_cache(dir, arg):
    if arg == "mig":
        for dirpath, dirnames, filenames in os.walk(dir):
            for dirname in dirnames:
                if dirname == 'migrations':
                    migrations_dir = os.path.join(dirpath, dirname)
                    for filename in os.listdir(migrations_dir):
                        if  filename != "__init__.py" and filename.endswith(".py"):
                            file_path = os.path.join(migrations_dir, filename)
                            os.remove(file_path)
        print("---------- all migrations removed ----------")

    if arg == "cache":
        for dirpath, dirnames, filenames in os.walk(dir):
            for dirname in dirnames:
                if dirname == '__pycache__':
                    migrations_dir = os.path.join(dirpath, dirname)
                    for filename in os.listdir(migrations_dir):
                        if filename.endswith(".pyc"):
                            file_path = os.path.join(migrations_dir, filename)
                            os.remove(file_path)
        print("---------- all cache removed ----------")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(1)

    argument = sys.argv[1]
    directory = os.getcwd()
    rm_mig_cache(directory, argument)

