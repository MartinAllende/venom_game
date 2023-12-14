import sqlite3

def createDB():
    """funcion encargada de crear una base de datos con el nombre Level_points.db
    """
    conn = sqlite3.connect("Level_points.db")
    conn.commit()
    conn.close()

def createTable():
    """funcion encargada de crear una tabla de nombre puntos y nivel en la base de datos Level_points.db
    """
    conn = sqlite3.connect("Level_points.db")
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE player (
        name text, 
        points integer,
        level integer
    )"""
    )
    conn.commit()
    conn.close()

def insertRow(name, points, level):
    """funcion encargada de insertar datos en la primera fila vacia de la base de datos Level_points.db

    Args:
        name (_type_): nombre del jugador
        points (_type_): puntos del jugador 
        level (_type_): nivel donde consiguio esos puntos
    """
    conn = sqlite3.connect("Level_points.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO player VALUES ('{name}', {points}, {level})"
    cursor.execute(instruction)
    conn.commit()

def get_scores_ordered(world_data):
    """funcion encargada de leer la base de datos Level_points.db, y devolver una lista con sus datos
    ordenados de mayor a menos por puntuacion y nivel

    Args:
        world_data (_type_): informacion de los niveles

    Returns:
        _type_: retornar una lista de listas en las cuales se encuentra por nivel en nombre y las puntuaciones
        oredenadas de mayor a menos de cada jugador
    """
    conn = sqlite3.connect("Level_points.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM player ORDER BY points DESC" 
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close() 

    counter = 1
    points_per_level_list = []
    for i in range(len(world_data)):
        lvl_player_scores = list(filter(lambda player: player[2] == counter, data))
        scores = []
        for players in lvl_player_scores:
            scores.append((players[0],players[1]))
        points_per_level_list.append(scores)
        counter += 1
    return points_per_level_list

def get_score_by_name(name, world_data):
    """funcion encargada de conseguir el score de un jugador segun su nombre

    Args:
        name (_type_): nombre del jugador 
        world_data (_type_): informacion de los niveles

    Returns:
        _type_: una lista de listas en las cuales por nivel estan los scores del jugador
    """

    conn = sqlite3.connect("Level_points.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM player WHERE name like '{name}'"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close() 

    counter = 1
    points_per_level_list = []
    for i in range(len(world_data)):
        lvl_player_scores = list(filter(lambda player: player[2] == counter, data))
        scores = []
        for players in lvl_player_scores:
            scores.append(players[1])
        points_per_level_list.append(scores)
        counter += 1
    return points_per_level_list