#!/usr/bin/python
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.sew-brilliant.org/
#
# Copyright (C) 2010, 2011 Susan Spencer and Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# measurement constants
in_to_pt = ( 72.72 / 1    )  #convert inches to printer's points
cm_to_pt = ( 72.72 / 2.54  ) #convert centimeters to printer's points
cm_to_in = ( 1 / 2.54 )   #convert centimeters to inches
in_to_cm = ( 2.54 / 1 )   #convert inches to centimeters

in_to_px = ( 90 / 1 )   	  # convert inches to pixels - Inkscape value
cm_to_px = ( 72.72 /  2.54 )  #convert cm to px - Inkscape value

# sewing constants
QUARTER_SEAM_ALLOWANCE = ( in_to_px * 1 / 4 ) # 1/4" seam allowance
SEAM_ALLOWANCE         = ( in_to_px * 5 / 8 ) # 5/8" seam allowance
HEM_ALLOWANCE          = ( in_to_px * 2     ) # 2" seam allowance
PATTERN_OFFSET         = ( in_to_px * 3     ) # 3" between patterns
