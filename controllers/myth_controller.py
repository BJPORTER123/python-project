from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.creature import Creature
from models.habitat import Habitat
import repositories.creature_repository as creature_repo
import repositories.habitat_repository as habitat_repo

creatures_blueprint = Blueprint("creatures", __name__)
habitats_blueprint =  Blueprint("habitats", __name__)

# creatures contoller section
# 1 display all the creatures 
@creatures_blueprint.route("/creatures")
def creatures():
    creatures = creature_repo.select_all()
    return render_template("creatures/index.html", creatures = creatures)

# 2 show individual creature
@creatures_blueprint.route("/creatures/<id>", methods = ['GET'])
def show_creature(id):
    creature = creature_repo.select(id)
    return render_template("/creatures/show.html", creature = creature)

# 3 Delete a creature
@creatures_blueprint.route("/creatures/<id>/delete", methods = ['POST'])
def destroy(id):
    creature_repo.delete(id)
    return redirect("/creatures")

# 4 New creature template
@creatures_blueprint.route("/creatures/new", methods = ['GET'])
def new_creature():
    habitats = habitat_repo.select_all()
    return render_template("/creatures/new.html", habitats = habitats)

# 5 create a new creature
@creatures_blueprint.route("/creatures", methods = ['POST'])
def create_creature():
    name = request.form['name']
    habitat = habitat_repo.select(request.form['habitat_id'])
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    image = request.form['image']
    if image.strip() == "":
        image = "https://media.istockphoto.com/id/1357365823/vector/default-image-icon-vector-missing-picture-page-for-website-design-or-mobile-app-no-photo.jpg?s=612x612&w=0&k=20&c=PM_optEhHBTZkuJQLlCjLz-v3zzxp-1mpNQZsdjrbns="
    creature = Creature(name, habitat, description, quantity, buying_cost, selling_price, image)
    creature_repo.save(creature)
    return redirect("/creatures")


# 6 edit creature template
@creatures_blueprint.route("/creatures/<id>/edit", methods = ['GET'])
def edit_creature(id):
    habitats = habitat_repo.select_all()
    creature = creature_repo.select(id)
    return render_template("/creatures/edit.html",habitats = habitats, creature = creature)

# 7 update a creature
@creatures_blueprint.route("/creatures/<id>/update", methods = ['POST'])
def update_creature(id):
    name = request.form ['name']
    description = request.form ['description']
    quantity = request.form ['quantity']
    buying_cost = request.form ['buying_cost']
    selling_price = request.form ['selling_price']
    habitat = habitat_repo.select(request.form['habitat_id'])
    image = request.form['image']
    creature = Creature(name, habitat, description, quantity, buying_cost, selling_price, image, id)
    creature_repo.update(creature)
    return redirect("/creatures")
        

# HABITATS CONTROLLER SECTION
# 1 Display all habitats
@habitats_blueprint.route("/habitats")
def habitats():
    habitats = habitat_repo.select_all()
    return render_template("/habitats/index.html", habitats = habitats)

# 2 show individual habitat
@habitats_blueprint.route("/habitats/<id>", methods = ['GET'])
def show_habitat(id):
    habitat = habitat_repo.select(id)
    return render_template("/habitats/show.html", habitat = habitat)

# 3 delete a habitat
@habitats_blueprint.route("/habitats/<id>/delete", methods = ['POST'])
def destroy_habitat(id):
    habitat_repo.delete(id)
    return redirect("/habitats")

# 4 new habitat template
@habitats_blueprint.route("/habitats/new", methods = ['GET'])
def new_habitat():
    return render_template("/habitats/new.html")

# 5 create a new habitat
@habitats_blueprint.route("/habitats", methods = ['POST'])
def create_habitat():
    name = request.form['name']
    image = request.form['image']
    if image.strip() == "":
        image = "https://media.istockphoto.com/id/1357365823/vector/default-image-icon-vector-missing-picture-page-for-website-design-or-mobile-app-no-photo.jpg?s=612x612&w=0&k=20&c=PM_optEhHBTZkuJQLlCjLz-v3zzxp-1mpNQZsdjrbns="
    habitat = Habitat(name, image)
    habitat_repo.save(habitat)
    return redirect("/habitats")

# 6 edit habitat template
@habitats_blueprint.route("/habitats/<id>/edit", methods = ['GET'])
def edit_habitat(id):
    habitat = habitat_repo.select(id)
    return render_template("/habitats/edit.html",habitat = habitat)

# 7 update habitat
@habitats_blueprint.route("/habitats/<id>/update", methods = ['POST'])
def update_habitat(id):
    name = request.form['name']
    image = request.form['image']
    habitat = Habitat(name, image, id)
    habitat_repo.update(habitat)
    return redirect("/habitats")


    

