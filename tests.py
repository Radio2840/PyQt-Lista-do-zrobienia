import pytest
from unittest.mock import MagicMock
from main import MyForm

@pytest.fixture
def app(qtbot):
    obj = MyForm()
    obj.ui = MagicMock()
    obj.fileoperator = MagicMock()
    obj.tuple_of_checkBox_statuses = {}
    qtbot.addWidget(obj)
    return obj

def test_message_calculate_bmi(app):
    app.ui.height_spin_box.value.return_value = 180
    app.ui.weight_spin_box.value.return_value = 81
    app.calculate_bmi()
    app.ui.bmi_value_label.setText.assert_called_with("Twoje BMI wynosi: 25.0")

def test_value_calculate_bmi(app):
    app.ui.height_spin_box.value.return_value = 180
    app.ui.weight_spin_box.value.return_value = 81
    bmi = app.calculate_bmi()
    assert bmi == 25

def test_fail_value_calculate_bmi(app):
    app.ui.height_spin_box.value.return_value = 181
    app.ui.weight_spin_box.value.return_value = 81
    bmi = app.calculate_bmi()
    assert bmi != 25

def test_prepare_data_for_json(app):
    mock_list = MagicMock()
    mock_list.count.return_value = 1
    mock_list.item(0).text.return_value = "Test"
    app.ui.done_list = app.ui.draft_list = app.ui.main_list = mock_list
    
    result = app.prepare_data_for_json()
    assert result['done'] == ["Test"]
    assert len(result) == 3

def test_delete_from_lists(app):
    mock_list = MagicMock()
    mock_item = MagicMock()
    mock_list.selectedItems.return_value = [mock_item]
    mock_list.row.return_value = 0
    app.ui.done_list = app.ui.draft_list = app.ui.main_list = mock_list
    
    assert app.delete_from_lists() == 3

def test_add_to_list_logic(app):
    app.ui.textEdit.toPlainText.return_value = "zadanie"
    app.tuple_of_checkBox_statuses = {'main': True, 'done': False, 'draft': False}
    app.add_to_main_list = MagicMock()
    
    app.add_to_list()
    app.add_to_main_list.assert_called_with("Zadanie")

def test_check_box_changed(app):
    app.ui.check_box_done_list.isChecked.return_value = True
    app.ui.check_box_draft_list.isChecked.return_value = False
    app.ui.check_box_main_list.isChecked.return_value = True
    
    app.check_box_changed()
    assert app.tuple_of_checkBox_statuses['done'] is True
    assert app.tuple_of_checkBox_statuses['draft'] is False