from models import Creature

# Test the Creature class
def test_creature():
    # Create a test creature
    test_creature = Creature('Test Creature', 'Test Habitat', 'Test Description', 10, 5, 10)

    # Test that the creature attributes are set correctly
    assert test_creature.name == 'Test Creature'
    assert test_creature.habitat == 'Test Habitat'
    assert test_creature.description == 'Test Description'
    assert test_creature.quantity == 10
    assert test_creature.buying_cost == 5
    assert test_creature.selling_price == 10