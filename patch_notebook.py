import json
import os

notebook_path = r"c:/Users/adity/OneDrive/Documents/Google-Hackthon/mainArch.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

changes_made = 0

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        new_source = []
        modified = False
        
        # Check for get_adk_proxy_url definition
        if any("def get_adk_proxy_url():" in line for line in source):
            for line in source:
                if 'url = f"http://localhost:{ADK_PORT}"' in line:
                    new_source.append('    url = f"http://localhost:{ADK_PORT}/dev-ui/"\n')
                    modified = True
                elif 'ADK_PORT = "8000/dev.ui"' in line or 'ADK_PORT = "8000"' in line:
                    new_source.append('    ADK_PORT = "8081"\n')
                    modified = True
                elif 'to start the ADK web UI.' in line:
                    new_source.append(line.replace('to start the ADK web UI.', 'to start the ADK web UI on port 8081.'))
                    modified = True
                else:
                    new_source.append(line)
            if modified:
                cell['source'] = new_source
                changes_made += 1
                print("Updated get_adk_proxy_url")
                continue

        # Check for url_prefix definition (first one)
        if any('url_prefix = "localhost:8000' in line for line in source) and any('print(f"ADK web UI run on' in line for line in source):
            for line in source:
                if 'url_prefix = "localhost:8000' in line:
                    new_source.append('    url_prefix = "localhost:8081"\n')
                    modified = True
                elif 'print(f"ADK web UI run on' in line:
                    new_source.append('    print(f"ADK web UI run on : http://{url_prefix}/dev-ui/")\n')
                    modified = True
                else:
                    new_source.append(line)
            if modified:
                cell['source'] = new_source
                changes_made += 1
                print("Updated first url_prefix cell")
                continue

        # Check for !adk web command
        if any('!adk web' in line for line in source):
            for line in source:
                if 'url_prefix = "localhost:8000' in line:
                    new_source.append('    url_prefix = "localhost:8081"\n')
                    modified = True
                elif '!adk web' in line:
                    new_source.append('    !adk web --port 8081 --url_prefix {url_prefix}\n')
                    modified = True
                else:
                    new_source.append(line)
            if modified:
                cell['source'] = new_source
                changes_made += 1
                print("Updated !adk web cell")
                continue

if changes_made > 0:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print(f"Successfully patched {changes_made} cells.")
else:
    print("No changes matched.")
