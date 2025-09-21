# App Tkinter con GitHub Actions

Este es un proyecto de prueba para aprender a usar **GitHub Actions** con Python y Tkinter.

## 🚀 Cómo funciona

1. Cada vez que publiques un **release** en GitHub, se ejecutará un workflow.
2. Ese workflow:
   - Instala Python
   - Instala dependencias
   - Usa PyInstaller para crear un `.exe`
   - Sube el `.exe` al release automáticamente

## 🖥️ Ejecución local

```bash
python app.py
```
