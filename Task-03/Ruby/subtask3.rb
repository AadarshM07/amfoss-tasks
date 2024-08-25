
puts "Enter the number of rows for the diamond (n): "  #input
n = gets.to_i

middle = (n / 2) + 1

# Generate the upper part
(1..middle).each do |i|
  print ' ' * (middle - i)
  print '*' * (2 * i - 1)
  puts
end

# Generate the lower part 
(middle-1).downto(1) do |i|
  print ' ' * (middle - i)
  print '*' * (2 * i - 1)
  puts
end
