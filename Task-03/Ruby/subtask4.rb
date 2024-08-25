# Read the value of n from input.txt
input= File.read('input.txt')
n=input.read.to_i
input.close()

# Open the output.txt file for writing
File.open('output.txt', 'w') do |file|
  middle = (n / 2) + 1

  (1..middle).each do |i|
    line = ' ' * (middle - i) + '*' * (2 * i - 1)
    file.puts(line)
  end

  (middle-1).downto(1) do |i|
    line = ' ' * (middle - i) + '*' * (2 * i - 1)
    file.puts(line)
  end
end
