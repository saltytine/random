#!/bin/bash

echo "Speak the incantation:"
read -r input
cleaned=""
input_len=${#input}
for (( i=0; i<input_len; i++ )); do
    c="${input:$i:1}"
    if [[ "$c" =~ [a-zA-Z] ]]; then
        cleaned+="$c"
    fi
done
cleaned_lower=$(echo "$cleaned" | tr 'A-Z' 'a-z')
is_palindrome=1
len=${#cleaned_lower}
for (( i=0; i<len/2; i++ )); do
    left="${cleaned_lower:$i:1}"
    right="${cleaned_lower:$((len - i - 1)):1}"
    if [[ "$left" != "$right" ]]; then
        is_palindrome=0
        break
    fi
done
if (( is_palindrome == 1 )); then
    echo "smth about a mirror"
else
    echo "darkness is grabbing my ass!"
fi

