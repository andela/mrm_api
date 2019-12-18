from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None

cbr_data = {"createBlock": {"block": {"officeId": 2, "name": "Blask"}}}
create_block_response = build(
    data=cbr_data
)

bc_error = error_item
bc_error.message = "Ec Block already exists"
bc_error.locations = [{"line": 3, "column": 3}]
bc_error.path = ["createBlock"]
bc_data = {"createBlock": null}

block_creation_with_duplicate_name_response = build(
    error=bc_error.build_error(bc_error),
    data=bc_data
)

cb_error = error_item
cb_error.message = "Office not found"
cb_error.locations = [{"line": 3, "column": 3}]
cb_error.path = ["createBlock"]
cb_data = {"createBlock": null}
create_block_with_non_existing_office_response = build(
    cb_error.build_error(cb_error),
    cb_data
)

ub_data = {"updateBlock": {"block": {"name": "Block A", "id": "1"}}}
update_block_response = build(
    data=ub_data
)

db_data = {"DeleteBlock": {"block": {"name": "Ec", "id": "1"}}}
delete_block_response = build(
    data=db_data
)

dne_error = error_item
dne_error.message = "Block not found"
dne_error.locations = [{"line": 3, "column": 3}]
dne_error.path = ["DeleteBlock"]
dne_data = {"DeleteBlock": null}
delete_non_existent_block_response = build(
    dne_error.build_error(dne_error),
    dne_data
)

une_error = error_item
une_error.message = "Block not found"
une_error.locations = [{"line": 3, "column": 3}]
une_error.path = ["updateBlock"]
une_data = {"updateBlock": null}
update_non_existent_block_response = build(
    une_error.build_error(une_error),
    une_data
)
