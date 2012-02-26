factors :: Integer -> [Integer]
factors x = factors' x 2 []

factors' :: Integer -> Integer -> [Integer] -> [Integer]
factors' 1 _ r = r
factors' x p r = if x `mod` p == 0 then (factors' (x `div` p) p (p:r)) else (factors' x (p+1) r)

main = do putStrLn $ show $ head $ factors 600851475143
