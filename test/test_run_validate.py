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
            tf_in.extractall("precom")
        with open("precom/run.txt", "r") as txt_in:
            run = txt_in.read()
    return run


def test_validate():
    run = read_run()
    a = validator(run, k=1000)
    os.remove("precom/run.txt")
    assert len(a) == 0
