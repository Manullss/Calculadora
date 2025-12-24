```text
  ____      _            _           _                 
 / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _ 
| |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |
| |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |
 \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|
```
## 🧮 Calculadora Gráfica en Python (Tkinter)  &nbsp; &nbsp; &nbsp; ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Este proyecto es una calculadora gráfica avanzada desarrollada en Python usando Tkinter.
Permite realizar operaciones matemáticas básicas y avanzadas sin usar eval(), procesando las expresiones manualmente mediante expresiones regulares.   


![06cal](https://github.com/user-attachments/assets/ac6036b8-3c1f-4806-b724-2c795e6a11f6)

🧩 Características  
- Interfaz gráfica con Tkinter 
- Botones con íconos personalizados  
- Entrada dinámica de operaciones  
- Soporte para:  
  - Suma +  
  - Resta -  
  - Multiplicación x  
  - División ÷  +
  - Potencias ^  
  - Raíz cuadrada √  
  - Paréntesis ()  
  - Números decimales . 
- Eliminación de caracteres uno a uno  
- Limpieza total de la operación  
- Manejo de errores de sintaxis (Syntax Error)  
- Evaluación de expresiones matemáticas complejas

🛠️ Requisitos  
Python 3.9 o superior 
Librerías estándar:  
  - tkinter  
  - re


> [!NOTE]
>Las rutas de los íconos están definidas de forma absoluta en el código,
Se recomienda mover los íconos a una carpeta local del proyecto y cambair el path o ruta de estas.


### Uso de la calculadora  
Presiona los botones numéricos para ingresar valores  
Usa los operadores para crear expresiones matemáticas  
El botón ( ← ) elimina el último carácter  
El botón ( C ) limpia toda la operación  
El botón ( = ) evalúa la expresión  
Si la operación es inválida, se mostrará Syntax Error  

Funcionamiento interno  
Las expresiones se analizan con expresiones regulares  
El programa respeta el orden de operaciones:  
 -Paréntesis  
 -Raíces y potencias  
 -Multiplicación y división  
 -Suma y resta  
Se evita el uso de eval() por seguridad  
Los paréntesis implícitos como 2(3) o (4)(5) se interpretan como multiplicaciones  

- **Tecnologías usadas**
  - Python
  - Tkinter
  - Regex (re)
  
**Posibles mejoras**  
Usar rutas relativas para los íconos  
Soporte para teclado  
Historial de operaciones  
Modo científico ampliado  
Refactorizar botones usando bucles  
Separar lógica y GUI en distintos módulos 

>Autor: Manuel Edgardo Barahona - Proyecto Educativo






        



 
