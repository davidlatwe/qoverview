
from Qt5 import QtWidgets, QtGui
from qoverview import VerticalExtendedTreeView


class Example(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Example, self).__init__(parent=parent)

        widgets = {
            "view": VerticalExtendedTreeView(),
        }
        widgets["view"].setHeaderHidden(True)
        widgets["view"].setAlternatingRowColors(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(widgets["view"])

        self._widgets = widgets

        self.setStyleSheet(stylesheet)
        self.mock()

    def mock(self):
        data = [
            ("A", []),
            ("B", ["bar"]),
            ("C", []),
            ("D", ["david", "devy", "deep"]),
            ("E", []),
            ("F", ["foo"]),
        ]

        model = QtGui.QStandardItemModel()
        root = model.invisibleRootItem()

        for name, children in data:
            item = QtGui.QStandardItem(name)
            for child in children:
                item.appendRow(QtGui.QStandardItem(child))
            root.appendRow(item)

        self._widgets["view"].setModel(model)


stylesheet = """
* {
    outline: none;
    color: #A49884;
    background-color: #262626;
}
QAbstractItemView {
    alternate-background-color: #212121;
    selection-color: #212121;
    selection-background-color: #826138;
}
QAbstractItemView::item{
    padding: 5px 1px;
    border: 0px;
}
QAbstractItemView::item:selected:active,
QAbstractItemView::item:selected:!focus {
    background-color: #826138;
}
"""


if __name__ == "__main__":
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    view = Example()
    view.show()
    app.exec_()
