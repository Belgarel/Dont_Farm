########## ------------ Key bindings ------------ ##########

NUMBER_OF_SIRENS   = 99
BATTLE_TIME       = 130
STOP_SCRIPT        = 'ESCAPE'
ACTION_UP          = 'w'
ACTION_LEFT        = 'a'
ACTION_RIGHT       = 'd'
ACTION_DOWN        = 's'
ACTION_SELECT      = 'ENTER'
ACTION_MENU        = 'TAB'
ACTION_RETURN      = 'BACKSPACE'

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
menu_back = Command(ACTION_RETURN, 0.5)
wait_battle = Command(ACTION_LEFT, BATTLE_TIME, True)
go_down = Command(ACTION_DOWN, 0.5)
commands_heal_cecil = [wait_short, menu, go_down, wait_short, select, wait_short, select, wait_short, select, wait_short, select, wait_short, select, wait_short, menu_back, wait_short, menu_back, wait_short, menu_back, wait_short, menu_back, wait_short, menu_back, wait_short, menu_back, wait_short]
commands_use_siren = [wait_short, menu, wait_short, select, wait_short, select]
commands_do_battle = [wait_battle, select, wait_short, select, wait_short, select, wait_short, select, wait_short, select, wait_short, wait_short]
commands = commands_heal_cecil + commands_use_siren + commands_do_battle

########################## Do not concern yourself with this part. ###########################
##############################################################################################
if __name__ == "__main__":                                                                   #
  for i in range (0, NUMBER_OF_SIRENS):                                                      #
    print("Used " + str(i) + " sirens out of " + str(NUMBER_OF_SIRENS) + ".")                #
    for command in commands:                                                                 #
      command.execute()                                                                      #
  print("I've done it all. Event if there is no tail, please be grateful for my hard work.") #
##############################################################################################
