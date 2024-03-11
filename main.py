# git-scm.com
# git init #инициализация гита в проекте
# git config --global user.name "Name" #устанавливаем глобольно имя
# git config --global user.name #чтоб посмотреть имя
# git config --global user.email "Name" #устанавливаем глобольно email
# git config --global user.name #чтоб посмотреть email
# git add * # добавить в список очикування на додання в локальний репозиторий все
# git add */*.txt # добавить в список очикування на додання всі файли в будьяких папках з розширенням txt
# git add . #додати в чергу все що е
# git status #подивитись в якаму статусі яки файли знайходятся
# git rm --cached <file_name> # удалить файл з черги очикування на додання
# git rm --cached -r . # удалить з черги на очикування всі файли і папки що там е
# git commit -m "first version of project" #завантаження на локальний репозиторий того що було в черзі
# .gitignore #файл для игнорирования
# git reset --soft HEAD~1 #откат на попередню версію
# --soft # перейти на вибрану версію зі зміною вмисту файлів
# git reflog #подивитись всі дії і їх id
# git reset --soft 618b726 #перейти на версію з даним id
# git reset --hard HEAD~1 # перейти на попередню версію зі зміною вмисту файлів
# --hard # перейти на вибрану версію зі зміною вмисту файлів
# git reset --hard 618b726 # повернення на версію з вказаним id в hard режимі - зі зміною вмісту файлів
# git reflog
# git branch <branch_name> #створюеться нова гилка
# git checkout <branch_name> #переходимо у вказану гилку
# git checkout master #перехід на головну гилку
# git branch -d <branch_name> #удалить вказану гилку
# git merge forum #зьеднання гилки з мастер=гилкою
# git remote add origin https://github.com/MichaelNest/Git_Lesson.git #підключення до удаленного репозіторія GitHub
# git remote #подивитись до якого удаленного репозіторія підключено - до репозіторія на імя origin
# git remote remove origin #відключитися від удаленного репозіторія на імя origin
# git push -u origin master #залівка локального репозіторія на удаленний
# git clone https://github.com/MichaelNest/Git_Lesson.git # клонировать проект до себе
#
