from sqlalchemy import MetaData, Table, Integer, Column, String, ForeignKey

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False, unique=True),
)

statistics = Table(
    "statistics",
    metadata,
    Column(
        "id",
        Integer,
        ForeignKey("users.id"),
        primary_key=True,
    ),
    Column(
        "username",
        String,
        ForeignKey("users.username"),
        nullable=False,
        unique=True,
    ),
    Column(
        "matches",
        Integer,
        nullable=False,
        default=0,
    ),
    Column(
        "wins",
        Integer,
        nullable=False,
        default=0,
    ),
    Column(
        "good_word",
        Integer,
        nullable=False,
    ),
)
