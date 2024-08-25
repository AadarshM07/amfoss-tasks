content = File.read('input.txt')  #open the file input.txt

File.open('output.txt', 'w') do |file|   #open the output file
  file.write(content)
  puts "Task successfull"
end
