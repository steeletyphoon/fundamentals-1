Preconditions:
  * You encounter a monster/npc/pokewhatever

Actions:

  Prompt player for action:
    * Battle
    * Flee
    * Use
  
  Battle:
    * Show stats and HP for player and opponent
    * Prompt player to select move
    * Computer selects random-ish move
    * if player.speed > opponent.speed player goes first
      else opponent goes first
    * Call handlers for each  

  Flee:



Postconditions:
  * XP has been awarded to player
  * Battle recorded in player history
