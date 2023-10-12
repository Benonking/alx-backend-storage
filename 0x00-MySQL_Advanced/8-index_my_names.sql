-- sql scrip that creates an index on 
-- a table names and first letter of names must be indexed

CREATE INDEX idx_name_first
ON names(name(1));
