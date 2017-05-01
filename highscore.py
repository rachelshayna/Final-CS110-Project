#Lauren Birck
def highscore(score):
  infile = open("hiscore.txt", "r")
  old_hi = int(infile.readline())
  infile.close()
  outfile = open("hiscore.txt", "w")
  if old_hi > score:
    outfile.write(str(old_hi))
    return old_hi
  outfile.write(str(score))
  return score
  outfile.close()
