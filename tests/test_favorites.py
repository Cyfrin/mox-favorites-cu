def test_starting_values(favorites):
    assert favorites.retrieve() == 77


def test_can_change_value(favorites):
    # Arrange
    new_number = 99

    # Act
    favorites.store(new_number)

    # Assert
    assert favorites.retrieve() == new_number


def test_can_add_people(favorites):
    # Arrange
    new_person = "Becca"
    favorite_number = 16

    # Act
    favorites.add_person(new_person, favorite_number)

    # Assert
    assert favorites.list_of_people(0) == (favorite_number, new_person)
