defmodule DiamondPattern do
  def run do
    IO.write("Enter the number of rows for the diamond (n): ")
    n = IO.gets("") |> String.trim() |> String.to_integer()

    middle = div(n + 1, 2)

    # Generate the upper part of the diamond
    Enum.each(1..middle, fn i ->
      spaces = middle - i
      stars = 2 * i - 1
      IO.puts("#{String.duplicate(" ", spaces)}#{String.duplicate("*", stars)}")
    end)

    # Generate the lower part of the diamond
    Enum.each((middle - 1)..1, fn i ->
      spaces = middle - i
      stars = 2 * i - 1
      IO.puts("#{String.duplicate(" ", spaces)}#{String.duplicate("*", stars)}")
    end)
  end
end

DiamondPattern.run()
