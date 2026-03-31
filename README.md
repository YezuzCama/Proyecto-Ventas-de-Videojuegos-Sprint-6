# Proyecto de Análisis de Ventas de Videojuegos - Tienda Ice

## Descripción del Proyecto

Este proyecto analiza datos históricos de ventas de videojuegos para identificar patrones que determinen el éxito de un juego. El objetivo es detectar proyectos prometedores y planificar campañas publicitarias para 2017.

## Archivos Incluidos

1. **analisis_videojuegos_ice.ipynb** - Jupyter Notebook con todo el análisis completo
2. **games.csv** - Dataset de ejemplo con 5,000 juegos
3. **generate_sample_data.py** - Script para regenerar datos de ejemplo si es necesario
4. **README.md** - Este archivo con instrucciones

## Requisitos

### Librerías Python necesarias:

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

O instalar todas de una vez:

```bash
pip install -r requirements.txt
```

## Contenido del requirements.txt

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
jupyter>=1.0.0
```

## Cómo Usar

### Opción 1: Usar el dataset de ejemplo incluido

1. Asegúrate de tener todas las librerías instaladas
2. Abre Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Navega a `analisis_videojuegos_ice.ipynb`
4. Modifica la ruta del archivo en la celda de carga:
   ```python
   df = pd.read_csv('games.csv')  # Usa el archivo local
   ```
5. Ejecuta todas las celdas

### Opción 2: Descargar el dataset original

1. Descarga el dataset original desde:
   ```
   https://practicum-content.s3.us-west-1.amazonaws.com/datasets/games.csv
   ```
2. Guarda el archivo en la misma carpeta que el notebook
3. Asegúrate de que la ruta en el notebook sea correcta:
   ```python
   df = pd.read_csv('games.csv')
   ```

### Opción 3: Regenerar datos de ejemplo

Si quieres modificar los datos de ejemplo:

```bash
python generate_sample_data.py
```

Esto generará un nuevo archivo `games.csv` con datos simulados.

## Estructura del Análisis

El notebook está organizado en 6 pasos principales:

### Paso 1: Carga y Exploración de Datos
- Importación de librerías
- Carga del dataset
- Exploración inicial

### Paso 2: Preparación de Datos
- Normalización de nombres de columnas
- Conversión de tipos de datos
- Manejo de valores ausentes
- Cálculo de ventas totales

### Paso 3: Análisis de Datos
- Juegos lanzados por año
- Análisis de ventas por plataforma
- Ciclos de vida de plataformas
- Diagramas de caja por plataforma
- Correlación entre reseñas y ventas
- Distribución por género

### Paso 4: Perfil de Usuario por Región
- Top 5 plataformas por región (NA, EU, JP)
- Top 5 géneros por región
- Impacto de clasificación ESRB

### Paso 5: Pruebas de Hipótesis
- Hipótesis 1: Calificaciones Xbox One vs PC
- Hipótesis 2: Calificaciones Action vs Sports
- Pruebas estadísticas con t-test

### Paso 6: Conclusiones Generales
- Resumen ejecutivo
- Hallazgos clave
- Recomendaciones para campaña 2017

## Visualizaciones Incluidas

El notebook genera múltiples visualizaciones:
- Gráficos de línea (evolución temporal)
- Gráficos de barras (comparaciones)
- Diagramas de caja (distribuciones)
- Histogramas (frecuencias)
- Gráficos de dispersión (correlaciones)

## Resultados Esperados

Al ejecutar el notebook completo, obtendrás:

1. **Datos limpios y procesados** para análisis
2. **Identificación de plataformas líderes** (PS4, XOne, 3DS)
3. **Géneros más rentables** (Action, Shooter, Sports)
4. **Perfiles regionales** distintos para NA, EU y JP
5. **Análisis estadístico** de hipótesis sobre calificaciones
6. **Recomendaciones estratégicas** para campaña 2017

## Notas Importantes

### Sobre el Dataset de Ejemplo

El archivo `games.csv` incluido es un dataset **simulado** con características similares al original:
- 5,000 juegos
- Distribución realista de plataformas y géneros
- Valores ausentes simulados (~40-50% en scores)
- Distribución temporal enfocada en 2009-2016

### Diferencias con Datos Reales

Los datos de ejemplo:
- Son generados aleatoriamente
- Siguen patrones estadísticos realistas
- Pueden producir resultados diferentes en las pruebas de hipótesis
- Son perfectos para aprender la metodología de análisis

### Recomendaciones

Para un análisis de producción:
1. Usa el dataset original de Practicum
2. Valida los resultados de las pruebas estadísticas
3. Considera factores adicionales (presupuestos, marketing)
4. Actualiza el análisis con datos más recientes

## Solución de Problemas

### Error: ModuleNotFoundError
```bash
pip install [nombre_del_módulo]
```

### Error: File not found
Verifica que todos los archivos estén en la misma carpeta o ajusta las rutas en el código.

### Advertencias de Matplotlib
Son normales y no afectan los resultados. Puedes ignorarlas o actualizar matplotlib:
```bash
pip install --upgrade matplotlib
```

## Contacto y Soporte

Este proyecto fue creado como parte del curso de análisis de datos.
Para preguntas sobre el análisis o la metodología, consulta la documentación de:
- Pandas: https://pandas.pydata.org/
- Matplotlib: https://matplotlib.org/
- Seaborn: https://seaborn.pydata.org/
- SciPy: https://scipy.org/

## Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

**¡Buena suerte con tu análisis! 🎮📊**
