from db.run_sql import run_sql

from models.creature import Creature
from models.habitat import Habitat

def select_all():
    habitats = []
    sql = "SELECT * FROM habitats"
    results = run_sql(sql)
    for row in results:
        habitat = Habitat(row['name'],row['id'])
        habitats.append(habitat)
    return habitats

def select(id):
    habitat = None
    sql = "SELECT * FROM habitats WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        habitat = Habitat(result['name'],result['id'])
    return habitat

def delete_all():
    sql = "DELETE FROM habitats"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM habitats WHERE id= %s"
    values = [id]
    run_sql(sql, values)

def save(habitat):
    sql = "INSERT INTO habitats (name) VALUES (%s) RETURNING id"
    values = [habitat.name]
    results = run_sql(sql,values)
    id = results[0]['id']
    habitat.id =id
    return habitat

def update(habitat):
    sql = "UPDATe habitats SET (name) = (%s) WHERE id = %s"
    values = [habitat.name, habitat.id]