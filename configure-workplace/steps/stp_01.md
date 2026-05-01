# Шаг 1. Установка JDK (Openjdk-17) 
JDK (Java Development Kit) — это комплект инструментов, для создания и запуска приложений на Java (Scala, Spark используют для исполнения JVM (Java Virtual Machine)).  

**Обновление репозитория**
```console
sudo apt update
sudo apt upgrade
```

**Установка openjdk-17** (Для работы со Spark - требуется версия 17)
```console
sudo apt-cache search openjdk | grep openjdk-17
sudo apt install openjdk-17-jre
sudo apt install openjdk-17-jdk
```  
**Вывод версии Java (д.б. 17)**
```console
java --version
# openjdk 17.x.xx 2026-xx-xx
# OpenJDK Runtime Environment (build 17.x.xx-ea+8-Ubuntu-1)
# OpenJDK 64-Bit Server VM (build 17.x.xx-ea+8-Ubuntu-1, mixed mode, sharing)
```
