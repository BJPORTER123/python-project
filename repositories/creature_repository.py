from db.run_sql import run_sql
from models.creature import Creature
from models.habitat import Habitat
import repositories.habitat_repository as habitat_repo


def select_all():
    creatures = []
    sql = "SELECT * FROM creatures"
    results = run_sql(sql)
    for row in results:
        habitat = habitat_repo.select(row['habitat_id'])
        creature = Creature(row['name'],habitat, row['description'], row['quantity'],row['buying_cost'],row['selling_price'],row['image'] ,row['id'])
        creatures.append(creature)
    return creatures

def select(id):
    creature = None
    sql = "SELECT * FROM creatures WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        habitat = habitat_repo.select(result['habitat_id'])
        creature = Creature(result['name'], habitat, result['description'], result['quantity'], result['buying_cost'], result['selling_price'] , result['image'], result['id'] )
    return creature

def delete_all():
    sql = "DELETE FROM creatures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM creatures WHERE id= %s"
    values = [id]
    run_sql(sql, values)

def save(creature):
    sql = "INSERT INTO creatures (name, habitat_id, description, quantity, buying_cost, selling_price, image) VALUES (%s, %s, %s, %s ,%s, %s, %s) RETURNING *"
    values = [creature.name ,creature.habitat.id, creature.description, creature.quantity, creature.buying_cost, creature.selling_price, creature.image]
    results = run_sql(sql,values)
    id = results[0]['id']
    creature.id = id
    return creature

def update(creature):
    sql = "UPDATE creatures SET (name, habitat_id, description, quantity, buying_cost, selling_price, image) = (%s, %s, %s, %s, %s,%s, %s) WHERE id = %s"
    values = [creature.name, creature.habitat.id, creature.description, creature.quantity, creature.buying_cost, creature.selling_price, creature.id]
    run_sql(sql, values)
