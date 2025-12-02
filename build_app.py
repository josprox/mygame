import PyInstaller.__main__
import os

# Define the build options
options = [
    'main.py',                      # Your main script
    '--name=JuegosPython',          # Name of the executable
    '--onefile',                    # Create a single executable file
    '--windowed',                   # No console window
    '--noconfirm',                  # Overwrite existing build/dist folders
    '--clean',                      # Clean cache
    # Add data if needed (e.g., images, though we draw everything with code)
    # '--add-data=path/to/data;dest_folder', 
]

print("Iniciando compilación con PyInstaller...")
print(f"Opciones: {options}")

try:
    PyInstaller.__main__.run(options)
    print("\n¡Compilación exitosa!")
    print(f"El ejecutable se encuentra en: {os.path.abspath('dist/JuegosPython.exe')}")
except Exception as e:
    print(f"\nError durante la compilación: {e}")
