# Шаг 2. Установка Scala 2.12.20 

Установить scala версии 2.12.20 можно 2-мя способами

**Вариант 1:** загрузить вручную с сайта https://www.scala-lang.org/download/2.12.20.html  

**Вариант 2:** выполнить команду
```console
sudo wget http://scala-lang.org/files/archive/scala-2.12.20.deb
```

Установка:
```console
sudo dpkg -i scala-2.12.20.deb
```
Проверка версии:
```console
scala -version
# Scala code runner version 2.12.20 -- Copyright 2002-2024, LAMP/EPFL and Lightbend, Inc.
```
Проверка запуска:
```console
scala
# Welcome to Scala 2.12.20 (OpenJDK 64-Bit Server VM, Java 17.0.15).
# Type in expressions for evaluation. Or try :help.
```
```scala
scala> val s = "Hello Scala!"
s: String = Hello Scala!

scala> println(s)
Hello Scala!
// Выход
scala> :q
```
