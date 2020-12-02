# Melyssa Minto
# Advent of Code Day 1: https://adventofcode.com/2020/day/1


# input
test_input = c(1721, 979, 366, 299, 675, 1456)
real_input <- read_csv("GitHub/AdventofCode/2020/1_input.txt",  col_names = FALSE)$X1

# part 1
input=real_input
for( val1 in input )
  {
    for ( val2 in input)
      {
          if( val1 + val2 == 2020) {
            cat( val1, " + ", val2, " = ", val1 + val2, "\n")
            cat( val1, " x " , val2, " = " , val1*val2, "\n" )
            break
          }
      }
}

# part 2
input = real_input
for( val1 in input )
{
  for ( val2 in input)
  {
    for( val3 in input)
    {
      if( val1 + val2 + val3 == 2020) {
        cat( val1, " + ", val2," + ", val3, " = ", val1 + val2 + val3, "\n")
        cat( val1, " x " , val2, " x ", val3 ," = " , val1*val2*val3, "\n" )
        break
      }
    }
    
  }
}

