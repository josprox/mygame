# Guía de Instalación y Ejecución

## Prerrequisitos

Asegúrate de tener instalado lo siguiente en tu sistema:

1.  **Python 3.8+**: Puedes descargarlo desde [python.org](https://www.python.org/).
2.  **pip**: El gestor de paquetes de Python (generalmente viene incluido).

## Instalación

1.  **Clonar el repositorio** (o descargar el código fuente):
    ```bash
    git clone https://github.com/josprox/mygame
    cd mygame
    ```

2.  **Crear un entorno virtual** (Recomendado):
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias**:
    El proyecto requiere `PySide6`.
    ```bash
    pip install -r requirements.txt
    ```
    *Nota: Si no existe `requirements.txt`, puedes instalarlo directamente:*
    ```bash
    pip install PySide6
    ```

## Ejecución

Para iniciar la aplicación, ejecuta el archivo `main.py` desde la raíz del proyecto:

```bash
python main.py
```

## Solución de Problemas常见

-   **Error: "No module named 'PySide6'"**: Asegúrate de haber activado el entorno virtual y de haber instalado las dependencias.
-   **Problemas de visualización en Linux**: Es posible que necesites instalar librerías adicionales de Qt. Consulta la documentación de PySide6 para tu distribución.
