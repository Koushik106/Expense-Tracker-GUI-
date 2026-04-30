from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QApplication,
    QMessageBox,
    QPlainTextEdit,
    QFileDialog,
)

import json
import csv
from datetime import date
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QDoubleValidator
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


icon = resource_path("expenses.ico")


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 300)
        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle("Expense Tracker")
        self.label_welcome = QLabel("Howdy Buddy !\nWhat do you want to do ?")
        self.button_add_expenses = QPushButton("Add Expenses")
        self.button_view_expenses = QPushButton("View All Expenses(Json)")
        self.button_total_expenses_for_the_month = QPushButton(
            "Total Expenses for the Month"
        )
        self.button_export_csv = QPushButton("Export to CSV")

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_welcome)
        vbox.addWidget(self.button_add_expenses)
        vbox.addWidget(self.button_view_expenses)
        vbox.addWidget(self.button_total_expenses_for_the_month)
        vbox.addWidget(self.button_export_csv)

        self.setLayout(vbox)

        self.setObjectName("main_window")
        self.button_add_expenses.setObjectName("button_add_expenses")
        self.button_view_expenses.setObjectName("button_view_expenses")
        self.button_export_csv.setObjectName("button_export_csv")
        self.button_total_expenses_for_the_month.setObjectName(
            "button_total_expenses_for_the_month"
        )
        self.setAttribute(Qt.WA_StyledBackground, True)

        # css
        self.setStyleSheet("""
            QWidget#main_window{
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #2c3e50,
                    stop:1 #4ca1af
                )}

            QPushButton#button_add_expenses{
            background-color: hsl(113, 73%, 57%);
            font-weight: bold;
            border-radius: 20px;
            padding: 5px;
            border: 6px solid black;}

            QPushButton#button_view_expenses{
            background-color: hsl(42, 73%, 57%);
            font-weight: bold;
            border-radius: 20px;
            padding: 5px;
            border: 6px solid black;}

            QPushButton#button_export_csv{
            background-color: hsl(174, 73%, 57%);
            font-weight: bold;
            border-radius: 20px;
            padding: 5px;
            border: 6px solid black;}

            QPushButton#button_total_expenses_for_the_month{
            background-color: hsl(303, 73%, 57%);
            font-weight: bold;
            border-radius: 20px;
            padding: 5px;
            border: 6px solid black;}

            
            QPushButton#button_add_expenses:hover{
                background-color: hsl(113, 90%, 73%);
            }
            QPushButton#button_view_expenses:hover{
                background-color: hsl(42, 90%, 73%);
            }
            QPushButton#button_export_csv:hover{
                background-color: hsl(174, 90%, 73%);
            }
            QPushButton#button_total_expenses_for_the_month:hover{
                background-color: hsl(303, 90%, 73%);
            }

            """)

        # Clicking buttons
        self.button_add_expenses.clicked.connect(self.add_expenses)

        self.button_total_expenses_for_the_month.clicked.connect(self.total_expense)
        self.button_view_expenses.clicked.connect(self.view_expense)
        self.button_export_csv.clicked.connect(self.export_csv)
        self.geo()

    def add_expenses(self):
        self.add_window = Add_expense()
        self.add_window.show()

    def view_expense(self):
        self.add_window = View_expense()
        self.add_window.show()

    def total_expense(self):
        self.add_window = Total_expenses_for_the_month()
        self.add_window.show()

    def export_csv(self):
        json_file = "Expense Record.json"
        try:
            with open(json_file, "r", encoding="utf-8") as file:
                data = json.load(file)
            if not data:
                QMessageBox.information(self, "No Data", "No expenses to export.")
                return

            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save CSV File",
                "expenses.csv",
                "CSV Files (*.csv)",
            )
            if not file_path:
                return
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["Category", "Description", "Amount", "Recording time"],
                )
                writer.writeheader()
                writer.writerows(data)
            QMessageBox.information(
                self, "Success", f"Exported successfully to:\n{file_path}"
            )
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "Expense file not found.")
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Error", "JSON file is corrupted.")

    def geo(self):
        self.label_welcome.setFont(QFont("times new roman", 50))
        self.label_welcome.setAlignment(Qt.AlignHCenter)
        self.button_export_csv.setFont(QFont("roboto", 20))
        self.button_total_expenses_for_the_month.setFont(QFont("roboto", 20))
        self.button_view_expenses.setFont(QFont("roboto", 20))
        self.button_add_expenses.setFont(QFont("roboto", 20))


