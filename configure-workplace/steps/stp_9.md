# Шаг 10. Сборка и запуск тестового проекта Apache Spark в IntelliJ IDEA. 
Конслоное приложение с оконным интрефейсом c bcgjkmpjdfybt  Apache Spark (сборщик SBT Assembly) представлено на примере демонстрационного проекта **spark-simple-parquet - Демо-проект Scala Spark для сборщика SBT Aassembly . Приложение — конвертер файлов формата parquet в формат csv.**  
Код и описание проекта находится репозитории: https://github.com/chulyukin/parquetor_spark .  

Загрузить проект из репозитория
```console
cd ~/SBTProjects
git clone https://github.com/chulyukin/parquetor_spark.git
```  
(Или можно воспользоваться интерфейсом загрузки из Idea)   
Далее про сборку проекта можно прочитать в README самого проекта.  

## Структура проекта
  
```tree
.
├── build.sbt
├── example_parquet
│   ├── example_150plus_columns.parquet
│   ├── example_first.parquet
│   ├── ....
│   └── yellow_tripdata_2023-08.parquet
├── LICENSE
├── project
│   ├── build.properties
│   └── plugins.sbt
├── README.md
└── src
    └── main
        ├── resources
        │   └── log4j2.properties
        └── scala
            └── com
                └── proto
                    └── parquetor
                        ├── package.scala
                        ├── ClassItems.scala
                        ├── Main.scala
                        ├── Menu.scala
                        ├── MessageBox.scala
                        ├── Templates.scala
                        ├── WindowConvert.scala
                        └── WindowInfo.scala                        
```
