#   
#   Based on Breakout by John Cheetham (http://www.johncheetham.com/projects/breakout)
#   Coder: Greg Michalik

#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#    
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import wasp
import fonts
import icons

import fonts.breakout as gfx

class BreakOutApp():
    NAME = 'BreakOut'
    ICON = icons.app

    def __init__(self):
        self.xspeed = -3
        self.yspeed = -3
        self.bat_speed = 10
        self.bat_x = 140
        self.ball_x = 120
        self.ball_y = 120
        
    def foreground(self):
        wasp.system.bar.clock = False # No Status Bar
        self._draw() # Initial Draw
        wasp.system.request_tick(17) # Set Tick callback for Roughly 30fps
        wasp.system.request_event(wasp.EventMask.TOUCH | wasp.EventMask.SWIPE_UPDOWN) # Event Setup

    def tick(self, ticks):
        # Detect Bat / Ball hit and deflection
        if self.ball_y >= 220 and self.ball_x + 10 >= self.bat_x - 30 and self.ball_x - 10 <= self.bat_x + 30:
            self.yspeed = -self.yspeed
            offset = self.ball_x - self.bat_x; # Determine offset of ball
            if self.xspeed > 0:
                if offset > 30:  
                    self.xspeed = 7
                elif offset > 23:                 
                    self.xspeed = 6
                elif offset > 17:
                    self.xspeed = 5
                if offset < -30:
                    self.xspeed = -7
                elif offset < -23:
                    self.xspeed = -6
                elif offset < -17:
                    self.xspeed = -5
            wasp.watch.drawable.string('({})'.format(offset), 0, 108, width=240)
        
        # Move Ball
        self.ball_x = self.ball_x + self.xspeed
        self.ball_y = self.ball_y + self.yspeed
        
        # Detect Wall hit and deflection
        if self.ball_x <= 21:
            self.ball_x = 21
            self.xspeed = -self.xspeed
        elif self.ball_x >= 240:
            self.ball_x = 240
            self.xspeed = -self.xspeed
            
        if self.ball_y <= 21:
            self.ball_y = 21
            self.yspeed = -self.yspeed
        elif self.ball_y >= 240:
            self.ball_y = 240
            self.xspeed = 0
            self.yspeed = 0
            
        self._draw()

    def swipe(self, event):
        return #Ignore

    def touch(self, event):
        # Move Bat
        if event[1] > 120 and self.bat_x < 220:
            self.bat_x += self.bat_speed
        elif event[1] <= 120 and self.bat_x > 60:
            self.bat_x -= self.bat_speed
        #wasp.watch.drawable.string('({}, {})'.format(event[1], event[2]), 0, 108, width=240) # Draw coordinates as string

    def _draw(self):
        wasp.watch.display.mute(True)
        draw = wasp.watch.drawable
        draw.fill()
        draw.blit(gfx.bat, self.bat_x - 60, 220) # Draw Bat
        draw.blit(gfx.ball, self.ball_x - 20, self.ball_y - 20)
        #draw.blit(gfx.brick, 0, 0)
        wasp.watch.display.mute(False)
