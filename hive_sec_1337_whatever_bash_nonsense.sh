read -p "Enter a number: " n
[[ $n =~ ^-?[0-9]+$ ]] || { echo "Invalid input!"; exit; }
(( n % 2 == 0 )) && echo "even" || echo "odd"
