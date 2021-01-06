defmodule WordCount do
  # Matches pontuaction symbols
  @pontuation_regex ~r<!|&|@|\$|%|^|&|,|\^|:>

  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    sentence
    |> String.downcase()
    |> String.replace("_", " ")
    |> String.replace(@pontuation_regex, "")
    |> String.split()
    |> Enum.reduce(
      %{},
      fn item, acc ->
        Map.update(acc, item, 1, &(&1 + 1))
      end
    )
  end
end
