from gendiff.generate_diff import generate_diff


def test_gendiff():
    assert generate_diff("/home/georgiy/python-project-50/test/files/test1.json",
                         "/home/georgiy/python-project-50/test/files/test2.json") == """{
+ follow: False
- host: github.io
+ host: hexlet.io
+ proxy: 123.234.53.22
  timeout: 50
- type: normal
}"""


def test_gendiff_identical_files():
    assert generate_diff("/home/georgiy/python-project-50/test/files/test1.json",
                         "/home/georgiy/python-project-50/test/files/test1.json") == """{
  host: github.io
  timeout: 50
  type: normal
}"""


def main():
    test_gendiff()
    test_gendiff_identical_files()


if __name__ == '__main__':
    main()
