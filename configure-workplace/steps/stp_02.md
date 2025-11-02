# Шаг 2. Установка Scala 2.13.16 

Установить scala версии 2.13.16 можно 2-мя способами

**Вариант 1:** загрузить вручную с сайта https://www.scala-lang.org/download/2.13.16.html  

**Вариант 2:** выполнить команду
```console
sudo wget http://scala-lang.org/files/archive/scala-2.13.16.deb
```

Установка:
```console
sudo dpkg -i scala-2.13.16.deb
```
Проверка версии:
```console
scala -version
# Scala code runner version 2.13.16 -- Copyright 2002-2025, LAMP/EPFL and Lightbend, Inc. dba Akka
```
Проверка запуска:
```console
scala
# Welcome to Scala 2.13.16 (OpenJDK 64-Bit Server VM, Java 17.0.17-ea).
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
