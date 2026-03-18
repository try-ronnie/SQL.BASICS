SELECT owner.name
FROM owner
INNER JOIN cat_owners
ON owner.id = cat_owners.owner_id WHERE cat_owners.cat_id = 3;


