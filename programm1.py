import tkinter
from tkinter import *
from settings import * #импортируем настройки
from param import * 

# app = tkinter.Tk() #Создание окна приложения.
app.title(APP_NAME) #указываем название приложения
app.minsize(width = WIDTH, height = HEIGHT)
app.maxsize(width = WIDTH, height = HEIGHT)
# text = tkinter.Text(app, width = WIDTH - 100, height = HEIGHT, wrap='word')#создали поле с текстом
scroll = Scrollbar(app, orient= VERTICAL, command = text.yview)#создали скролл
scroll.pack(side="right", fill="y")#связь между текстом и скроллом
text.configure(yscrollcommand=scroll.set) #разместили скролл
text.pack()#разместили поле с текстом

menuBar = tkinter.Menu(app)#создаем меню

editor = Text_editor()

app_menu = tkinter.Menu(menuBar)

app_menu.add_command(label="Новый", command=editor.new_file)
app_menu.add_command(label="Открыть", command=editor.open_file)
app_menu.add_command(label="Сохранить", command=editor.save_file)
app_menu.add_command(label="Сохранить как", command=editor.save_as_file)

reference = tkinter.Menu(menuBar)
reference.add_command(label="Советы/рекомендации")
reference.add_command(label="Лицензия ппрограммы")
reference.add_command(label="О программе")

menuBar.add_cascade(label="Файл", menu=app_menu)
menuBar.add_cascade(label="Вид")
menuBar.add_cascade(label="Справка", command=editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)

app.config(menu=menuBar)#публикуем в окне

app.mainloop() # бесконечный цикл нашего приложения