diamondPattern :: Int -> IO ()
diamondPattern n = mapM_ putStrLn $  bottomRows ++ topRows
  where
    topRows = [spaces i ++ stars (n - 2 * i) | i <- [0..n `div` 2]]
    bottomRows = reverse [spaces i ++ stars (n - 2 * i) | i <- [1..n `div` 2]]
    stars x = replicate x '*'
    spaces x = replicate x ' '
    
main = do
    putStr "Enter a number: "
    input <- getLine  -- Read the input as a str
    
    -- Convert the input to an int
    let n = read input :: Int
    diamondPattern n