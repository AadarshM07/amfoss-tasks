defmodule DiamondPattern do
  def run do
    # Read the number of rows for the diamond from input.txt
    {:ok, n} = File.read("input.txt")
    n = String.trim(n) |> String.to_integer()

    middle = div(n + 1, 2)

    # Open output.txt for writing
    {:ok, file} = File.open("output.txt", [:write])

    # Generate the upper part of the diamond
    Enum.each(1..middle, fn i ->
      spaces = middle - i
      stars = 2 * i - 1
      IO.write(file, "#{String.duplicate(" ", spaces)}#{String.duplicate("*", stars)}\n")
    end)

    # Generate the lower part of the diamond
    Enum.each((middle - 1)..1, fn i ->
      spaces = middle - i
      stars = 2 * i - 1
      IO.write(file, "#{String.duplicate(" ", spaces)}#{String.duplicate("*", stars)}\n")
    end)

    # Close the file
    File.close(file)
  end
end

DiamondPattern.run()
