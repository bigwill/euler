factorial :: (Num a) => a -> a
factorial 1 = 1
factorial n = n * factorial (n-1)

run :: (Num a, Read a) => a -> a
run n = sum [read [x] | x <- show $ factorial n]

main = do putStrLn $ show $ run 100