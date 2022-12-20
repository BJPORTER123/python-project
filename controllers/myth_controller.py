from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.creature import Creature
from models.habitat import Habitat
import repositories.creature_repository as creature_repo
import repositories.habitat_repository as habitat_repo

creatures_blueprint = Blueprint("creatures", __name__)
habitats_blueprint =  Blueprint("habitats", __name__)

# display all the creatures 
@creatures_blueprint.route("/creatures")
def creatures():
    creatures = creature_repo.select_all()
    return render_template("creatures/index.html", creatures = creatures)
# Delete a creature
@creatures_blueprint.route("/creatures/<id>", methods = ['POST'])
def destroy(id):
    creature_repo.delete(id)
    return redirect("/creatures")
# New creature template
@creatures_blueprint.route("/creatures/new", methods = ['GET'])
def new_creature():
    habitats = habitat_repo.select_all()
    return render_template("creatures/newcreature.html", habitats = habitats)
# create a new creature
@creatures_blueprint.route("/creatures", methods = ['POST'])
def create_creature():
    name = request.form['name']
    habitat_id = request.form['habitat_id']
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    habitat = habitat_repo.select(habitat_id)
    creature = Creature(name, habitat, description, quantity, buying_cost,selling_price)
    creature_repo.save(creature)
    return redirect("/creatures")
# edit creature template
@creatures_blueprint.route("creatures/<id>/edit", methods = ['GET'])
def edit_creature(id):
    habitats = habitat_repo.select_all()
    creature = creature_repo.select(id)
    return render_template("creatures/creatureedit.html",habitats = habitats, creature = creature)

# Display all habitats
@habitats_blueprint.route("/habitats")
def habitats():
    habitats = habitat_repo.select_all()
    return render_template("creatures/indexhabitat.html", habitats = habitats)
# delete a habitat
@creatures_blueprint.route("/habitat/<id>", methods = ['POST'])
def destroy_habitat(id):
    habitat_repo.delete(id)
    return redirect("/habitats")
# new habitat template
@habitats_blueprint.route("/habitats/new", methods = ['GET'])
def new_habitat():
    return render_template("/creatures/newhabitat.html")
# create a new habitat
@habitats_blueprint.route("/habitats/new", methods = ['POST'])
def create_habitat():
    name = request.form['name']
    habitat = Habitat[name]
    habitat_repo.save(habitat)
    return redirect("/habitats")

