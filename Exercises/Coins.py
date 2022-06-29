change = float(input())
current_number = int(change * 100)


coin_counter = 0

coin_counter += current_number // 200
current_number %= 200
coin_counter += current_number // 100
current_number %= 100
coin_counter += current_number // 50
current_number %= 50
coin_counter += current_number // 20
current_number %= 20
coin_counter += current_number // 10
current_number %= 10
coin_counter += current_number // 5
current_number %= 5
coin_counter += current_number // 2
current_number %= 2
coin_counter += current_number // 1
current_number %= 1

print(coin_counter)
