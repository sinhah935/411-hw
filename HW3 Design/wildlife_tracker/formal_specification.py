from typing import Any, List, Optional


age: Optional[int] = None                   #animal
animal_id: int                              #animal
animals: dict[int, Animal] = {}             #animalManager
animals: List[int] = []                     #habitat
current_date: str                           #migration
current_location: str                       #migration
destination: Habitat                        #migrationPath
duration: Optional[int] = None              #migrationPath
environment_type: str                       #habitat
geographic_area: str                        #habitat
habitat_id: int                             #habitat
habitats: dict[int, Habitat] = {}           #habitatManager
health_status: Optional[str] = None         #animal
migration_id: int                           #migration
migration_path: MigrationPath               #migration
migrations: dict[int, Migration] = {}       #MigrationManager
path_id: int                                #MigrationPath
paths: dict[int, MigrationPath] = {}        #MigrationManager
size: int                                   #habitat
species: str                                #animal
species: str                                #migrationPath
start_date: str                             #migration
start_location: Habitat                     #migrationPath
status: str = "Scheduled"                   #migration


def assign_animals_to_habitat(animals: List[Animal]) -> None:  #habitat
    pass

def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:  #habitatManager
    pass

def cancel_migration(migration_id: int) -> None:
    pass

def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat: #habitatManager
    pass

def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None: #migrationManager
    pass

def get_animal_by_id(animal_id: int) -> Optional[Animal]: #animalManager
    pass

def get_animal_details(animal_id) -> dict[str, Any]: #animal 
    pass

def get_animals_in_habitat(habitat_id: int) -> List[Animal]:    #habitat
    pass

def get_habitat_by_id(habitat_id: int) -> Habitat:      #habitatManager
    pass

def get_habitat_details(habitat_id: int) -> dict:       #habitat
    pass

def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]: #habitatManager
    pass

def get_habitats_by_size(size: int) -> List[Habitat]:   #habitatManager
    pass

def get_habitats_by_type(environment_type: str) -> List[Habitat]:   #habitatManager
    pass

def get_migration_by_id(migration_id: int) -> Migration:    #migrationPath
    pass

def get_migration_details(migration_id: int) -> dict[str, Any]: #migration
    pass

def get_migration_path_by_id(path_id: int) -> MigrationPath:    #migrationPath
    pass

def get_migration_paths() -> list[MigrationPath]:               #migrationManager
    pass

def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:    #migrationPath
    pass

def get_migration_paths_by_species(species: str) -> list[MigrationPath]:    #migrationPath    
    pass

def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:  #migrationPath  
    pass

def get_migrations() -> list[Migration]:        #migration
    pass

def get_migrations_by_current_location(current_location: str) -> list[Migration]:   #migration
    pass

def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:    #??
    pass

def get_migrations_by_start_date(start_date: str) -> list[Migration]:   #migration
    pass

def get_migrations_by_status(status: str) -> list[Migration]:   #migration
    pass

def get_migration_path_details(path_id) -> dict:    #migrationPath
    pass

def register_animal(animal: Animal) -> None:  #animalManager
    pass

def remove_animal(animal_id: int) -> None:      #animalManager
    pass

def remove_habitat(habitat_id: int) -> None:    #habitatManager
    pass

def remove_migration_path(path_id: int) -> None:    #migrationPath
    pass

def schedule_migration(migration_path: MigrationPath) -> None:  #migration
    pass

def update_animal_details(animal_id: int, **kwargs: Any) -> None:      #animal
    pass

def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:  #habitat
    pass

def update_migration_details(migration_id: int, **kwargs: Any) -> None: #migration
    pass

def update_migration_path_details(path_id: int, **kwargs) -> None:  #migrationPath
    pass