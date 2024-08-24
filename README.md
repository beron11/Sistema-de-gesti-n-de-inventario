# Sistema de Gestión de Inventario

## Descripción

Este proyecto implementa un **Sistema de Gestión de Inventario** diseñado para facilitar el seguimiento y administración de productos, categorías, proveedores y bodegas. El sistema permite realizar operaciones como registro de entidades, gestión de stock, establecimiento de relaciones entre entidades y generación de consultas e informes detallados. Está desarrollado en **Python** y estructurado siguiendo las mejores prácticas de programación orientada a objetos, con cada clase definida en archivos separados para mejorar la modularidad y mantenibilidad del código.

La interfaz de usuario actual es de **línea de comandos enriquecida** utilizando la librería [Rich](https://rich.readthedocs.io/), con planes futuros para una implementación web utilizando **Flask**.

## Tabla de Contenidos

- [Características Principales](#características-principales)
  - [Registro de Entidades](#registro-de-entidades)
  - [Gestión de Stock](#gestión-de-stock)
  - [Relaciones entre Entidades](#relaciones-entre-entidades)
  - [Consultas y Reportes](#consultas-y-reportes)
- [Diagrama de Clases (UML)](#diagrama-de-clases-uml)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
  - [Clonar el Repositorio](#clonar-el-repositorio)
  - [Configuración del Entorno Virtual](#configuración-del-entorno-virtual)
  - [Instalación de Dependencias](#instalación-de-dependencias)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Uso de Git](#uso-de-git)
  - [Primer Commit](#primer-commit)
  - [Realizar Cambios y Enviarlos](#realizar-cambios-y-enviarlos)
  - [Actualizar el Repositorio Local](#actualizar-el-repositorio-local)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Autor](#autor)
- [Recursos y Herramientas Utilizadas](#recursos-y-herramientas-utilizadas)
- [Planes Futuros](#planes-futuros)
- [Licencia](#licencia)

---

## Características Principales

### Registro de Entidades

El sistema permite registrar y administrar las siguientes entidades clave:

- **Producto**
  - Atributos: nombre, descripción, precio, stock inicial y categoría asociada.
  
- **Categoría**
  - Atributos: nombre y descripción.
  
- **Proveedor**
  - Atributos: nombre, dirección, teléfono y lista de productos suministrados.
  
- **Bodega**
  - Atributos: nombre, ubicación, capacidad máxima y lista de productos almacenados.

### Gestión de Stock

Operaciones para mantener y actualizar el inventario de productos:

- **Agregar Stock**
  - Incrementa la cantidad disponible de un producto existente especificando la cantidad a añadir.
  
- **Retirar Stock**
  - Decrementa la cantidad disponible de un producto existente especificando la cantidad a retirar.
  
- **Calcular Valor Total del Stock**
  - Calcula el valor total del stock multiplicando el precio de cada producto por su cantidad disponible.

### Relaciones entre Entidades

Establece y administra las relaciones entre las diferentes entidades del sistema:

- **Productos y Categorías**
  - Agregar o eliminar un producto de una categoría existente.
  
- **Productos y Proveedores**
  - Agregar o eliminar un producto de la lista de productos suministrados por un proveedor existente.
  
- **Productos y Bodegas**
  - Agregar un producto a una bodega verificando la disponibilidad de espacio.
  - Retirar un producto de una bodega asegurando que la cantidad a retirar no exceda el stock disponible.
  - Consultar la disponibilidad de un producto en una bodega específica.

### Consultas y Reportes

Provee información detallada sobre las entidades y el estado del inventario:

- **Consultas Individuales**
  - Información completa de productos, categorías, proveedores y bodegas.
  
- **Informes de Stock**
  - Genera reportes detallados mostrando:
    - Stock total.
    - Stock por categoría.
    - Stock por proveedor.
    - Stock por bodega.

---

## Diagrama de Clases (UML)

El diseño del sistema está representado mediante un **Diagrama de Clases UML** que ilustra las clases, sus atributos, métodos y las relaciones entre ellas.

> **Ubicación del Diagrama:** [diagrama-UML.png](diagrama-UML.png)

> **Herramienta Utilizada:** [eraser.io](https://eraser.io/) para la creación y edición del diagrama UML.

---
##Autor
**Nombre del Autor:** -Juan Sebastian Beron Lozada.
**Contacto: -juanseberon11@gmail.com.

## Requisitos Previos

Asegúrese de tener instalados los siguientes componentes en su sistema:

- **Python 3.8 o superior**
  - [Descargar Python](https://www.python.org/downloads/)
  
- **Git**
  - [Descargar Git](https://git-scm.com/downloads)

---

## Instalación y Configuración

Siga los pasos a continuación para configurar y ejecutar el proyecto en su entorno local.

### Clonar el Repositorio

```bash
git clone https://github.com/beron11/sistema-gestion-inventario.git
cd sistema-gestion-inventario
