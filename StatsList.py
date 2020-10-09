digimon_stats=[["Attack",7], ["Defense",10],["S",4]]

#Use the Analyzer to get Digimon details.

print(digimon_stats[1])

#Use the Analyzer to get the numerical value for the Digimon's Speed (S)
#[2][1] is the 2nd list & 1st value inside digimon_stats, where counting is 0-based.

print(digimon_stats[2][1])

#Display all of the statistics at once.
print("Full Battle Statistics:")
for digimon in digimon_stats:
    print(digimon)

#Reveal the numeric statistic for each attribute.
print("Value per attribute:")
for digimon in digimon_stats:
        print(digimon[1])