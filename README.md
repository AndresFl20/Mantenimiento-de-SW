# 📚 Mantenimiento de Software | CORPORACIÓN UNIVERSITARIA IBEROAMERICANA

**Basado en:**  
Unidad 2 – Actividad práctica colaborativa: Mantenimiento e implementación de funcionalidades mediante Git y GitHub.  
**Proyecto principal:** Gestor de Biblioteca en Python — versión inicial mejorada mediante mantenimiento correctivo, adaptativo y evolutivo.

---

## ✍🏽 Descripción

Este proyecto es un **Sistema de Gestión de Biblioteca** desarrollado en Python como parte del módulo Mantenimiento de Software. Su propósito es aplicar buenas prácticas de **control de versiones, documentación, trabajo colaborativo y técnicas de mantenimiento** mediante la creación, mejora y ampliación de un sistema funcional.

El equipo partirá de una versión base del sistema y realizará:

- Mantenimiento **evolutivo** implementando cinco historias de usuario  
- Mantenimiento **correctivo**  
- Mejoras estructurales para garantizar un código más claro, modular y sostenible  

Todo el proceso se gestionará mediante **Git y GitHub** utilizando ramas, commits estructurados, pull requests y seguimiento de cambios.

---

## 🔠 Características

- Gestión de libros: registro, consulta, disponibilidad  
- Administración de usuarios  
- Registro de préstamos y devoluciones  
- Búsqueda de información por criterios definidos en las historias de usuario  
- Mejoras introducidas a partir del mantenimiento requerido en la actividad  
- Estructura modular del código para facilitar futuras actualizaciones  
- Historial de cambios documentado mediante commits y ramas

---

## 🧑🏽‍💻 Tecnologías y Herramientas

- **Lenguaje:** Python  
- **Control de versiones:** Git  
- **Repositorio colaborativo:** GitHub  
- **Mantenimiento aplicado:**  
  - Correctivo (corrección de errores)  
  - Evolutivo (nuevas funcionalidades según historias de usuario)  
  - Preventivo (mejoras de legibilidad y estructura)  
  - Adaptativo (ajustes necesarios para nuevas necesidades)  
- **Interacción:** Consola / línea de comandos

---

## 🧠 Historias de Usuario (a implementar)

*(Ejemplo general; puedes reemplazarlas si ya tienes otras)*

1. Como usuario quiero buscar libros por título para encontrarlos rápidamente  
2. Como administrador quiero registrar nuevos usuarios para gestionar préstamos  
3. Como usuario quiero visualizar los libros disponibles para seleccionar uno  
4. Como administrador quiero registrar préstamos y devoluciones para controlar el inventario  
5. Como usuario quiero ver mi historial de préstamos para conocer mis libros leídos

---

## 📂 Estructura del Código

### Clases principales
- **Libro** — información del libro  
- **Usuario** — información del lector  
- **Biblioteca** — lógica principal del sistema

### Funcionalidades del menú
- Registrar libros  
- Registrar usuarios  
- Prestar y devolver libros  
- Consultar libros  
- Consultar usuarios  
- Ver historial de préstamos  
- Búsquedas según funcionalidades solicitadas

---

## 🔧 Uso

1. Ejecutar el programa desde consola:  
```bash
python main.py
