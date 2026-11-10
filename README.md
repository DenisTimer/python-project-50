# Вычислитель отличий (Python)

[![hexlet-check](https://github.com/DenisTimer/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DenisTimer/python-project-50/actions)
[![CI](https://github.com/DenisTimer/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/DenisTimer/python-project-50/actions/workflows/ci.yml)

В этом проекте отрабатывается работа с коллекциями. Изучаются способы построения и обхода деревьев. Вы познакомитесь с разными форматами данных (JSON, YAML), научитесь их парсить и формировать. Начнете писать тесты (pytest) и освоите разработку через них. Познакомитесь с непрерывной интеграцией (CI) и элементами экстремального программирования (XP)

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://asciinema.org/a/Pe6QypnLEmFWssNAjCOJN1iii

## Стек

- Python

## Установка

<!-- Опишите установку: клонирование, зависимости, переменные окружения -->

```bash
git clone https://github.com/DenisTimer/python-project-50.git
cd python-project-50
```

## Использование

`gendiff` сравнивает два конфигурационных файла и показывает, какие параметры добавились, удалились или изменились. Поддерживаются JSON (`.json`) и YAML (`.yaml`, `.yml`).

Запускать команды из корня проекта.

### Сравнение JSON

```bash
uv run gendiff tests/test_data/file1.json tests/test_data/file2.json
```

[Посмотреть демонстрацию сравнения JSON](https://asciinema.org/a/bu7fYurpW4DXqD0e)

### Сравнение YAML

```bash
uv run gendiff tests/test_data/file1.yml tests/test_data/file2.yml
```

[Посмотреть демонстрацию сравнения YAML](https://asciinema.org/a/MvGkkqArqiSaSiju)

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
