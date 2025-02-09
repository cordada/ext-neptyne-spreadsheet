"""remove stripeuser table

Revision ID: 60d36be2e019
Revises: 2631ed812fa3
Create Date: 2023-01-08 22:44:28.142264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "60d36be2e019"
down_revision = "2631ed812fa3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stripe_subscription", sa.Column("user_id", sa.Integer(), nullable=True)
    )
    op.drop_constraint(
        "stripe_subscription_stripe_user_id_fkey",
        "stripe_subscription",
        type_="foreignkey",
    )
    op.create_foreign_key(None, "stripe_subscription", "user", ["user_id"], ["id"])
    op.drop_column("stripe_subscription", "stripe_user_id")
    op.add_column("user", sa.Column("stripe_uid", sa.Text(), nullable=True))
    op.create_unique_constraint(None, "user", ["stripe_uid"])
    op.drop_constraint("user_stripe_id_fkey", "user", type_="foreignkey")
    op.drop_column("user", "stripe_id")
    op.drop_table("stripe_user")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("stripe_id", sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_foreign_key(
        "user_stripe_id_fkey", "user", "stripe_user", ["stripe_id"], ["id"]
    )
    op.drop_constraint(None, "user", type_="unique")
    op.drop_column("user", "stripe_uid")
    op.add_column(
        "stripe_subscription",
        sa.Column("stripe_user_id", sa.TEXT(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "stripe_subscription", type_="foreignkey")
    op.create_foreign_key(
        "stripe_subscription_stripe_user_id_fkey",
        "stripe_subscription",
        "stripe_user",
        ["stripe_user_id"],
        ["id"],
    )
    op.drop_column("stripe_subscription", "user_id")
    op.create_table(
        "stripe_user",
        sa.Column("id", sa.TEXT(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="stripe_user_pkey"),
    )
    # ### end Alembic commands ###
