# Рабочая среда. Установка и конфигурирование.  

Рабочая среда на ОС Ubuntu **Linux 26.04 (Resolute Raccoon)** для изучения технологий, "домашней" разработки небольших систем и проведения экспериментов. Инструкция создана на примере существующей домашней среды и сведена в перечень шагов по установке.  
Используется установленная (чистая) ОС Ubuntu https://ubuntu.ru/. Настраивается рабочее место для разработки и прототипирования.  
  
**Требуется установить и настроить:**
--
 - среды разработки проектов на **scala**, в т.ч. sbt и IDE IntelliJ IDEA
 - Jupyter Notebook c "ядрами" для работы с python, pyspark, pytorch, scala, spark (scala - Apache Toree)

```console
python3 --version  # Проверка версии Python -  должна быть не ниже 3.14.x
```

```console
# Установка пакетов Git (для работы с Git Hub) и curl (инструмент командной строки для работы с HTTP-запросами).  
sudo apt install git
sudo snap install curl
```

### Последовательность шагов установки:  
#### [Шаг 1. Установка Java Development Kit (JDK) (Openjdk-17)](steps/stp_01.md)
#### [Шаг 2. Установка Scala 2.13](steps/stp_02.md)
#### [Шаг 3. Scala Build Tool (SBT). Установка](steps/stp_03.md)
*Время выполнения* - 10 мин.
#### [Шаг 4. IntelliJ IDEA. Установка, настройка и тестовые проекты](steps/stp_04.md)
*Время выполнения* - 20 мин.
#### [Шаг 5. Apache Spark. Установка](steps/stp_05.md)
*Время выполнения* - 15 мин.
#### [Шаг 6. Установка и настройка Jupyter Notebook](steps/stp_06.md)
**Jupter Notebook** - это интерактивная  веб-среда для созданния документов, содержащих исполняемый код с текстовыми пояснениями и графикой. Среда подходит для проверки гипотез, создания прототипов, отладки и презентации решений на python, scala, R и др.  
https://github.com/jupyter/notebook  
*Время выполнения* - 40 мин.
#### [Шаг 7. Jupyter Notebook. Установка и настройка Scala kernel Almond ](steps/stp_07.md)
**Scala Almond** — это ядро Scala для Jupyter. Для созданния документов, содержащих исполняемый код на Scala с текстовыми пояснениями и графикой. 
Проект в Git: https://github.com/almond-sh/almond  
*Время выполнения* - 15 мин.
#### [Шаг 8. Jupyter Notebook. Установка и настройка Scala Kernel Apache Toree ](steps/stp_08.md)
**Apache Toree** - это ядро для Jupyter Notebook для создания основы интерактивных приложений, которые подключаются к Apache Spark и используют его с помощью языка Scala.  
*Время выполнения* - 25 мин.
#### [Шаг 9. Сборка и запуск тестового проекта Spark средствами SBT assembly. ](steps/stp_09.md)
Сборка небольшого проекта Scala Apache Spark (сборщик SBT Assembly) на примере демонстрационного проекта для сборщика SBT Aassembly . Приложение — конвертер файлов формата parquet в формат csv.
Код и описание проекта находится репозитории: https://github.com/chulyukin/spark-simple-parquet .  
*Время выполнения* - 40 мин.
#### [Шаг 10. Сборка и запуск тестового проекта Apache Spark в IntelliJ IDEA. ](steps/stp_10.md)
Еще один демо-проект Scala Spark для сборщика SBT Aassembly. Приложение "Parquetor" - конвертер файлов формата parquet в формат csv с консольным оконным интерфейсом. Код и описание проекта находится репозитории: https://github.com/chulyukin/parquetor_spark .  
*Время выполнения* - 50 мин.  

## В результате выполнения шагов:
**Инструменты среды**
|Инструмент|Версия|Комментарий|Ресурс|
|:-|:-|:-|:-|
|Python3|Python 3.14.x|Версия уже установлена в Ubuntu, устанавливать дополнительно не требуется|https://www.python.org/|
|Java|openjdk-17|Openjdk-17 - это (Open Java Development Kit) - это бесплатная реализация платформы Java Standard Edition (Java SE) с открытым исходным кодом |https://openjdk.org/|
|Scala|2.13.17|Проверенная стабильная версия, хорошо совместима с OoenJDK-17 (в качестве альтернативы можно использовать 2.12.20 )|https://scala-lang.org/|
|SBT|1.12.9| Scala build tool. В качестве альтернативы можно использовать не ниже 1.6.1|https://scala-lang.org/|
|IntelliJ IDEA|2025.2|JetBrains IntelliJ IDEA Community Edition 2025.2 - Cреда разработки для реализации Scala - проектов )|https://www.jetbrains.com/idea/|
|Apache Spark|4.1.1|Фреймворк с открытым исходным кодом для реализации распределённой обработки данных, входящий в экосистему проектов Hadoop. |https://spark.apache.org/|
|Jupyter Notebook|7.5.5|Интерактивный блокнот для выполнения кода на различных языках программирования.|https://jupyter.org/|
|Scala Almond|0.14.5|Ядро Scala для Jupyter. Представляет собой оболочку Scala (Ammonite) для Jupyter|https://almond.sh/|
|Apache Toree|0.5.0|Ядро Scala для Jupyter Notebook. Предоставляет механизм для интерактивного и удалённого доступа к Apache Spark.|https://toree.apache.org/|

