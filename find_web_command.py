import os

search_path = r"C:\Users\adity\AppData\Local\Programs\Python\Python312\Lib\site-packages\google\adk\cli"

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if "@click.command" in content and "def web" in content:
                    print(f"Found web command in: {path}")
