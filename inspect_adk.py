import google.adk
import os

package_path = os.path.dirname(google.adk.__file__)
print(f"Package path: {package_path}")

for root, dirs, files in os.walk(package_path):
    for file in files:
        if file.endswith(".html") or file.endswith(".js") or file.endswith(".css"):
            print(os.path.join(root, file))
