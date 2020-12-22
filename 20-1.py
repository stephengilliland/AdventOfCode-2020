from itertools import combinations

inpt = ["Tile 3209:",
".##.####..",
"....#....#",
"#.##.#....",
"#.....#...",
"#..#......",
".##.##..##",
"##.#......",
"#.######..",
"....##..#.",
"....######",
"Tile 1409:",
".##.####..",
"...#...#.#",
"#....#.#..",
"#...##.##.",
".###....#.",
"..#....#..",
"##...#....",
".....#....",
"......#..#",
".#.#.#####",
"Tile 1039:",
"##...#.##.",
"..#.##..##",
"#......#.#",
"#.#.#....#",
"####...#.#",
"#..#.....#",
"#.....#...",
".#..#...##",
"..#....##.",
"#.#.#.####",
"Tile 3037:",
"#..##.#.##",
"##.......#",
".#......##",
".........#",
"..........",
"...#.#....",
"#...####.#",
"...#..#.##",
".........#",
"#..###.#..",
"Tile 1427:",
"#..#.#..#.",
"......##..",
"#.......##",
"..#..#....",
"#...###.#.",
".......#.#",
".#.......#",
".#...##...",
"......#...",
".#.#.#....",
"Tile 2879:",
"###..#.#..",
"#....##...",
"..#..#....",
"#.....#...",
".#.......#",
"#......#.#",
".#.#.....#",
"#.....#..#",
"..........",
"####.##...",
"Tile 3617:",
"...#.#..#.",
"#...#....#",
"...#.#...#",
"#.....#..#",
"#........#",
"......#..#",
"#.......##",
"....#....#",
".##......#",
"##.####..#",
"Tile 1801:",
"..###...##",
"#.###.....",
".###....##",
"#...#.....",
"#........#",
".#.##...##",
"#.#..#...#",
"###.#....#",
"#.#......#",
"##.##.##.#",
"Tile 3221:",
".##.###.##",
"#..##....#",
"#.#.#.#.#.",
"#...#.#...",
"#.....##..",
"......#..#",
"..........",
"#...#.##..",
"...#...#..",
".###...##.",
"Tile 1987:",
".##.###.##",
".##....###",
"#..#.#.##.",
".#..##...#",
".....##..#",
".......#..",
"#......##.",
"#.#.....##",
"......##.#",
"###...#...",
"Tile 2917:",
"#.#..#..##",
"......##..",
".#........",
"##.......#",
".#.......#",
"..#.#.#...",
"...#.#...#",
"...##..##.",
"........##",
".#.#.#.#.#",
"Tile 1297:",
"#..#.##...",
"...##..#.#",
"....#...##",
"##.#.#.##.",
"#.......##",
"#.........",
"####......",
"#.........",
"#.........",
".#....###.",
"Tile 1613:",
"#...####..",
".....#.###",
".....#.##.",
"#.#......#",
"...##...##",
"#.........",
".##..#....",
"....#.....",
"..........",
"..##.##.##",
"Tile 1481:",
"#.##..##..",
"#.#..#.#.#",
"..........",
"##..#..#..",
"..##....#.",
"..#...#.#.",
"#..#......",
"##.....#..",
"...#.....#",
".#.####..#",
"Tile 3779:",
"##.#......",
"...#.....#",
"...#......",
"##.##.#..#",
"##......##",
"#..#...#..",
"....#.#.##",
"#......#.#",
".......#.#",
"#...###..#",
"Tile 3121:",
".#.#..#.##",
"#..#.#.#..",
"....#.....",
"#..#.#.#..",
".......###",
"#.#......#",
"#.....#..#",
"#.#.#....#",
"...#.#....",
".##..#.##.",
"Tile 1913:",
"##..##...#",
".......##.",
"##..#..#..",
"##..#....#",
"..........",
"#.#...#..#",
".........#",
".......###",
"......#.##",
".#...##.#.",
"Tile 3929:",
".#...#####",
".#.......#",
"#...#.....",
"..#.##....",
"###..##...",
"..#.....#.",
"......#...",
"#........#",
".........#",
"##..##....",
"Tile 3947:",
"#...#.#..#",
"......#...",
"#.#...#...",
"........#.",
"..#.#.....",
"#....#.##.",
"..........",
"##..#.....",
"##....#.##",
"##.###.###",
"Tile 2663:",
".#.#.#.##.",
"....###...",
"#..#......",
"#...#.####",
"##......#.",
"#.###.#..#",
"#..#...#.#",
"..#......#",
"##......#.",
"....##..##",
"Tile 3499:",
"########.#",
"....#..#.#",
".#.##....#",
"......#...",
".#..#..#..",
"#..#.....#",
"###...##..",
"#..##.....",
"#.#...#..#",
"#..###.##.",
"Tile 3877:",
"..######.#",
"..#.#....#",
".#........",
"##..##..##",
".#.#...#.#",
".....#.###",
".........#",
"#........#",
".....#....",
"#..#.###.#",
"Tile 2251:",
"#.#.......",
"..##...#.#",
"#..#..##.#",
".#...#..#.",
"##........",
"##.##.###.",
"..#...#...",
"..#......#",
"#..#..#...",
"##..#.#...",
"Tile 2357:",
".....#.#..",
".#.#......",
"#...###...",
".#..##.#.#",
"#........#",
"...#....#.",
"#.........",
".##.##.#.#",
"###...####",
"...##....#",
"Tile 2381:",
"...####.##",
"#.......#.",
"......##..",
"..#.##.#..",
"#..###....",
"##.#..#...",
".##..#....",
"##..#..#..",
"#....#..#.",
"#.#...#.#.",
"Tile 1693:",
"###.......",
"#...####.#",
"##.##.....",
"#..#.....#",
"#.#......#",
"...#.#....",
"....#.##.#",
"..#.#.....",
"..#.#...#.",
".##..###..",
"Tile 3697:",
"....#.#..#",
"#.........",
"#.#...#...",
"..#....##.",
"#....##.#.",
"#........#",
".#...#....",
"#...#..#..",
"#.........",
"###....#..",
"Tile 3307:",
"####..##.#",
"........#.",
"#........#",
"#..##.##..",
"#...##..#.",
"...##.##..",
"#.....#..#",
"##.......#",
"......#.##",
"##.#..#...",
"Tile 1823:",
"#.##...##.",
"......#...",
"#.........",
"#.........",
"#.##....##",
"##..##.#.#",
".#........",
".#....####",
"#......#..",
"#..#..##..",
"Tile 2837:",
".#...#.#.#",
"..##.....#",
"##....##.#",
"#.#..##.##",
"###.#....#",
".#....#...",
"..#...#...",
".#.#......",
"#...#.....",
"#....###..",
"Tile 1483:",
"##.##...#.",
".##..##...",
".##...#.#.",
"#...#....#",
"#..##..#..",
"#.......##",
".....#...#",
"..###.#..#",
"#...##.#.#",
"#...#.####",
"Tile 3889:",
".#.#.##.#.",
"...###.#.#",
"#.....##.#",
"......#...",
".#..#.##.#",
"##....#...",
".###.....#",
"#..#...#.#",
"##....#...",
"#.#..##..#",
"Tile 2677:",
".......###",
"#.#..#..#.",
".#...##..#",
".........#",
"........##",
".......#.#",
"...#...#.#",
".......#..",
"..#...####",
"..#..####.",
"Tile 1021:",
"#...######",
"..#.#.....",
"........##",
"#....#..##",
"#....##.#.",
"..#......#",
"#..#.#.#.#",
"#.....#...",
".#.#......",
".####.###.",
"Tile 3067:",
"#####..#.#",
"##..#.##..",
"#.###...#.",
"###...#..#",
"#......#..",
"###......#",
"#.....#...",
".....#..##",
"#...#..###",
"..#.#..#..",
"Tile 1559:",
"..#...#.##",
"#.......##",
"....#....#",
"..##.#..##",
"##..#..#.#",
"##.....##.",
"....#..##.",
"#.#...##..",
"....#..#..",
"#..#.....#",
"Tile 3917:",
"#.######..",
".#......#.",
"#...#...##",
".......#..",
"##......#.",
"#.......#.",
"#..##..###",
"....##...#",
".....#....",
"###...#...",
"Tile 3823:",
"...####.##",
"....#..#..",
"......#.#.",
"......#...",
"...#..#...",
"#..##.#...",
"..#......#",
"#...#..###",
".#.......#",
".###..#.#.",
"Tile 1307:",
"...#.....#",
"##.#.....#",
"###......#",
".....###.#",
"#..##.##..",
"#.........",
"..##.....#",
"#....#..#.",
"#.#.#....#",
"#.##...#.#",
"Tile 1949:",
"....##.#.#",
"#...#.....",
"....#.#.#.",
"#...#.....",
"#..#......",
"........##",
".#..#.#.##",
".....#...#",
"..........",
"..##....##",
"Tile 1571:",
"#..#####.#",
".....##.##",
"..#.#..#..",
"#..#.#....",
".....#...#",
"...#.....#",
".#.....##.",
"##...#...#",
".....#...#",
".#.#...###",
"Tile 2777:",
"#.###.#..#",
"#....#..##",
"#........#",
"#....#..#.",
"#.#.......",
".#.#...#.#",
"..#.##....",
"##........",
".....##...",
"..#.###.##",
"Tile 3019:",
".##.#####.",
"...#..##..",
"...#....##",
".........#",
"#.........",
"#....#...#",
"#.........",
".......#.#",
"..##.....#",
".##...#...",
"Tile 2579:",
"###.######",
"##.....#.#",
".#....##.#",
"#.#...#..#",
"#...##....",
"....#....#",
"#.#...#..#",
"##.......#",
"###......#",
"#..##.####",
"Tile 2887:",
"..##..###.",
"####.##.##",
".##..#...#",
".#....#...",
"..#.....##",
"#..#......",
"....##...#",
"..........",
"..##...#..",
".#..##....",
"Tile 2287:",
"..#.####..",
"##..#.....",
"....##..#.",
".....##...",
"##..###.##",
"#....##.#.",
"##....#...",
"..........",
"...#......",
".#.#..#.##",
"Tile 1637:",
"###.#...#.",
"#......###",
"....###..#",
"..#..#...#",
"....#..#.#",
"....#.....",
".........#",
"#....#.#.#",
"...###...#",
".##..#.#.#",
"Tile 1901:",
".##.......",
".#........",
"##..##....",
"......#.#.",
"....#..#..",
"#.#...##.#",
".#.....#.#",
"..........",
"#..#..#..#",
".#.##....#",
"Tile 2957:",
"##.###..#.",
"..###..#.#",
"#...#.#...",
".....#.###",
"#........#",
"......#...",
".#......##",
"##...#..##",
".#.#.#...#",
"..###.##..",
"Tile 2699:",
"..#.#.###.",
".#...#.#.#",
"#.....##..",
"#...#.#..#",
".....#..##",
".....###..",
"#..#......",
"##.#.....#",
"##.#..#..#",
"#..#...#..",
"Tile 2081:",
"..#...#...",
"....#.....",
"#.#.#.....",
"..##.##..#",
"...#...#.#",
".####.....",
".##..#..#.",
"#.....##..",
".........#",
"#..##.###.",
"Tile 2383:",
".####.###.",
"...##....#",
"...#....#.",
"...#.....#",
"##......#.",
"...#......",
"##.#.#...#",
"##.#...#.#",
"........##",
".##.##.#.#",
"Tile 3407:",
"##..#.###.",
"#..#..#...",
"#.......#.",
".#.......#",
"###...#..#",
"........##",
"#..###...#",
"#.....##.#",
"..##......",
".####.....",
"Tile 2503:",
".###..#...",
".......###",
"##....#.#.",
".##.....#.",
".#.......#",
"##.#..#...",
".#.......#",
"....######",
"...#..#...",
"...######.",
"Tile 1249:",
"##.#.#####",
"..#.......",
".#.......#",
"..#.......",
".......#..",
"###....#..",
"...#.....#",
".......###",
"#.....#..#",
"..##...##.",
"Tile 3541:",
"..##.#####",
".....#....",
"..##...#.#",
"..........",
".#....##..",
"..........",
"..#...##.#",
"##.#..#.#.",
"......#..#",
"..#..#...#",
"Tile 1447:",
".#...####.",
"#.#..#...#",
".....#.#.#",
".....#....",
".....#..#.",
"#.....#..#",
"..##...#.#",
"#.##......",
"..#...#.#.",
".#.##.#..#",
"Tile 2969:",
"#..###.#..",
"#.#..#....",
"#........#",
"#..#.#.#..",
".#.......#",
"..#..#.#.#",
"#........#",
".........#",
"#...#.#...",
".###......",
"Tile 1621:",
".#.#.#....",
".#..#....#",
"....##...#",
"#.#....#..",
"..........",
"##.#..##.#",
"#.#...#..#",
"#...#.....",
".##....#..",
"#..#.##.##",
"Tile 2129:",
"######..#.",
"....#....#",
"#........#",
"#.....##..",
"##.#...#.#",
"##.##....#",
"#.........",
"##..##....",
"#.#...#..#",
".#.....##.",
"Tile 1741:",
".....#....",
"#......#..",
"........#.",
"#....#..#.",
".......#.#",
"#......#.#",
"#...##..##",
"##.....#..",
"..##.#..#.",
"....#...#.",
"Tile 1549:",
"#.##.#...#",
"#.........",
".#.....#.#",
".#.#.#....",
".....#....",
"......#.##",
"......####",
"#.#.#..#..",
"#...#.....",
"..#..##..#",
"Tile 1063:",
"####.#####",
"#........#",
"##........",
"##........",
"........#.",
"#.#....#..",
"....#.....",
".##.###...",
"#.........",
"##.##.#.##",
"Tile 3931:",
".##......#",
".#.......#",
"...#....#.",
"#...#.....",
"....#...#.",
"..#...##.#",
"#.#.#..#.#",
"..........",
"#..#....#.",
".#..#.#...",
"Tile 1367:",
".##.#.....",
"##.#......",
"###....#..",
".....#...#",
"##...###..",
"#.#....#..",
"...##....#",
"#..#...#..",
"..#...#...",
"#..#....##",
"Tile 1783:",
"#.#####...",
"......##.#",
"#....#.###",
"..#......#",
"#.........",
"###......#",
"##........",
"##....#...",
"#.#.#..#.#",
"#####.#...",
"Tile 1777:",
"#.....####",
"#.##..#...",
".##.#..##.",
"..#.#.#...",
"#....#...#",
"#......#..",
"..#.#.#...",
"#.#.......",
"#.......##",
"#.##..##..",
"Tile 1487:",
"...###.###",
"..........",
"##.......#",
"#.#.......",
"#....#..#.",
"..#..#....",
"#.#..#..##",
".#.##.#...",
"........#.",
"#.####.#..",
"Tile 2039:",
".#.#######",
"..#...##..",
"..#..#...#",
"##......##",
"#......#.#",
"#...##...#",
"...#...#..",
"#.##.#....",
"....####.#",
".#..#..##.",
"Tile 2833:",
".##.#.#..#",
".....#.#.#",
"#.....####",
"#...#....#",
"#.......##",
"#......###",
"......##..",
"##.#..##..",
"##.##..#.#",
"#.#...#.##",
"Tile 3301:",
"..#.####.#",
".#.#...##.",
"#.#.##.#..",
".##.#.....",
"..#......#",
"..........",
"#..##.#.#.",
"#.......#.",
"..........",
".###...###",
"Tile 2963:",
"..##.##.#.",
"##....#.##",
"#.#.#.....",
"##.......#",
"....#.....",
".....#....",
"#.#...#...",
".#.......#",
"....#....#",
"..##..#.##",
"Tile 2477:",
"###.#..###",
"......#...",
"#.##.#..##",
"###...#..#",
"##....#...",
"...##...#.",
"..#....#..",
"#.#....###",
"#.#.#.#...",
"..##.....#",
"Tile 2659:",
"####..##..",
"..#.##....",
"#......#..",
"...#...###",
"#....###.#",
".........#",
"#.#.......",
"#.#.#..#.#",
"##.....#.#",
"#...#..###",
"Tile 1051:",
"###.#.#..#",
"#.#..#....",
"#.......#.",
"#...##...#",
"#....#...#",
".....#....",
"##..##..#.",
"..#......#",
"#.........",
"..#####.#.",
"Tile 3637:",
".#...###.#",
"#.#.#.....",
"..#..#.###",
"...##.....",
"#..#....##",
".........#",
"#.......#.",
"..##.#..#.",
"##......##",
"#######.##",
"Tile 1697:",
"##.###.#..",
"....#...##",
"#.......##",
"....#....#",
"#.....#...",
"#.##......",
"##.......#",
"#....#..##",
"#.........",
"...#...##.",
"Tile 1499:",
"#...####.#",
"..#.##.#.#",
".##.....##",
".##....#..",
".##......#",
".#......##",
"#..##.###.",
"#.#....#..",
".##.#.#.##",
".#.#.#.#..",
"Tile 2543:",
"#.##.#.##.",
".....#....",
"...#.#...#",
"#...#..#.#",
"..##....#.",
"##..#..#.#",
"...#......",
"#.##......",
"###...####",
"#..####.#.",
"Tile 2269:",
"###.#..###",
"..#..#...#",
"#..#.##..#",
"#......##.",
".#..#.....",
"#.....#...",
"#..#.#....",
".#......##",
".###..#...",
".###......",
"Tile 2029:",
"##.###....",
".#.....##.",
".........#",
"#.#......#",
"##.#....#.",
".##.#.....",
"#.........",
"#...#....#",
".........#",
"...###.##.",
"Tile 2141:",
"#.#.#..#.#",
"..##.....#",
"#.........",
".##......#",
"#.#..#.#..",
"#........#",
"##..##.#..",
".#........",
"#.#.....##",
".....##...",
"Tile 1601:",
".......##.",
"##.#.##.##",
"####...#..",
"#.##...###",
"##...#...#",
"#......#..",
"#..#....##",
"##......#.",
"..##...#.#",
"#..###..##",
"Tile 1049:",
"..#.##.#.#",
"##........",
".#......#.",
"#...###..#",
"........#.",
"....#.#...",
".###..###.",
".#....#...",
"#....#...#",
"#....#..#.",
"Tile 1543:",
"###...#..#",
".........#",
"#.....##.#",
".#...#...#",
"....#.#...",
"...#.....#",
"#..#.....#",
"..#.......",
"#......#..",
"..#..###..",
"Tile 2069:",
"##..#.#.##",
"#...#....#",
"#...##....",
"#..#......",
"#...#....#",
"....#....#",
".........#",
"#.....###.",
"...#.....#",
".##.#.#...",
"Tile 2687:",
"#.#..#....",
"#.#..#....",
"#....#....",
"..........",
".....#...#",
"#........#",
"....#.....",
"...##...#.",
"#.......#.",
"##....#.##",
"Tile 3691:",
".######.#.",
"..#..##..#",
"#.....#...",
"......#...",
"#.##.#..##",
"##....#..#",
"....#....#",
".##..#....",
".........#",
".#..#.#..#",
"Tile 2521:",
"#..#.###..",
"#.#.......",
"##..##..##",
".....#.#..",
".....#..##",
".###....#.",
"#.....##.#",
"#.....##.#",
"#.#.#...##",
"###.#...#.",
"Tile 1093:",
"#..#######",
"#......#.#",
"..........",
"..#....#.#",
"##.##....#",
"..#..#...#",
".....##...",
"#.....#..#",
"#.#.#.#..#",
"#..##.####",
"Tile 2341:",
".####.#.#.",
"#.#...#..#",
".....#...#",
"#....#..#.",
".........#",
"#......###",
"..#.#.....",
"#.......#.",
"#.#.#.....",
"######....",
"Tile 2903:",
"#.#.###.##",
".#...#....",
"........#.",
"..#.......",
"#......##.",
".#...#...#",
".#...#....",
"#.##.....#",
"..........",
"....#..#..",
"Tile 3413:",
"...#.####.",
"#...#...##",
".....#.#.#",
".#.#..#...",
".#.......#",
"#.......#.",
"#....##...",
"..#....#..",
"......##..",
"....#.####",
"Tile 2213:",
"###...####",
"..#....#..",
"..##...#..",
"...#.#....",
"#..##.#.#.",
"..#..##...",
".##..##...",
"........##",
".#..#.....",
"##..#.####",
"Tile 1931:",
"#.#.##.###",
".........#",
"........##",
"..........",
".#.....##.",
"#.#.#....#",
"#.....#..#",
".......#..",
".#........",
"#.......#.",
"Tile 1373:",
".###.#..##",
".#.....#.#",
".....###..",
"....#...#.",
"..........",
"##..#....#",
"#.........",
"...#...##.",
".......#.#",
"......####",
"Tile 1229:",
"#..#..#.##",
"..........",
".#........",
".......##.",
".......#.#",
"#..##....#",
"#.#....#.#",
".#.....#.#",
".........#",
".##..###.#",
"Tile 1361:",
"...#.....#",
".#......#.",
"#.#.#....#",
"#........#",
"......#.##",
"#.....##..",
"#.......#.",
"........#.",
"#...#.#.##",
"##.#.#.###",
"Tile 1031:",
"###.#.#.#.",
"#...##....",
"#..#.#...#",
"#...#..#.#",
".#.....#..",
"......#..#",
".###...##.",
"..#.#....#",
"...#...#.#",
"##...#.##.",
"Tile 1451:",
"..#.##.#.#",
"....#..#..",
".#......#.",
".......##.",
"#.#.#.....",
".......#.#",
"##..#...##",
"......#...",
".#........",
".##...#.##",
"Tile 3943:",
"..#.#.##.#",
".........#",
"#........#",
"#..#..#..#",
".#.#......",
".##...#...",
"##....#..#",
"..#.#.....",
"..#.......",
"#..##.###.",
"Tile 2393:",
"...###..#.",
".........#",
".....#..##",
".##....###",
"..........",
"#.........",
".#.###...#",
"..##.....#",
".#.####..#",
".#.#.#..##",
"Tile 1531:",
"..#.#####.",
"#........#",
"...##..#..",
"#..#.....#",
"#........#",
"##...#.#..",
".#......##",
"..........",
"#.#.#.##.#",
"#....##.##",
"Tile 3923:",
"##...#....",
"......##.#",
"...#..#...",
".....#....",
".....#..##",
"#..######.",
".........#",
"#......###",
"##.....#.#",
"#..#.#...#",
"Tile 1471:",
".#.#.#.#.#",
"##...#...#",
"..#.......",
"#.........",
".....#..##",
"#..##.#.#.",
"#........#",
"#...#.....",
"#...#....#",
".#####.##.",
"Tile 1123:",
"#..###...#",
"#.##.##.##",
"##.....#..",
"#.......##",
".......#.#",
".....#.###",
"......#..#",
".....#...#",
"#.#....#..",
"##.#.#..##",
"Tile 1907:",
"###.#....#",
"#..#..#.##",
"...###....",
"#....#...#",
".....#.#.#",
"#....#....",
"#.........",
".#......##",
"#........#",
"###...###.",
"Tile 2371:",
"##.....###",
"..#...#.#.",
"#.......##",
"#.###..#..",
".......##.",
"#..##.#..#",
".#..#..#.#",
"##......##",
".#.....#.#",
".######.#.",
"Tile 1117:",
"####..#..#",
"...##....#",
"#.........",
"#.#..#...#",
"#..##....#",
"#....#....",
".#..###.##",
".#.#..#.##",
"#........#",
"....#..#.#",
"Tile 1553:",
"########.#",
"##.....#.#",
"..#..#.#..",
"..#..#....",
"###......#",
".#..#.#...",
"..#.......",
"........##",
"........#.",
"#.#.......",
"Tile 3709:",
"##..#...##",
"...#.#....",
"#........#",
"...#..#...",
"#.......##",
"#..#.##...",
".........#",
"..#.....##",
"#....#...#",
".###.#..#.",
"Tile 2221:",
"#.####..##",
"....#.#...",
".........#",
".....#..#.",
"....#...#.",
"#..##.#...",
"#..##.....",
"#.#..#..##",
".#...#....",
"##.#.#.##.",
"Tile 1303:",
".#..######",
"..###....#",
"#.........",
"###....#.#",
"..#......#",
"##...#....",
"..........",
"#.....#...",
"#........#",
"#.#.#.###.",
"Tile 3391:",
"##..##...#",
"#..#.....#",
".......##.",
"#..#......",
"....#.....",
"#.##..#..#",
"..###..#.#",
"#.......##",
".......#..",
"#..#.#.#.#",
"Tile 1433:",
"##..#..##.",
"#.........",
"..........",
"....#.....",
".......#..",
"##..#....#",
"#.....#..#",
"..........",
"..#...#.##",
"..#.#...#.",
"Tile 1163:",
".###.##.##",
"#.........",
"#.......#.",
".......#.#",
".........#",
"##....#..#",
"#......##.",
"#....#.#.#",
".........#",
".#...#..#.",
"Tile 2113:",
"###..###.#",
"...#..#...",
"#...##...#",
".........#",
"...#.#....",
".#....#...",
"..#.##....",
"....#.....",
"#..##.#..#",
"##.#...##.",
"Tile 3023:",
".####.####",
"#....#....",
".#...#..#.",
"##......#.",
"#......#..",
".........#",
".......#..",
"#....#.###",
"#..#..##..",
".#.##.##..",
"Tile 1103:",
"......#.##",
"#..#..#...",
"..#.#..#.#",
".#..#....#",
"..##...##.",
"##.##.....",
".#..#.....",
"#.#...#..#",
"..#...#.#.",
"#.#####.#.",
"Tile 3469:",
"..##.#....",
"....##..#.",
"..........",
"#........#",
"##....#..#",
".........#",
"#..#.#.#..",
".........#",
".#..#..###",
"##.#..#...",
"Tile 3671:",
"..#.....##",
".....#....",
".#......#.",
".#...#.#..",
".#........",
"#.##......",
"#.#...#.#.",
"#..#....##",
"..#.......",
"###.######",
"Tile 1213:",
"#..#......",
"...#.....#",
"#.......##",
"....##....",
"....#.#..#",
"#.#......#",
"#.........",
"#..#..#...",
"#....#....",
".#.##.###.",
"Tile 2063:",
".##...##.#",
".......#..",
"#........#",
"..#...#...",
".###.....#",
"#........#",
"#..##.#.#.",
".....#....",
"......#.#.",
".####...#.",
"Tile 1753:",
"#.##.##.##",
"###.#.#..#",
"#........#",
"##....#..#",
"....#.....",
"#....#.##.",
"..#..#....",
"...#.#....",
".....#..##",
"##.##....#",
"Tile 2309:",
"#..#..#.##",
"#.......##",
"#..#......",
".......#.#",
"#..#.....#",
"##.#.#...#",
".#.#....#.",
"#....#....",
".##.......",
"#..#....#.",
"Tile 3767:",
"#......#..",
".#.#..#.#.",
"#........#",
"..#.#.....",
"#....#...#",
".#..#..#..",
"#.....#..#",
"#.........",
"..#....##.",
".##.#.###.",
"Tile 1321:",
"#.####...#",
"#.#...#..#",
"##........",
".......#.#",
".#....#.#.",
".#..##....",
"#.#....#.#",
"........##",
"..#.##...#",
"#..#.#.#.#",
"Tile 2731:",
"..#.#..###",
"#..#......",
"..#....###",
"...#..#..#",
"..........",
"..#.....##",
"#..###....",
"..........",
"#...#.....",
"#......#..",
"Tile 2803:",
".#.#.##.#.",
"##..##...#",
"...#..#..#",
"..#.#..#.#",
"#.#..##..#",
"##.#..#..#",
"...###.###",
"##.#..#...",
"..#.......",
".......#..",
"Tile 3191:",
".###..#.#.",
"###.#...#.",
"........##",
"....##...#",
".....#....",
".#.......#",
"..........",
"..#...#...",
"..###.....",
"##.....#.#",
"Tile 2753:",
"..#.#####.",
"....##..#.",
".........#",
"....##....",
"#..#...##.",
"#.....#..#",
"..........",
".##.......",
"#.....#..#",
".##..#.##.",
"Tile 2789:",
"##.#...#..",
"#.....##..",
".....###..",
"#.#.....##",
"#.#...##.#",
".........#",
"##.......#",
"##......##",
"#..#..###.",
"..###....#",
"Tile 2719:",
"##.###.#.#",
".........#",
"#....##...",
"...#..#...",
"##.......#",
"....##...#",
"..#...#..#",
"##.#.....#",
"##....#..#",
".#####...#",
"Tile 2143:",
".######..#",
"#......#..",
"#.......##",
"....#....#",
"#...#.....",
".........#",
"....#.#..#",
".......#.#",
"..........",
"#.##....##",
"Tile 2411:",
"..#.#..##.",
"##...##..#",
"...###...#",
"..#......#",
"#.###.....",
".........#",
"..#.##....",
"#..#....##",
"#..#..#..#",
"....##...#",
"Tile 1187:",
"##.##.....",
"##..#....#",
"..#..##...",
"##.#......",
".#..##....",
"#....#....",
"..........",
"##.......#",
"#..##..#.#",
"#..#.####.",
"Tile 3049:",
"..#..#.#.#",
".....#....",
"#........#",
"#...#..#..",
".........#",
"..#...#.#.",
"#.#....#..",
".....#....",
".......#..",
".#.#.#.##.",
"Tile 1997:",
".##.#.###.",
".....##...",
"....###..#",
"#....#...#",
"#.....#..#",
"#...#..#.#",
"....##...#",
".##..#....",
"#...#.....",
"#.#.###.#.",
"Tile 3181:",
"...#..#..#",
"..#..#..##",
"........#.",
"..........",
"#......#.#",
"##........",
"##.....#..",
"#.....##.#",
".#..#.....",
"##.....###",
"Tile 3371:",
".#....###.",
"#.....#...",
"##........",
"#.#.......",
"#........#",
".#.......#",
"#........#",
"...#.....#",
"..#.##.#..",
"...#..####",
"Tile 3491:",
".#.##...#.",
"#..#..##..",
"..#.####.#",
"...#......",
"#...#....#",
"#.........",
".....#..##",
"#...##....",
"##.....#..",
".####.....",
"Tile 2999:",
"#..#.##.##",
".#.#.....#",
"#.#.......",
"...#.....#",
".........#",
"###...#..#",
"..#......#",
"#...#.#...",
"..........",
".#....####",
"Tile 1423:",
".....###.#",
"##.#......",
"#......#..",
"##...#...#",
"#.#.#..#..",
"#.##......",
".....#...#",
".#.......#",
"......#..#",
"#.#..#####",
"Tile 3739:",
".#...###.#",
"..#...#...",
".#.#.#....",
"....#.....",
"..........",
".#.#...###",
"#.........",
"#...###...",
"#....#..##",
"#..#.....#"]
currTile = []
tiles = []
top = ''
bottom = ''
right = ''
left = ''
currLine = []
tileID = ''
matched = []
for x in range(1, len(inpt)-10, 11):
    tileID = inpt[x-1][inpt[x-1].index(' ')+1:inpt[x-1].index(':')]
    top = inpt[x]
    bottom = inpt[x+9]

    left = ''
    right = ''
    for y in range(10):
        currLine = list(inpt[x+y])
        print(currLine)
        print(currLine[0])
        left += currLine[0]
        right += currLine[9]

    tiles.append([top, top[::-1], bottom, bottom[::-1], left, left[::-1], right, right[::-1], tileID])
    print("Top",top)
    print("Bottom",bottom)
    print("Left",left)
    print("Right",right)
corners = []
for tile in tiles:
    print(tile)
compTile = []
for x in range(len(tiles)):
    currTile = tiles[x]
    sidesMatched = 0
    matched = []
    for y in range(len(tiles)):
        if y != x:
            compTile = tiles[y]
            for z in range(0, len(currTile)-1, 2):
                if currTile[z] in compTile:
                    if z == 0:
                        matched.append("Top")
                    if z == 2:
                        matched.append("Bottom")
                    if z == 4:
                        matched.append("Left")
                    if z == 6:
                        matched.append("Right")
                    sidesMatched += 1

    if sidesMatched == 2:
        corners.append(currTile[8])
        print(currTile[8])
        print(matched)

answer = 0
combos = combinations(corners, 4)
for combo in combos:
    answer = 1
    combin = list(combo)
    for x in range(len(combin)):
        answer *= int(combin[x])
    print(answer)


# 49979659793741 Wrong
# 68001945360061 Wrong
#77592375893567 too High
#29036849366009 Wrong
#33131965840723
#45079100979683
#26865179634743
#30654021817021
#41707629168941
#17809169122729
#346915602462983
#53532190032301
#72835491009821
#31100774687449
#28774743713623