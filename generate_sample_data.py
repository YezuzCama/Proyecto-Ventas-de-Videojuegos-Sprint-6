"""
Script para generar datos de ejemplo de videojuegos
Simula el dataset games.csv para el proyecto de análisis de Ice
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Configurar semilla para reproducibilidad
np.random.seed(42)

# Definir parámetros
n_games = 5000

# Listas de opciones
platforms = ['PS4', 'XOne', 'PC', '3DS', 'PS3', 'X360', 'WiiU', 'PSV', 'Wii', 'PS2']
genres = ['Action', 'Shooter', 'Sports', 'Role-Playing', 'Racing', 'Fighting', 
          'Adventure', 'Platform', 'Simulation', 'Strategy', 'Puzzle', 'Misc']
ratings = ['E', 'E10+', 'T', 'M', 'AO', 'RP', np.nan]

# Nombres de juegos (ejemplos + generados)
game_names_base = [
    'Call of Duty', 'Grand Theft Auto', 'FIFA', 'Madden NFL', 'NBA 2K',
    'The Legend of Zelda', 'Super Mario', 'Pokemon', 'Assassins Creed',
    'Battlefield', 'Halo', 'Minecraft', 'The Elder Scrolls', 'Fallout',
    'Uncharted', 'The Last of Us', 'Dark Souls', 'Final Fantasy',
    'Metal Gear Solid', 'Resident Evil', 'Street Fighter', 'Mortal Kombat',
    'Need for Speed', 'Gran Turismo', 'Forza Motorsport'
]

# Generar datos
data = {
    'Name': [],
    'Platform': [],
    'Year_of_Release': [],
    'Genre': [],
    'NA_sales': [],
    'EU_sales': [],
    'JP_sales': [],
    'Other_sales': [],
    'Critic_Score': [],
    'User_Score': [],
    'Rating': []
}

for i in range(n_games):
    # Nombre del juego
    if i < len(game_names_base) * 20:
        base_name = np.random.choice(game_names_base)
        year_suffix = np.random.choice(['', ' 2', ' 3', ' 4', ' V', ' VI', ' 2015', ' 2016'])
        name = f"{base_name}{year_suffix}"
    else:
        name = f"Game Title {i}"
    
    # Plataforma
    platform = np.random.choice(platforms, p=[0.25, 0.20, 0.15, 0.12, 0.08, 0.07, 0.05, 0.03, 0.03, 0.02])
    
    # Año de lanzamiento (más juegos recientes)
    year_weights = np.array([0.05, 0.08, 0.10, 0.12, 0.15, 0.18, 0.20, 0.12])
    years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
    year = np.random.choice(years, p=year_weights)
    
    # Algunos valores ausentes en year
    if np.random.random() < 0.02:
        year = np.nan
    
    # Género
    genre = np.random.choice(genres)
    
    # Ventas base según plataforma y año
    base_sales = np.random.lognormal(0, 1.5)
    
    # Ajustar según plataforma
    platform_multipliers = {
        'PS4': 1.5, 'XOne': 1.3, 'PC': 1.2, '3DS': 1.0,
        'PS3': 0.8, 'X360': 0.7, 'WiiU': 0.6, 'PSV': 0.5,
        'Wii': 0.4, 'PS2': 0.3
    }
    multiplier = platform_multipliers.get(platform, 1.0)
    
    # Ventas por región
    na_sales = round(base_sales * multiplier * np.random.uniform(0.3, 0.5), 2)
    eu_sales = round(base_sales * multiplier * np.random.uniform(0.25, 0.45), 2)
    
    # Japón favorece ciertas plataformas
    jp_multiplier = 1.5 if platform in ['3DS', 'PSV', 'PS4'] else 0.5
    jp_sales = round(base_sales * multiplier * jp_multiplier * np.random.uniform(0.1, 0.3), 2)
    
    other_sales = round(base_sales * multiplier * np.random.uniform(0.05, 0.15), 2)
    
    # Scores
    # Algunos juegos no tienen scores
    if np.random.random() < 0.4:
        critic_score = np.nan
    else:
        critic_score = np.random.randint(40, 100)
    
    if np.random.random() < 0.5:
        user_score = 'tbd' if np.random.random() < 0.1 else round(np.random.uniform(3.0, 9.5), 1)
    else:
        user_score = np.nan
    
    # Rating
    rating = np.random.choice(ratings, p=[0.15, 0.10, 0.15, 0.25, 0.02, 0.03, 0.30])
    
    # Agregar a los datos
    data['Name'].append(name)
    data['Platform'].append(platform)
    data['Year_of_Release'].append(year)
    data['Genre'].append(genre)
    data['NA_sales'].append(na_sales)
    data['EU_sales'].append(eu_sales)
    data['JP_sales'].append(jp_sales)
    data['Other_sales'].append(other_sales)
    data['Critic_Score'].append(critic_score)
    data['User_Score'].append(user_score)
    data['Rating'].append(rating)

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar como CSV
df.to_csv('/home/claude/games.csv', index=False)
print(f"Dataset generado con {len(df)} juegos")
print(f"Guardado en: /home/claude/games.csv")
print("\nPrimeras filas:")
print(df.head())
print("\nInformación del dataset:")
print(df.info())
