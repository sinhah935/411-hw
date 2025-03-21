from typing import Optional
from wildlife_tracker.migration_tracking.migration_path import MigrationPath
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationManager:
    def __init__(self) -> None:
        paths: dict[int, MigrationPath] = {}
        migrations: dict[int, Migration] = {}

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migration_paths() -> list[MigrationPath]:       
        pass

    def get_migration_path_by_id(path_id: int) -> MigrationPath:    
        pass

    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:    
        pass

    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:   
        pass

    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass