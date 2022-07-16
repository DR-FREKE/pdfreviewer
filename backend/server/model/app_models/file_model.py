from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.connection import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True);
    file_title = Column(String(255), nullable=False);
    file_url = Column(String(255), nullable=False);
    description = Column(String, nullable=False);
    reference_num = Column(Integer, nullable=False);
    status = Column(Integer, ForeignKey('status.id'));
    update_reason = Column(String, default=None, nullable=True);
    total_reviews = Column(Integer, default=0);
    downloadable = Column(Boolean, default=False);
    user_id = Column(Integer, ForeignKey('users.id'));
    created_at = Column(DateTime, default=datetime.utcnow);

    status_rel = relationship("Status", back_populates="files");
    owner = relationship("User", back_populates="files");
