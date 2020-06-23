
########## ------------ Key bindings ------------ ##########

NUMBER_OF_SIRENS   = 90
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
wait_1_s = Command(ACTION_SELECT, 1, True)
select = Command(ACTION_SELECT, 0.4)
menu = Command(ACTION_MENU, 1)
menu_back = Command(ACTION_RETURN, 0.4)
wait_battle = Command(ACTION_LEFT, 180, True)
run_right = Command(ACTION_RIGHT, 3)
go_down = Command(ACTION_DOWN, 0.4)
go_up = Command(ACTION_UP, 0.4)
commands = [wait_1_s, menu, go_down, wait_1_s, select, wait_1_s, select, wait_1_s, select, wait_1_s, select, wait_1_s, select, wait_1_s, menu_back, wait_1_s, menu_back, wait_1_s, menu_back, wait_1_s, menu_back, wait_1_s, menu_back, wait_1_s, menu_back, wait_1_s, wait_1_s, menu, wait_1_s, select, wait_1_s, select, wait_battle, select, wait_1_s, select, wait_1_s, select, wait_1_s, select, wait_1_s, select, wait_1_s, wait_1_s]

########################## Do not concern yourself with this part. ###########################
##############################################################################################
if __name__ == "__main__":                                                                   #
  for i in range (0, NUMBER_OF_SIRENS):                                                      #
    print("Used " + str(i) + " sirens out of " + str(NUMBER_OF_SIRENS) + ".")                #
    for command in commands:                                                                 #
      command.execute()                                                                      #
  print("I've done it all. Event if there is no tail, please be grateful for my hard work.") #
##############################################################################################
