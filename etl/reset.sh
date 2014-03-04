grep -e "Ag" ../agau.dat | python extrame_price_reducer.py 0 > extrame_prices.ag
grep -e "Ag" ../agau.dat | python tipping_point_variations.py > tipping_points.ag 
grep -e "Ag" ../agau.dat | python backto_open_reducer.py > backto_open.ag;
grep -e "Ag" ../agau.dat | python boundary_prices.py --fix > boundary_prices.ag;

echo 'cat boundary_prices.ag | python stage_alter_direction.py\n';
cat boundary_prices.ag | python stage_alter_direction.py > stage_alters.ag

echo 'cat stage_alters.ag | python stage_direction_relations.py\n';
cat stage_alters.ag | python stage_direction_relations.py;

echo 'cat stage_alters.ag | python stage_threshold_odds.py day\n';
cat stage_alters.ag | python stage_threshold_odds.py day;