class Add_expense(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 300)
        self.setWindowTitle("Adding Expenses")
        self.setWindowIcon(QIcon(icon))

        vbox = QVBoxLayout()
        self.input_category = QLineEdit()
        self.input_category.setPlaceholderText("Category...")
        self.input_description = QLineEdit()
        self.input_description.setPlaceholderText("Discription...")
        self.input_amount = QLineEdit()
        self.input_amount.setPlaceholderText("Amount...")
        self.input_amount.setValidator(QDoubleValidator())
        self.back_button = QPushButton("Back")
        self.save_button = QPushButton("Save")

        vbox.addWidget(self.input_category)
        vbox.addWidget(self.input_description)
        vbox.addWidget(self.input_amount)
        vbox.addWidget(self.back_button)
        vbox.addWidget(self.save_button)
        self.setLayout(vbox)

        # css
        self.back_button.setObjectName("back_button")
        self.save_button.setObjectName("save_button")
        self.setObjectName("add_window")
        self.input_category.setObjectName("input_category")
        self.input_description.setObjectName("input_description")
        self.input_amount.setObjectName("input_amount")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
            QWidget#add_window{
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #2c3e50,
                stop:1 #4ca1af
            )}
            QPushButton#back_button{
                background-color:hsl(197, 45%, 27%);
                font-size: 30px;
                font-family: geogeria;
                font-weight: bold;
                border-radius: 20px;
                padding: 5px;
                border: 6px solid black;
            }
            QPushButton#save_button{
                background-color:hsl(145, 45%, 27%);
                font-size: 30px;
                font-family: geogeria;
                font-weight: bold;
                border-radius: 20px;
                padding: 5px;
                border: 6px solid black;
            }
            QPushButton#back_button:hover{
                background-color:hsl(197, 45%, 37%);
            }
            QPushButton#save_button:hover{
                background-color:hsl(145, 45%, 37%)
            }
            QLineEdit#input_category{
                background-color: hsl(145, 14%, 76%);
                font-size: 30px;
                font-family: geogeria;
            }
            QLineEdit#input_description{
                background-color: hsl(145, 14%, 76%);
                font-size: 30px;
                font-family: geogeria;
            }
            QLineEdit#input_amount{
                background-color: hsl(145, 14%, 76%);
                font-size: 30px;
                font-family: geogeria;
            }
                            
                           """)

        self.back_button.clicked.connect(self.hit_back)
        self.save_button.clicked.connect(self.save)

    def save(self):

        category = self.input_category.text()
        description = self.input_description.text()
        amount_txt = self.input_amount.text()
        recording_time = date.today().strftime("%d/%m/%Y")

        if not amount_txt.strip():
            QMessageBox.warning(
                self, "Input Error", "Please enter an amount before saving."
            )
            return
        try:
            amount = float(amount_txt)
        except ValueError:
            QMessageBox.warning(
                self, "Input Error", "Invalid amount Please check your numbers."
            )
            return

        record = {
            "Category": category,
            "Description": description,
            "Amount": float(amount),
            "Recording time": recording_time,
        }
        file_path = "Expense Record.json"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            content = []
        content.append(record)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(content, file, indent=2)

        QMessageBox.information(
            self, "Success!", "Your expense was saved successfully."
        )
        self.hide()

    def hit_back(self):
        self.hide()


class View_expense(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 300)
        self.setWindowTitle("Viewing Expenses")
        self.setWindowIcon(QIcon(icon))
        self.search = QLineEdit()
        self.search.setPlaceholderText(
            "Search categories, description or date(dd/mm/yyyy)"
        )
        self.search.textChanged.connect(self.j_structure)

        self.back = QPushButton("Back")
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        self.setObjectName("window")
        self.search.setObjectName("search")
        self.back.setObjectName("back")
        self.setAttribute(Qt.WA_StyledBackground, True)

        # main layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.search)
        vbox.addWidget(self.text)
        vbox.addWidget(self.back, alignment=Qt.AlignBottom)

        self.setLayout(vbox)

        # css
        self.setStyleSheet("""
            QWidget#window{ 
                background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #2c3e50,
                stop:1 #4ca1af
            )}

            QLineEdit#search{
                padding: 10px;
                font-family: jetbrains mono;
                font-size: 15px;
                border-radius: 10px;
                border: 2px solid #1a252f;
                background-color: hsl(0, 0%, 88%);
            }
            
            QPlainTextEdit{
                padding:10px;
                font-family: jetbrains mono;
                font-size: 20px;
                border-radius: 10px;
            }
            QPushButton{
                background-color: hsl(197, 45%, 27%);
                font-size: 30px;
                font-family: geogeria;
                font-weight: bold;
                border-radius: 20px;
                padding: 5px;
                border: 6px solid black;
            }

            QPushButton#back:hover{
            background-color: hsl(197, 45%, 37%);
            }""")
        self.j_structure()
        self.back.clicked.connect(self.back_button)

    def back_button(self):
        self.hide()

    def j_structure(self):

        file_path = "Expense Record.json"
        user_search = self.search.text().lower()
        try:
            with open(file_path, "r") as file:
                content = json.load(file)
        except FileNotFoundError:
            self.text.setPlainText("No expenses recorded yet !")
            QMessageBox.information(self, "No Data", "No expense recorded")
            return
        except json.JSONDecodeError:
            self.text.setPlainText("Error: Corrupted Data.")
            QMessageBox.warning(
                self,
                "Data Error",
                "The expense record file is either corrupted or empty.",
            )
            return
        self.text.clear()
        match_found = False
        for i, item in enumerate(content, start=1):
            category = item["Category"].lower()
            description = item["Description"].lower()
            date = item["Recording time"].lower()
            if (
                user_search == ""
                or user_search in category
                or user_search in description
                or user_search in date
            ):
                match_found = True

                text = (
                    f"{i}. Category 🏷️ : {item['Category'].title()}"
                    f"\nDescription 📄 : {"Blank" if item['Description'] =='' else item['Description']}"
                    f"\nAmount 💵 : {item['Amount']}"
                    f"\nDate 📅 : {item['Recording time']}"
                    "\n"
                )
                self.text.appendPlainText(text)
        if not match_found and user_search != "":
            self.text.setPlainText("No matching expenses found.")


class Total_expenses_for_the_month(QWidget):
    symbl = ["*", "-", "#"]

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 300)
        self.setWindowTitle("Total Expenses")
        self.setWindowIcon(QIcon(icon))
        self.date = QLineEdit()
        self.text_display = QPlainTextEdit()
        self.date.setPlaceholderText("Enter the month (1-12)")
        self.back_btn = QPushButton("Back")
        self.check_btn = QPushButton("Check")

        self.text_display.setReadOnly(True)

        self.date.setObjectName("date")
        self.text_display.setObjectName("text_display")
        self.back_btn.setObjectName("back_btn")
        self.check_btn.setObjectName("check_btn")
        self.setObjectName("window")

        self.setAttribute(Qt.WA_StyledBackground, True)
        vbox = QVBoxLayout()
        vbox.addWidget(self.date)
        vbox.addWidget(self.text_display)
        vbox.addWidget(self.check_btn)
        vbox.addWidget(self.back_btn)

        self.setLayout(vbox)

        # css
        self.setStyleSheet("""
            QWidget#window{
                background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #2c3e50,
                stop:1 #4ca1af
            )}

            QLineEdit#date{
                background-color: hsl(0, 0%, 88%);
                font-size: 18;
                font-family: jetbrains mono;
                font-weight: bold;
                padding:10px;
                border-radius: 15px;
                border: 4px solid black;
                }

            QPlainTextEdit#text_display{
                padding:10px;
                border-radius=10px;
                font-family: jetbrains mono;
                font-size: 22;
                font-weight: bold;
            }
            QPushButton#back_btn{
                background-color: hsl(197, 45%, 27%);
                font-size: 30px;
                font-family: geogeria;
                font-weight: bold;
                border-radius: 20px;
                padding: 5px;
                border: 6px solid black;
                }
            QPushButton#back_btn:hover{
                background-color: hsl(197, 45%, 37%);}

            QPushButton#check_btn{
            background-color: hsl(0, 92%, 46%);
            font-size: 30px;
            font-family: geogeria;
            font-weight: bold;
            border-radius: 20px;
            padding: 5px;
            border: 6px solid black;
            }
            QPushButton#check_btn:hover{
                background-color: hsl(0, 82%, 66%)}""")
        self.check_btn.clicked.connect(self.month_total)
        self.back_btn.clicked.connect(self.back)

    def back(self):
        self.hide()

    def month_total(self):
        file_path = "Expense Record.json"
        search = self.date.text()
        try:
            month = int(search)
            month_details = ""
            if month > 12 or month < 1 or month == "":
                QMessageBox.information(
                    self, "Error", "The month cannot be more than 12 or less than 0"
                )
                return
            else:
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = json.load(file)
                        total = 0
                        for i in content:
                            record_month = int(i["Recording time"].split("/")[1])
                            if record_month == month:
                                total += i["Amount"]
                                month_details += (
                                    f"📅 {i['Recording time']} | 💵 {i['Amount']}\n\n"
                                )
                        if total == 0:
                            text = f"No expenses were recorded for the month {month}."
                        else:
                            text = (
                                f"{self.symbl[1]*10} Expense Record {self.symbl[1] *10}"
                                f"\n{month_details}"
                                f""
                                f"\n{self.symbl[2]*34}\n"
                                f"Grand Total: {total}"
                            )
                        self.text_display.setPlainText(text)
                except FileNotFoundError:
                    QMessageBox.warning(self, "Error", "File No Found")
                except json.JSONDecodeError:
                    QMessageBox.warning(self, "Error", "Json file is corrupted")

        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter numbers only")
            return


if __name__ == "__main__":
    # main()
    app = QApplication(sys.argv)

    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
