from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, 
    QListWidgetItem, QLabel, QLineEdit, QPushButton, QMessageBox,
    QDialog, QFormLayout
)
from PyQt6.QtCore import Qt

from app.api.adapters.languages_data_adapter import LanguagesDataAdapter


# =========================================================
# فرم افزودن زبان (داخل همین فایل)
# =========================================================
class AddLanguageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Language")
        self.setFixedSize(400, 200)
        self.setModal(True)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g. English, Persian, French")
        form_layout.addRow("Name:", self.name_input)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("e.g. en, fa, fr (optional)")
        form_layout.addRow("Code:", self.code_input)

        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.save_btn = QPushButton("Save")
        self.save_btn.setFixedHeight(35)
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #107C41;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0B5931;
            }
        """)
        self.save_btn.clicked.connect(self.save_language)

        self.close_btn = QPushButton("Close")
        self.close_btn.setFixedHeight(35)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        self.close_btn.clicked.connect(self.reject)

        button_layout.addStretch()
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.close_btn)

        layout.addLayout(button_layout)

    def save_language(self):
        name = self.name_input.text().strip()
        code = self.code_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Name is required!")
            return

        # ===== ذخیره‌سازی واقعی =====
        try:
            LanguagesDataAdapter.add(
                name=name,
                code=code
            )
            QMessageBox.information(self, "Success", "Language saved successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Save failed: {str(e)}")


# =========================================================
# ویجت لیست زبان‌ها
# =========================================================
class LanguagesListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.languages = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        self.title_label = QLabel("LANGUAGES")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.title_label)

        search_layout = QHBoxLayout()
        search_layout.setSpacing(4)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search languages...")
        self.search_box.textChanged.connect(self.filter_list)

        self.add_button = QPushButton("+")
        self.add_button.setFixedWidth(40)
        self.add_button.setObjectName("addButton")
        self.add_button.clicked.connect(self.add_new_language)

        search_layout.addWidget(self.search_box)
        search_layout.addWidget(self.add_button)
        layout.addLayout(search_layout)

        self.list_widget = QListWidget()
        self.list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        layout.addWidget(self.list_widget)

        self.load_languages_data()

    def load_languages_data(self):
        self.list_widget.clear()

        try:
            self.languages = LanguagesDataAdapter.get_all()

            if not self.languages:
                self.list_widget.addItem("No languages found")
                return

            for language in self.languages:
                item = QListWidgetItem(language.name)
                item.setData(Qt.ItemDataRole.UserRole, language.id)
                self.list_widget.addItem(item)

        except Exception as e:
            self.list_widget.addItem(f"Error: {str(e)}")

    def filter_list(self, text):
        self.list_widget.clear()
        text = text.lower()

        for language in self.languages:
            if language.name.lower().startswith(text):
                item = QListWidgetItem(language.name)
                item.setData(Qt.ItemDataRole.UserRole, language.id)
                self.list_widget.addItem(item)

    def add_new_language(self):
        dialog = AddLanguageDialog(self)
        if dialog.exec():
            self.load_languages_data()
            self.search_box.clear()

    def delete_selected_language(self):
        current_item = self.list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Warning", "Please select a language to delete.")
            return

        language_id = current_item.data(Qt.ItemDataRole.UserRole)
        if not language_id:
            return

        reply = QMessageBox.question(
            self,
            "Delete Language",
            "Are you sure you want to delete this language?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                success = LanguagesDataAdapter.delete(language_id)
                if success:
                    self.load_languages_data()
                    self.search_box.clear()
                else:
                    QMessageBox.warning(
                        self,
                        "Error",
                        "Cannot delete this language. It may be referenced elsewhere."
                    )
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Delete failed: {str(e)}")