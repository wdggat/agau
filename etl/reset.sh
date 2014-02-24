grep -e "Ag" ../agau.dat | python extrame_price_reducer.py > extrame_prices.ag
grep -e "Ag" ../agau.dat | python tipping_point_variations.py > tipping_points.ag 
grep -e "Ag" ../agau.dat | python backto_open_reducer.py
grep -e "Ag" ../agau.dat | python boundary_prices.py > boundary_prices.ag

