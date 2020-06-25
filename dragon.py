########## ------------ Key bindings ------------ ##########

NUMBER_OF_SIRENS   = 99
BATTLE_TIME        = 28
ACTION_SELECT      = 'ENTER'
ACTION_MENU        = 'TAB'

########################## Do not concern yourself with this part. ###########################
##############################################################################################
import keyboard                                                                              #
import time                                                                                  #
class Command:                                                                               #
  def __init__(self, key, duration, is_silence = False):                                     #
    self.key = key                                                                           #
    self.duration = duration                                                                 #
    self.is_silence = is_silence                                                             #
  def execute(self):                                                                         #
    if (self.is_silence):                                                                    #
      print("Silence for " + str(self.duration) )                                            #
      time.sleep(self.duration)                                                              #
    else:                                                                                    #
      print("Key " + self.key + "   for " + str(self.duration) + " seconds.")                #
      keyboard.press(self.key)                                                               #
      time.sleep(self.duration)                                                              #
      keyboard.release(self.key)                                                             #
##############################################################################################

########## ----------     Actions     ----------- ##########
########## -- Scenario to hunt weakest summons -- ##########
wait_short = Command(ACTION_SELECT, 0.5, True)
select = Command(ACTION_SELECT, 0.5)
menu = Command(ACTION_MENU, 1)
wait_battle = Command(ACTION_SELECT, BATTLE_TIME, True)
commands_use_siren = [wait_short, menu, wait_short, select, wait_short, select]
commands_do_battle = [wait_battle, select, wait_short, select, wait_short]
commands = commands_use_siren + commands_do_battle

########################## Do not concern yourself with this part. ###########################
##############################################################################################
if __name__ == "__main__":                                                                   #
  for i in range (0, NUMBER_OF_SIRENS):                                                      #
    print("Used " + str(i) + " sirens out of " + str(NUMBER_OF_SIRENS) + ".")                #
    for command in commands:                                                                 #
      command.execute()                                                                      #
  print("I've done it all. Event if there is no tail, please be grateful for my hard work.") #
##############################################################################################
