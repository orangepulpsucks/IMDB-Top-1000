copy Movie(Poster_Link,Series_Title,Released_Year,Certificate,
           Runtime,Genre,IMDB_Rating,Overview,Meta_score,Director,
           Star1,Star2,Star3,Star4,No_of_Votes,Gross)
from '/docker-entrypoint-initdb.d/seed_data/imdb_top_1000.csv'
delimiter ','
csv header;

-- copy set(set_num, name, year, theme_id, num_parts)
-- from '/docker-entrypoint-initdb.d/seed_data/sets.csv'
-- delimiter ','
-- csv header;

-- copy inventory(id, version, set_num)
-- from '/docker-entrypoint-initdb.d/seed_data/inventories.csv'
-- delimiter ','
-- csv header;

-- copy inventory_set(inventory_id, set_num, quantity)
-- from '/docker-entrypoint-initdb.d/seed_data/inventory_sets.csv'
-- delimiter ','
-- csv header;

-- copy part_category(id, name)
-- from '/docker-entrypoint-initdb.d/seed_data/part_categories.csv'
-- delimiter ','
-- csv header;

-- copy part(part_num, name, part_cat_id)
-- from '/docker-entrypoint-initdb.d/seed_data/parts.csv'
-- delimiter ','
-- csv header;

-- copy color(id, name, rgb, is_trans)
-- from '/docker-entrypoint-initdb.d/seed_data/colors.csv'
-- delimiter ','
-- csv header;

-- copy inventory_part(inventory_id,part_num,color_id,quantity,is_spare)
-- from '/docker-entrypoint-initdb.d/seed_data/inventory_parts.csv'
-- delimiter ','
-- csv header;