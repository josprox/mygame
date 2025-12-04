# Documentación de API

Esta referencia documenta las clases y métodos principales de los controladores y modelos.

## Controladores (`controllers/`)

### `MainController`
Gestiona la navegación principal y la ventana de la aplicación.

-   **`show_menu()`**: Muestra la vista del menú principal.
-   **`show_game(game_name: str)`**: Cambia la vista al juego especificado (`"hangman"`, `"magic_cards"`, `"river"`).
-   **`run()`**: Inicia el bucle principal de la ventana.

### `HangmanController`
Controlador para el juego del Ahorcado.

-   **`start_game(word, description, attempts)`**: Inicializa una nueva partida con los parámetros dados.
-   **`guess_letter(letter)`**: Procesa el intento de una letra.
-   **`update_view()`**: Sincroniza la vista con el estado actual del modelo.

### `MagicCardsController`
Controlador para el juego de Cartas Mágicas.

-   **`start_game()`**: Reinicia el juego y muestra la primera carta.
-   **`answer(is_yes: bool)`**: Procesa la respuesta del usuario (Sí/No) para la carta actual.

### `RiverController`
Controlador para el juego del Río.

-   **`move_item(item)`**: Intenta mover un ítem (`"Lobo"`, `"Gallina"`, `"Maíz"` o `None` para solo la barca) al otro lado del río.

---

## Modelos (`models/`)

### `HangmanModel`
Lógica del Ahorcado.

-   **Atributos**:
    -   `secret_word`: La palabra a adivinar.
    -   `attempts_left`: Intentos restantes.
    -   `guessed_letters`: Conjunto de letras ya intentadas.
-   **Métodos**:
    -   `check_win()`: Devuelve `True` si se ha adivinado la palabra completa.
    -   `get_masked_word()`: Devuelve la palabra con guiones bajos para las letras no adivinadas.

### `MagicCardsModel`
Lógica de Cartas Mágicas (Adivinación binaria).

-   **Métodos**:
    -   `get_current_card_numbers()`: Genera los números para la carta actual basándose en bits.
    -   `process_answer(is_yes)`: Actualiza el número acumulado si la respuesta es afirmativa.
    -   `get_result()`: Devuelve el número final calculado.

### `RiverModel`
Lógica del acertijo del Río.

-   **Atributos**:
    -   `left_bank`: Conjunto de ítems en la orilla izquierda.
    -   `right_bank`: Conjunto de ítems en la orilla derecha.
    -   `boat_position`: `'left'` o `'right'`.
-   **Métodos**:
    -   `move(item)`: Mueve un ítem y la barca, luego verifica el estado.
    -   `check_state()`: Verifica si se ha ganado o perdido (reglas de depredación).
