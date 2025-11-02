# Настройка sbt
_По неизвестным причинам, файл **sbt-launch-....jar** не загружался. Определить, какой нужен файл, можно средствами команды **sbt -version** или **sbt**. Будет выведено сообщение об ошибке, в котором будет имя отсутствующего файла и путь к нему._  
_**Пример:**_  
``` 
cat: /home/user/.cache/sbt/boot/sbt-launch/1.11.7/sbt-launch-1.11.7.jar.sha1: Нет такого файла или каталога
shasum: standard input: no properly formatted SHA checksum lines found
failed to download launcher jar: https://repo1.maven.org/maven2/org/scala-sbt/sbt-launch/1.11.7/sbt-launch-1.11.7.jar (shasum mismatch) 
```

_В этом случае, файл загружается в ручную (в текущем примере это:)_
```console
sudo wget https://repo1.maven.org/maven2/org/scala-sbt/sbt-launch/1.11.7/sbt-launch-1.11.7.jar 
```
_Файл нужно скопировать в папку по пути из сообщения:_
```console
cp sbt-launch-1.11.7.jar ~/.cache/sbt/boot/sbt-launch/1.11.7/sbt-launch-1.11.7.jar
```  
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
Scala version (default: 3.3.4): 2.13.16
Scala Toolkit version (default: 0.5.0): 0.1.9
```
Далее, после успешного запуска sbt - необходимо завершить его
```sbt
sbt:user> exit
```
## Проверка версии:
```console
sbt -version
# sbt version in this project: 1.11.7
# sbt runner version: 1.11.7
```
## Проверка запуска:
```console
sbt 
# [info] welcome to sbt 1.11.7 (Ubuntu Java 17.0.17-ea)
# [info] loading project definition from /home/user/project
# [info] loading settings for project user from build.sbt...
# [info] set current project to user (in build file:/home/user/)
# [info] sbt server started at local:///home/user/.sbt/1.0/server/a6551c9e04f4d49b7473/sock
```
После успешного старта - вводим **exit**
```sbt
sbt:user> exit
```
