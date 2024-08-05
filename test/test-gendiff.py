from gendiff.generate_diff import generate_diff
import os


def test_gendiff():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1 = os.path.join(current_dir, 'files', 'test1.json')
    file2 = os.path.join(current_dir, 'files', 'test2.json')
    assert generate_diff(file1, file2) == """{
+ follow: False
- host: github.io
+ host: hexlet.io
+ proxy: 123.234.53.22
  timeout: 50
- type: normal
}"""


def test_gendiff_identical_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file1 = os.path.join(current_dir, 'files', 'test1.json')
    file2 = os.path.join(current_dir, 'files', 'test1.json')
    assert generate_diff(file1, file2) == """{
  host: github.io
  timeout: 50
  type: normal
}"""


def main():
    test_gendiff()
    test_gendiff_identical_files()


if __name__ == '__main__':
    main()
