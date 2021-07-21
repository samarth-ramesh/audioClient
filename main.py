from PySide6 import QtWidgets

from widgets.MainWidget import MainWidget


def main():
    app = QtWidgets.QApplication()
    widget = MainWidget()
    widget.resize(800, 800)
    widget.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
