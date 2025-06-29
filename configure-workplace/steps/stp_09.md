# Шаг 9. Сборка и запуск тестового проекта Spark средствами SBT assembly. 
Описание общего подхода к созданию небольших и средних проектов Scala Apache Spark (сборщик SBT Assembly) представлено на примере демонстрационного проекта **spark-simple-parquet - Демо-проект Scala Spark для сборщика SBT Aassembly . Приложение — конвертер файлов формата parquet в формат csv.**  
Код и описание проекта находится репозитории: https://github.com/chulyukin/spark-simple-parquet .  

Загрузить проект из репозитория
```console
cd ~/SBTProjects
git clone https://github.com/chulyukin/spark-simple-parquet.git
```  
Далее про сборку проекта можно прочитать в README самого проекта.  

## Общие принципы организации аналогичных проектов
Структура проекта:
```tree
.
├── LICENSE
├── .gitignore
├── README.md
├── build.sbt
├── project
│   ├── build.properties
│   └── plugins.sbt
└── src
    └── main
        ├── resources
        │   └── log4j2.properties
        └── scala
            └── com
                └── <директория головного пакета, для примера: example>
                    └── <директория дочернего пакета, для примера: actions>
                        ├── package.scala
                        ├── <Файл пакета 1 для, примера Analitics>.scala
                        ├── <Файл пакета 2, примера Processing>.scala
                        ├── ...
                        ├── <Файл пакета n>.scala
                        └── <Файл Main пакета - точки входа в приложение, для примера: Main>.scala
```

