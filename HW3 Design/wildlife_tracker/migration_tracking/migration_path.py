from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration

class MigrationPath:

    def __init__(self,
                 path_id: int,
                 species: str,
                 start_location: Habitat,
                 destination: Habitat,
                 duration: Optional[int] = None 
                 ) -> None:
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration
        pass

        pass

    def get_migration_path_details(path_id) -> dict:    #migrationPath
        pass

    def remove_migration_path(path_id: int) -> None:    #migrationPath
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:  #migrationPath
        pass
    def get_migrations() -> list[Migration]:
        pass
    
    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]: 
        pass
    
    
    