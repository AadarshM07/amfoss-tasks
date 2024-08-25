import System.IO

diamondPattern :: Int -> [String]
diamondPattern n = bottomRows ++ topRows
  where
    topRows = [spaces i ++ stars (n - 2 * i) | i <- [0..n `div` 2]]
    bottomRows = reverse [spaces i ++ stars (n - 2 * i) | i <- [1..n `div` 2]]
    stars x = replicate x '*'
    spaces x = replicate x ' '

main :: IO ()
main = do
    input <- readFile "input.txt"
    let n = read input :: Int

    let diamond = diamondPattern n

    writeFile "output.txt" (unlines diamond)
