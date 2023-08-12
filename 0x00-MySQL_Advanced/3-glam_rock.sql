-- list all bands with "GlAm rock" as their main style ranked by their logevity
-- dump file metal_bands.sql
SELECT band_name, (IFNULL(split, '2022') - formed) as lifespan
from metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
