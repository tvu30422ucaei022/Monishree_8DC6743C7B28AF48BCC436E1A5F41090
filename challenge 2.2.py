class player:
  def play(self):
    print("The player is playing ")
class batsman(player):
  def play(self):
    super().play()
    print("The batsman is batting")
class bowler(batsman):
  def play(self):
    super().play()
    print("The bowler is bowling")
s=bowler()
s.play()
