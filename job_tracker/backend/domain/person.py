from job_tracker.models.position import Position


class Person:
    id: str
    full_name: str
    first_name: str
    last_name: str
    current_position: Position
    previous_positions: list[Position]