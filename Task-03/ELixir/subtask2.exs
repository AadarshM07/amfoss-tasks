defmodule FileCopy do               
  def run do
    content = File.read!("input.txt")
    File.write!("output.txt", content)
    IO.puts "Content copied to output.txt"
  end
end

FileCopy.run()
