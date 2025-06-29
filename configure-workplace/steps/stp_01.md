# Шаг 1. Установка JDK (Openjdk-17) 

**Перед началом необходимо обновить репозиторий**
```console
sudo apt update
sudo apt upgrade
```

**Установка openjdk-17**
```console
sudo apt-cache search openjdk | grep openjdk-17
```  
```console
sudo apt install openjdk-17-jre
sudo apt install openjdk-17-jdk
```  
**Проверка версии**
```console
java --version
# openjdk 17.0.15 2025-04-15
# OpenJDK Runtime Environment (build 17.0.15+6-Ubuntu-0ubuntu125.04)
# OpenJDK 64-Bit Server VM (build 17.0.15+6-Ubuntu-0ubuntu125.04, mixed mode, sharing)
```
