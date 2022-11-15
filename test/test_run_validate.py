from RunValidator import validator
import os
import tarfile


def read_run():
    print(os.getcwd())

    if "rank" in os.listdir('precom'):
        run_tar_path = 'precom/rank/run.tar.gz'
    elif "rec" in os.listdir('precom'):
        run_tar_path = 'precom/rec/datasets/run.tar.gz'

    if run_tar_path.endswith(('.xz', '.gz')):
        with tarfile.open(run_tar_path) as tf_in:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tf_in, "precom")
        with open("precom/run.txt", "r") as txt_in:
            run = txt_in.read()
    return run


def test_validate():
    run = read_run()
    a = validator(run, k=1000)
    os.remove("precom/run.txt")
    assert len(a) == 0
