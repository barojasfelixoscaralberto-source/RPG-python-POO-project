# RPG Python POO Project

A turn-based RPG combat simulator built in Python's console, developed to apply object-oriented programming concepts.

## Features
- Choose between 3 player roles (Soldier, Tank, Explorer) and 3 enemy types (Demon, Beast, Witch), each with unique stats
- Turn-based combat system with attack/heal actions
- Enemy AI makes randomized decisions each turn

## OOP Concepts Applied
- **Inheritance**: `Player` and `Enemy` base classes, with `Tank`, `Explorer`, `Soldier` / `Demon`, `Beast`, `Witch` as subclasses
- **Polymorphism**: each subclass overrides `stats()` to return its own formatted output, called through a single shared interface

## Project Structure
RPG-python-POO-project/
|── entities.py # Player, Enemy classes and subclasses
|── main.py # Game loop and user interaction
|── README.md

## How to Run
```bash
git clone https://github.com/barojasfelixoscaralberto-source/RPG-python-POO-project.git
cd RPG-python-POO-project
python main.py
```

## Author
Oscar Alberto Barojas Félix

## Status
First OOP project, actively being refined as I continue learning.