|Файл|Описание|
|:-|:-|
|LICENSE|Лицензия на программное обеспечение в GitHub. Служит, для указания использования, распространения и модификации кода проекта. Лицензия также помогает защитить авторские права и ограничить ответственность. В случае публикации проекта в репозиории github, желательно создать этот файл и заполнить его стандартным образом. |
|.gitignore| Текстовый файл в системе Git для определения игнорируемых файлов и каталогов. Если файлы или директории указаны в .gitignore, Git не будет отслеживать их изменения и добавлять их в индекс или коммиты. Исключает из репозитория файлы, которые не нужны для работы приложения или разработки, такие как личные файлы настроек, временные файлы, конфигурационные, конфиденциальные файлы и т.п. GitHub предоставляет коллекцию шаблонов .gitignore для большинства языков программирования и технологий, которую можно найти в репозитории [gitignore.](https://github.com/github/gitignore)|
|README.md|Файл описания настроек и кода проекта. Файл документации проекта.|  
|build.sbt|Файл для описания настроек сборки проекта. В нём указываются имя, версия, версия Scala, зависимости, настройки компилятора и задачи сборки.|
|project/build.properties|Файл project/build.properties в проектах Scala с использованием инструмента сборки sbt нужен для указания версии самого sbt.|  
|project/plugins.sbt|Файл plugins.sbt в Scala нужен для добавления плагинов в проект. Плагины позволяют повторно использовать код для сборок.|  
|src/|Это стандартное место для исходного кода и ресурсов приложения. Поддерживается сборщиком SBT, IntelliJ Idea, VDCode и др. |
|src/main/scala|Содержит файлы основного исходного кода Scala|
|src/main/resources|Содержит файлы ресурсов приложения (картинки, конфигураторы, файлы с мета-данными и т.п.) |
|src/test/scala|Содержит файлы тестового исходного кода Scala. *В данной структруе не представлены*|
|src/test/resources|Содержит файлы ресурсов для тестового приложения (картинки, конфигураторы, файлы с мета-данными и т.п.) *В данной структруе не представлены*|
|src/main/resources/log4j2.properties|Настройка системы логирования приложения проекта. В файле задается как и куда будут записываться сообщения при исполнении приложения. |  
|src/main/scala/com/example/actions/package.scala| Файл служит для определения пакетов, объектов и утилит, которые должны быть доступны по прямому доступу из дочерних пакетов. Обычно в этом файле создается один, головной package object, элементы которого доступны в пакетах нижнего уровня по прямому доступу (без импорта) |  
|src/main/scala/com/example/actions/Analitics.scala|Собственный файл со специальным функционалом, вызовы которго осуществляются из других файлов: классов, функций, объектов и др. |  
|src/main/scala/com/example/actions/Processing.scala|Собственный файл со специальным функционалом, вызовы которго осуществляются из других файлов: классов, функций, объектов и др. |  
|src/main/scala/com/example/actions/Main.scala| Файл - точка входа в приложение, содержит  **object Main** или **object extends App** - првичные объекты которые которые исполняются при запуске приложения https://www.scala-lang.org/api/current/scala/App.html |  

**project/build.properties**
В файле версия sbt для сборки проекта. Если не задать нужную версию, то будет применяться установленная по умолчанию, а это может привести к сбою сборки из-за несовместимостей.
Пример заполнения:
```scala
sbt.version = 1.10.11
```

**build.sbt**  
В файле находится описание процесса сборки приложения.
**Пример заполнения:**  
```scala
import sbt.Keys.organization

ThisBuild / version := "0.1.1" // Здесь задать версию сборки проекта
 
ThisBuild / scalaVersion := "2.12.19"  // Здесь задать версию scala для сборки

lazy val root = (project in file("."))
  .settings(
    name := "<appliction name>",
    organization := "com.simple"
  ) // Организация и имя приложения (в данном случае исполняемый файл будет иметь имя <appliction name>-assembly-0.1.1.jar  )

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.5.5",
  "org.apache.spark" %% "spark-sql" % "3.5.5"
) // Зависимости, которые нужно загрузить для использования Spark 3.5.5
 
assembly / assemblyMergeStrategy := {
  case PathList("META-INF", "services", _*) => MergeStrategy.concat
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
} // AssemblyMergeStrategy в Scala используется для настройки стратегии слияния файлов при сборке проекта с помощью плагина sbt-assembly.
```     
Ситуации, в которых может потребоваться настройка стратегии (AssemblyMergeStrategy ) слияния:  
   - если несколько файлов имеют одинаковый относительный путь. По умолчанию стратегия проверяет, что все кандидаты имеют одинаковое содержимое, и выдаёт ошибку в противном случае.
   - при использовании sbt-assembly возникает ошибка, вызванная стратегией слияния по умолчанию deduplicate. В большинстве случаев это происходит из-за файлов в каталоге META-INF. 
   - нужно исключить определённые файлы.   
Подробнее можно посмотреть [здесь](https://www.baeldung.com/scala/sbt-fat-jar)


**project/plugins.sbt**

**src/main/resources/log4j2.properties**  
Файл log4j2.properties в контексте Scala используется для конфигурации системы ведения логов с помощью фреймворка Log4j.  

С помощью этого файла можно, например:
    - определять, куда будут записываться сообщения: на экран или в файлы;
    - использовать разные форматы для дат и самих сообщений;
    - включать в сообщения теги для дальнейшей фильтрации и группировки;
    - вращать файлы ведения логов, чтобы они не росли бесконечно;
    - отправлять сообщения в удалённую центральную систему ведения логов.

Использование файлов конфигурации позволяет менять различные параметры без модификации кода приложения.  
Пример заполнения:
```scala
rootLogger.level = error
rootLogger.appenderRef.stdout.ref = console

appender.console.type = Console
appender.console.name = console
appender.console.target = SYSTEM_OUT
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = %d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n%ex
```

**Вариант организации кода небольшого проекта в структуре src/main/scala (для даного примера) **
1) Создать файл src/main/scala/com/example/package.scala (это стандартный файл пакета)
В файле необходимо создать package верхнего уровня **package com.example** и объект для пакетов нижнего уровня **package object actions**. В объекте прописать элементы общего назначения.
Пример:
```scala
package com.example

import org.apache.spark.sql.SparkSession
import ....

package object actions {

def createSparkSession(appName: String): SparkSession = {
      SparkSession
        .builder()
        .config("spark.sql.caseSensitive", value = true)
        .config("spark.sql.session.timeZone", value = "UTC")
        .appName(appName)
        .getOrCreate()
  }

def parseArgs(args: Array[String]): ... = {
    <код функции>
  }

def my_global_fuction_1 (<params> ): ... = {
    <код функции>
  }

def my_global_fuction_2 (<params> ): ... = {
    <код функции>
  }

def my_global_fuction_3 (<params> ): ... = {
    <код функции>
  }
```
2) Создать файлы c кодом для обработки src/main/scala/com/example/Analitics.scala и src/main/scala/com/example/Processing.scala (это собcтвенные файлы пакета)
В файле необходимо прописать package нижнего уровня **package com.example.actions** с объектами логики приложения. 
Пример Analitics.scala:
```scala
package com.example.actions

object Analitics {
  class ...
  def analize_1... 
  def analize_2...
  ...
}
```
Пример Processing.scala:
```scala
package com.example.actions

object Analitics {
  class ...
  def analize_1... 
  def analize_2...
  ...
}
```
3) Создать основной файл проекта с точкой входа. В файле необходимо создать прописать package нижнего уровня **package com.actions**. Создать стандартный объект вызова приложения с помощью собственнго объекта с **extends App** или Main метода в собственном объекте:
```scala   
def main(args: Array[String])  
    { 
      // prints Run Application
       println("Run Application")  
    }
```
Пример Main.scala:
```scala
package com.example.actions
// Импорт объекта Analitics
import com.example.actions.Analitics._
// Импорт объекта Processing
import com.example.actions.Processing._
//Объектами из package.scala можно пользоваться по прямому вызову (без импорта)

object Main_runner extends App {
  // Чтение параметров
  val (parsed_param1, parsed_param2, parsed_param3) = parseArgs(args = args)
  // Инициализация Spark session
  val spark = createSparkSession("Spark test-convertor")
  // Чтение файлов .parquet

 // Далее последовательно, согласно логике приложения вызываются элементы, определенные в  Processing.scala и Analitics.scala
 }
```

    

Такая организация проекта (с разделением обработки, и вызова) является удобной с точки зрения читаемости кода и его поддержки.

