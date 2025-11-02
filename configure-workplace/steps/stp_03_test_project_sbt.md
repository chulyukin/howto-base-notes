# Тестовый проект SBT
Создать директорию проекта, файл сборки проекта и файл программы
```console
mkdir -p ~/SBTProjects
mkdir -p ~/SBTProjects/sbt_test_project
cd ~/SBTProjects/sbt_test_project
```
**Файл build.sbt:**  
```console
nano build.sbt
```
Ввести в файл build.sbt следующие строки:
```sbt
name := "HelloSBT"
version := "1.0"
scalaVersion := "2.13.16"
```
**Файл HelloSBT.scala:**
```console
nano HelloSBT.scala
```
Ввести в файл HelloSBT.scala следующие строки:
```scala
object HelloSBT extends App {
    println("Hello SBT!")
}
```
Собрать проект и запустить
```sbt
sbt run
```
Будет произведена сборка, создан исполняемый файл **hellosbt_2.13-1.0.jar** (по пути  ~/SBTProjects/sbt_test_project/target/scala-2.13/),а так же будет произведен запуск файла и вывод строки: "Hello SBT!"
```sbt
[info] welcome to sbt 1.11.7 (Ubuntu Java 17.0.17-ea)
[info] loading project definition from /home/user/SBTProjects/sbt_test_project/project
[info] loading settings for project sbt_test_project from build.sbt...
[info] set current project to HelloSBT (in build file:/home/user/SBTProjects/sbt_test_project/)
[info] compiling 1 Scala source to /home/user/SBTProjects/sbt_test_project/target/scala-2.13/classes ...
[info]   Compilation completed in 6.397s.
[info] running HelloSBT 
Hello SBT!
[success] Total time: 2 s, completed 2 нояб. 2025 г., 16:34:53
```
Так же можно воспользоваться интерактивным режимом
```console
sbt
# [info] welcome to sbt 1.11.7 (Ubuntu Java 17.0.17-ea)
# [info] loading project definition from /home/user/SBTProjects/sbt_test_project/project
# [info] loading settings for project sbt_test_project from build.sbt...
# [info] set current project to HelloSBT (in build file:/home/user/SBTProjects/sbt_test_project/)
# ...
# [info] started sbt server
```
Далее ввести команду **run** (по окончании исполнении -  **exit**)
```sbt
sbt:HelloSBT> run
[info] running HelloSBT 
Hello SBT!
[success] Total time: 2 s, completed 2 нояб. 2025 г., 16:40:46
```
```sbt
sbt:HelloSBT> exit
[info] shutting down sbt server
```
Запустить собранный **.jar** файл можно следующим образом
```console
scala ~/SBTProjects/sbt_test_project/target/scala-2.13/hellosbt_2.13-1.0.jar
# Hello SBT!
```
