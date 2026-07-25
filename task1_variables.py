# Video Game Sales Dataset
# Source: Adapted from VGChartz (public domain estimates)
# Each row: [rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, global_sales]

video_game_sales = [
    [1, 'Wii Sports', 'Wii', 2006, 'Sports', 'Nintendo', 41.49, 29.02, 3.77, 82.74],
    [2, 'Super Mario Bros.', 'NES', 1985, 'Platform', 'Nintendo', 29.08, 3.58, 6.81, 40.24],
    [3, 'Mario Kart Wii', 'Wii', 2008, 'Racing', 'Nintendo', 15.85, 12.88, 3.79, 35.82],
    [4, 'Wii Sports Resort', 'Wii', 2009, 'Sports', 'Nintendo', 15.75, 11.01, 3.28, 33.0],
    [5, 'Pokemon Red/Blue', 'GB', 1996, 'Role-Playing', 'Nintendo', 11.27, 8.89, 10.22, 31.37],
    [6, 'Tetris', 'GB', 1989, 'Puzzle', 'Nintendo', 23.2, 2.26, 4.22, 30.26],
    [7, 'New Super Mario Bros.', 'DS', 2006, 'Platform', 'Nintendo', 11.38, 9.23, 6.5, 30.01],
    [8, 'Wii Play', 'Wii', 2006, 'Misc', 'Nintendo', 14.03, 9.2, 2.93, 29.02],
    [9, 'New Super Mario Bros. Wii', 'Wii', 2009, 'Platform', 'Nintendo', 14.59, 7.06, 4.7, 28.62],
    [10, 'Duck Hunt', 'NES', 1984, 'Shooter', 'Nintendo', 26.93, 0.63, 0.28, 28.31],
    [11, 'Nintendogs', 'DS', 2005, 'Simulation', 'Nintendo', 9.07, 11.0, 1.93, 24.76],
    [12, 'Mario Kart DS', 'DS', 2005, 'Racing', 'Nintendo', 9.81, 7.57, 4.13, 23.42],
    [13, 'Pokemon Gold/Silver', 'GB', 1999, 'Role-Playing', 'Nintendo', 9.0, 6.18, 7.2, 23.1],
    [14, 'Wii Fit', 'Wii', 2007, 'Sports', 'Nintendo', 8.94, 8.03, 3.6, 22.72],
    [15, 'Kinect Adventures!', 'X360', 2010, 'Misc', 'Microsoft', 14.97, 4.94, 0.24, 21.82],
    [16, 'Grand Theft Auto V', 'PS3', 2013, 'Action', 'Take-Two', 7.01, 9.27, 0.97, 21.4],
    [17, 'Grand Theft Auto: San Andreas', 'PS2', 2004, 'Action', 'Take-Two', 9.43, 0.4, 0.41, 20.81],
    [18, 'Super Mario World', 'SNES', 1990, 'Platform', 'Nintendo', 12.78, 3.75, 3.54, 20.61],
    [19, 'Brain Age', 'DS', 2005, 'Puzzle', 'Nintendo', 4.75, 9.26, 4.16, 20.22],
    [20, 'Pokemon Diamond/Pearl', 'DS', 2006, 'Role-Playing', 'Nintendo', 6.42, 4.52, 6.04, 18.36],
]

# Column index reference (use these throughout the project)
RANK = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
NAME =('Wii Sports', 'Super Mario', 'Mario Kart Wii', 'Wii Sports Resort', 'Pokemon Red/Blue', 'Tetris', 'New Super Mario Bros.'
'Wii Play', 'New Super Mario Bros. Wii', 'Duck Hunt', 'Nintendogs', 'Mario Kart DS', 'Pokemon Gold/Silver', 'Wii Fit', 'Kinect Adventures!', 'Grand Theft Auto V', 'Grand Theft Auto: San Andreas', 'Super Mario World', 'Brain Age', 'Pokemon Diamond/Pearl')
PLATFORM = ('Wii', 'Wii', 'Wii', 'GB', 'GB', 'DS', 'Wii', 'Wii', 'NES', 'DS', 'DS', 'GB', 'Wii', 'X360', 'PS3', 'PS2', 'SNES', 'DS')
YEAR = (2006, 1985, 2008, 2009, 1996, 1989, 2006, 2006, 2009, 1984, 2005, 2005, 1999, 2007, 2010, 2013, 2004, 1990, 2005, 2006)
GENRE = ('Sports', 'Platform', 'Racing', 'Sports', 'Role-Playing', 'Puzzle', 'Platform', 'Misc', 'Platform', 'Shooter', 'Simulation', 'Racing', 'Role-Playing', 'Sports', 'Misc', 'Action', 'Action', 'Platform', 'Puzzle','Role-Playing')
PUBLISHER = ('Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Nintendo', 'Microsoft', 'Take-Two', 'Take-Two', 'Nintendo', 'Nintendo', 'Nintendo')
NA_SALES = [41.49, 29.08, 15.85, 15.75, 11.27, 23.2, 11.38, 14.03, 14.59, 26.93, 9.07, 9.81, 9.0, 8.94, 14.97, 7.01, 9.43, 12.78, 4.75, 6.42]
EU_SALES = [29.02, 3.58, 12.88, 11.01, 8.89, 2.26, 9.23, 9.2, 7.06, 0.63, 11.0, 7.57, 6.18, 8.03, 4.94, 9.27, 0.4, 3.75, 9.26, 4.52]
JP_SALES = [3.77, 6.81, 3.79, 3.28, 10.22, 4.22, 6.5, 2.93, 4.7, 0.28, 1.93, 4.13, 7.2, 3.6, 0.24, 0.97, 0.41, 3.54, 4.16, 6.04,]
GLOBAL_SALES = [82.74, 40.24, 35.82, 33.0, 31.37, 30.26, 30.01, 29.02, 28.62, 28.31, 24.76, 23.42, 23.1, 22.72, 21.82, 21.4, 20.81, 20.61, 20.22, 18.36]

total_games = len(video_game_sales)

avg_global_sales = []
for sale in GLOBAL_SALES:
    avg_global_sales = sum(GLOBAL_SALES)/len(GLOBAL_SALES)

total_gs = [0]
top_game_share = [0]
for sale in GLOBAL_SALES:
    total_gs = sum(GLOBAL_SALES)
    top_game_share = float(GLOBAL_SALES[0]/total_gs)*100
    
print(f'Total number of games: {total_games}')
print(f'The average global sale: ${avg_global_sales}')
print(f'Top game perecentage of global sales: {top_game_share}%')
