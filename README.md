# Colección de Juegos Python (WinUI 3 Edition)

Una colección de 3 mini-juegos clásicos reimaginados con una interfaz moderna estilo Windows 11 (WinUI 3) utilizando Python y PySide6.

## Juegos Incluidos

1.  **El Ahorcado**: Adivina la palabra secreta antes de que se complete el dibujo del ahorcado. Cuenta con gráficos vectoriales suaves.
2.  **Cartas Mágicas**: Piensa un número del 1 al 31 y el juego lo adivinará mostrándote 5 cartas mágicas.
3.  **El Río**: El clásico acertijo de lógica. Ayuda al Lobo, la Gallina y el Maíz a cruzar el río sin que nadie sea comido.

## Requisitos

- Python 3.8 o superior.
- Librerías listadas en `requirements.txt`.

## Instalación

1.  Clona este repositorio o descarga el código.
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Para iniciar el juego, ejecuta:

```bash
python main.py
```

## Compilación (Crear .exe)

Si deseas crear un ejecutable independiente para Windows:

1.  Asegúrate de tener `pyinstaller` instalado (incluido en requirements.txt).
2.  Ejecuta el script de construcción:
    ```bash
    python build_app.py
    ```
3.  El ejecutable `JuegosPython.exe` se generará en la carpeta `dist/`.

## Estructura del Proyecto

El proyecto sigue una arquitectura **MVC** (Modelo-Vista-Controlador):

-   `models/`: Lógica pura de los juegos.
-   `views/`: Interfaz gráfica (PySide6 widgets).
-   `controllers/`: Conexión entre lógica e interfaz.
-   `styles.py`: Hoja de estilos QSS para el tema oscuro WinUI 3.
-   `main.py`: Punto de entrada de la aplicación.
