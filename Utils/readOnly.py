from PyQt5.QtWidgets import QStyledItemDelegate


class ReadOnlyDelegate(QStyledItemDelegate):
    # deixar tabelas não editáveis
    def createEditor(self, parent, option, index):
        return
