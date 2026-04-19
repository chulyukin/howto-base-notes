# Шаг 1. Установка JDK (Openjdk-17) 

**Обновление репозитория**
```console
sudo apt update
sudo apt upgrade
```

**Установка openjdk-17**
```console
sudo apt-cache search openjdk | grep openjdk-17
sudo apt install openjdk-17-jre
sudo apt install openjdk-17-jdk
```  
**Вывод версии**
```console
java --version
# openjdk 17.0.17-ea 2025-10-2x
# OpenJDK Runtime Environment (build 17.0.17-ea+8-Ubuntu-1)
# OpenJDK 64-Bit Server VM (build 17.0.17-ea+8-Ubuntu-1, mixed mode, sharing)
```
