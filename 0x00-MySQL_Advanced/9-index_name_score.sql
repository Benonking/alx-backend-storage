-- create index idx_name_first_score on table names (muiltiple index)

CREATE INDEX idx_name_first ON
names(name(1), score);
