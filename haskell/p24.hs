import Data.List

main = do putStrLn $ show $ head $ drop 999999 $ sort $ permutations [0..9]

