-- Rank country origins of bands by number of fans
-- Db dump metal_bands.sql
SELECT origin, SUM(fans) as nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC

