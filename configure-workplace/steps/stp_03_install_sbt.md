# Настройка sbt

Вызвать команду:
```console
sbt new
```
Вывод команды:
```bash
Welcome to sbt new!
Here are some templates to get started:
 a) scala/toolkit.local               - Scala Toolkit (beta) by Scala Center and VirtusLab
 b) typelevel/toolkit.local           - Toolkit to start building Typelevel app
 c) sbt/cross-platform.local          - A cross-JVM/JS/Native project
 d) scala/scala3.g8                   - Scala 3 seed template
 e) scala/scala-seed.g8               - Scala 2 seed template
 f) playframework/play-scala-seed.g8  - A Play project in Scala
 g) playframework/play-java-seed.g8   - A Play project in Java
 i) softwaremill/tapir.g8             - A tapir project using Netty
 m) scala-js/vite.g8                  - A Scala.JS + Vite project
 n) holdenk/sparkProjectTemplate.g8   - A Scala Spark project
 o) spotify/scio.g8                   - A Scio project
 p) disneystreaming/smithy4s.g8       - A Smithy4s project
 q) quit
```
Выбрать конфигурацию:  
https://mvnrepository.com/artifact/org.scala-lang/toolkit  
```bash
Select a template: a
Scala version (default: 3.3.4): 2.13.17
Scala Toolkit version (default: 0.5.0): 0.6.0
```
Далее, после успешного запуска sbt - необходимо завершить его
```sbt
sbt:user> exit
```
## Проверка версии:
```console
sbt -version
# sbt version in this project: 1.12.9
# sbt runner version: 1.12.9
```
## Проверка запуска:
```console
sbt 
# [info] welcome to sbt 1.12.9 (Ubuntu Java 17.0.18)
# [info] loading project definition from /home/user/project
# [info] loading settings for project user from build.sbt...
# [info] set current project to user (in build file:/home/user/)
```
После успешного старта - вводим **exit**
```sbt
sbt:user> exit
```
