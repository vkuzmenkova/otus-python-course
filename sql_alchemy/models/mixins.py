from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    func
)


class TimestampMixin:
    changed_at = Column(DateTime, nullable=False, default=datetime.utcnow,
                        server_default=func.now())
