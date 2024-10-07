from typing import Any
from wildlife_tracker.animal_management.animal import MigrationPath

class Migration:

    def __init__(self,
                 migration_id: int,
                 migration_path: MigrationPath,
                 start_date: str,
                 current_date: str,
                 current_location: str,
                 status: str = "Scheduled"
                 ) -> None:
        self.migration_id = migration_id
        self.migration_path= migration_path
        self.start_date = start_date
        self.current_date = current_date
        self.current_location = current_location
        self.status = status
        pass

    def cancel_migration(migration_id: int) -> None:
        pass

    def get_migration_details(migration_id: int) -> dict[str, Any]: 
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:  #migration
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None: #migration
        pass



