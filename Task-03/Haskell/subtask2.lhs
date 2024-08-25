import System.IO

main :: IO ()
    inputHandle <- openFile "input.txt" ReadMode
    content <- hGetContents inputHandle
    hClose inputHandle  --closing the file

    --opening the output.txt for writing
    outputHandle <- openFile "output.txt" WriteMode
    hPutStr outputHandle content
    hClose outputHandle   --closing the file