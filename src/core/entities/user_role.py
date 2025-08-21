# from dataclasses import dataclass, field
# from datetime import datetime
# from typing import Optional, List

# @dataclass
# class UserRole:
#     """Junction entity for User-Role many-to-many relationship."""
    
#     user_id: int
#     role_id: int
#     assigned_at: Optional[datetime] = None
#     assigned_by: Optional[int] = None  # User ID who assigned the role
    
#     def __post_init__(self):
#         """Validate user role assignment."""
#         if self.user_id <= 0:
#             raise ValueError("User ID must be positive")
        
#         if self.role_id <= 0:
#             raise ValueError("Role ID must be positive")
        
#         if self.assigned_at is None:
#             self.assigned_at = datetime.utcnow()