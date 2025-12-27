import math
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QListWidgetItem
from FileOperator import FileOperator
from main_layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle("Lista do zrobienia")
        self.fileoperator = FileOperator()
        self.load_data()
        self.tuple_of_checkBox_statuses = {'done': False, 'draft': False, 'main': True}
        self.ui.add_button.clicked.connect(self.add_to_list)
        self.ui.delete_button.clicked.connect(self.delete_from_lists)
        self.ui.check_box_done_list.clicked.connect(self.check_box_changed)
        self.ui.check_box_draft_list.clicked.connect(self.check_box_changed)
        self.ui.check_box_main_list.clicked.connect(self.check_box_changed)
        self.ui.save_to_file_button.clicked.connect(self.safe_to_file)
        self.ui.calculate_button.clicked.connect(self.calculate_bmi)

    def prepare_data_for_json(self):
        list_widgets = [
                self.ui.done_list,
                self.ui.draft_list,
                self.ui.main_list
            ]
        list_names = [
            'done',
            'draft',
            'main'
        ]
        names_counter = 0
        dict_for_json = {}
        for list_widget in list_widgets:
            list_of_items_str = []
            items_count = list_widget.count()
            if items_count == 0:
                break
            for i in range(items_count):
                current_item = list_widget.item(i)
                list_of_items_str.append(current_item.text())
            dict_for_json[list_names[names_counter]] = list_of_items_str
            names_counter +=1
        return dict_for_json

    def safe_to_file(self):
        data = self.prepare_data_for_json()
        self.fileoperator.save_data(data)

    def delete_from_lists(self):
            list_widgets = [
                self.ui.done_list,
                self.ui.draft_list,
                self.ui.main_list
            ]
            
            total_deleted = 0
            
            for list_widget in list_widgets:
                selected_items = list_widget.selectedItems()
                
                for item in selected_items:
                    row = list_widget.row(item)
                    list_widget.takeItem(row) 
                    total_deleted += 1
                list_widget.clearSelection()
            return total_deleted
    
    def add_to_list(self):
        text_to_add = self.ui.textEdit.toPlainText()
        text_to_add = text_to_add.capitalize()
        if self.tuple_of_checkBox_statuses['main']:
            self.add_to_main_list(text_to_add)
        if self.tuple_of_checkBox_statuses['done']:
            self.add_to_done_list(text_to_add)
        if self.tuple_of_checkBox_statuses['draft']:
            self.add_to_draft_list(text_to_add)

    def add_to_main_list(self, text_to_add):
        main_list = self.ui.main_list
        main_list.addItem(QListWidgetItem(text_to_add))

    def add_to_draft_list(self, text_to_add):
        draft_list = self.ui.draft_list
        draft_list.addItem(QListWidgetItem(text_to_add))

    def add_to_done_list(self, text_to_add):
        done_list = self.ui.done_list
        done_list.addItem(QListWidgetItem(text_to_add))
        

    def check_box_changed(self):
        checkbox_tuple = {
            'done': self.ui.check_box_done_list,
            'draft': self.ui.check_box_draft_list,
            'main': self.ui.check_box_main_list,
        }
        
        for key, checkbox_widget in checkbox_tuple.items():
            self.tuple_of_checkBox_statuses[key] = checkbox_widget.isChecked()

    def load_data(self):
        data = self.fileoperator.read_data()
        if data != {}:
            for list_name in data:
                if list_name == 'done':
                    for value in data[list_name]:
                        if value == "":
                            continue
                        self.add_to_done_list(value)
                elif list_name == 'draft':
                    for value in data[list_name]:
                        if value == "":
                            continue
                        self.add_to_draft_list(value)
                elif list_name == 'main':
                    for value in data[list_name]:
                        if value == "":
                            continue
                        self.add_to_main_list(value)

    def calculate_bmi(self):
        height_cm = self.ui.height_spin_box.value()
        weight = self.ui.weight_spin_box.value()
        bmi_label = self.ui.bmi_value_label
    
        height_m = height_cm / 100
        bmi = weight / math.pow(height_m, 2)
        bmi = round(bmi, 2)
        bmi_label.setText(f"Twoje BMI wynosi: {bmi}")
        return bmi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec())
    