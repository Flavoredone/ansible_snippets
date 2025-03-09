import os

structure = {
    'k8s-elk-setup': {
        'inventory.ini': None,
        'site.yml': None,
        'roles': {
            'common': {
                'tasks': {
                    'main.yml': None
                }
            },
            'kubernetes': {
                'tasks': {
                    'main.yml': None
                },
                'templates': {
                    'k8s-join.sh.j2': None
                }
            },
            'elk': {
                'tasks': {
                    'main.yml': None
                },
                'templates': {
                    'elk-config.j2': None
                }
            }
        }
    }
}

# Функция для создания структуры
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            # Если content равен None, значит это файл
            open(path, 'a').close()
        else:
            # Иначе это директория
            os.makedirs(path, exist_ok=True)
            if isinstance(content, dict):
                create_structure(path, content)

# Создаем структуру
create_structure('.', structure)

print("Файловая структура создана.")