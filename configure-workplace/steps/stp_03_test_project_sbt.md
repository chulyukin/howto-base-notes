# Тестовый проект SBT
Создать директорию проекта, файл сборки проекта и файл программы
```console
mkdir ~/SBTProjects
mkdir ~/SBTProjects/sbt_test_project
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
scalaVersion := "2.12.20"
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
Будет произведена сборка, создан исполняемый файл **hellosbt_2.12-1.0.jar** (по пути  ~/SBTProjects/sbt_test_project/target/scala-2.12/),а так же будет произведен запуск файла и вывод строки: "Hello SBT!"
```sbt
[info] Updated file /home/user/SBTProjects/sbt_test_project/project/build.properties: set sbt.version to 1.11.2
[info] welcome to sbt 1.11.2 (Ubuntu Java 17.0.15)
[info] loading project definition from /home/user/SBTProjects/sbt_test_project/project
[info] loading settings for project sbt_test_project from build.sbt...
[info] set current project to HelloSBT (in build file:/home/user/SBTProjects/sbt_test_project/)
[info] compiling 1 Scala source to /home/user/SBTProjects/sbt_test_project/target/scala-2.12/classes ...
https://repo1.maven.org/maven2/org/scala-sbt/util-interface/1.10.7/util-interface…
  100,0% [##########] 4,3 KiB (71,1 KiB / s)
[info] Non-compiled module 'compiler-bridge_2.12' for Scala 2.12.20. Compiling...
[info]   Compilation completed in 6.397s.
[info] running HelloSBT 
Hello SBT!
[success] Total time: 8 s, completed 28 июн. 2025 г., 08:28:50
```
Так же можно воспользоваться интерактивным режимом
```console
sbt
# [info] welcome to sbt 1.11.2 (Ubuntu Java 17.0.15)
# [info] loading project definition from /home/user/SBTProjects/sbt_test_project/project
# [info] loading settings for project sbt_test_project from build.sbt...
# [info] set current project to HelloSBT (in build file:/home/user/SBTProjects/sbt_test_project/)
# [info] sbt server started at local:///home/user/.sbt/1.0/server/86f76a119b15197de980/sock
# [info] started sbt server
```
Далее ввести команду **run** (по окончании исполнении -  **exit**)
```sbt
sbt:HelloSBT> run
[info] running HelloSBT 
Hello SBT!
[success] Total time: 0 s, completed 28 июн. 2025 г., 08:30:11
```
```sbt
sbt:HelloSBT> exit
[info] shutting down sbt server
```
Запустить собранный **.jar** файл можно следующим образом
```console
scala ~/SBTProjects/sbt_test_project/target/scala-2.12/hellosbt_2.12-1.0.jar
# Hello SBT!
```
