set MEALBREAKS;										# set of mealbreak (3 options: 4, 4.5 and 5 hours after shift starts)
set SHIFTTIME;										# set of permissible shift starting time
set HALFHOURS;										# set of 48 half-hours

param big_M;										  # big M
param staff_req {HALFHOURS};			# staff requirement at each half hour	

param total_shifts;								# maximum number of shifts allowed 
													        # shifts start at the same time but have different meal break time 
													        # will be counted as 1 shift allowed
													
param shift_meal {HALFHOURS, SHIFTTIME, MEALBREAKS};
                                  # matrix indicating staff availbility for each half hour 
													        # of each combination from starting time and meal break	


var staff {SHIFTTIME, MEALBREAKS} integer >=0; 	# number of staff at shift starts at SHIFTTIME and have meal break at MEALBREAKS
var shift {SHIFTTIME} binary;					# binary, 1 if shift start at HALFHOURS have at least 1 staff 

# objective: minimize the total number of staffs required
minimize total_staffs:
	sum {s in SHIFTTIME} sum {m in MEALBREAKS} staff[s,m];	
	
# constraint: number of staffs at each half-hour satisfied the minimum requirement
subject to staff_req_cstr {h in HALFHOURS}:
	sum {s in SHIFTTIME} sum {m in MEALBREAKS} staff[s,m] * shift_meal[h,s,m] >= staff_req[h];
	
# constraint: total number of shift-start-timing allowed
subject to total_shifts_cstr:
	sum {s in SHIFTTIME} shift[s] <= total_shifts;
	
	
# constraint: 
	# if staff of shift starting at s is non zero, then shift[s] = 1
	# else shift[s] = 0	
subject to lower_bound_cstr {s in SHIFTTIME}:
	sum {m in MEALBREAKS} staff[s,m] >= shift[s];
subject to upper_bound_cstr {s in SHIFTTIME}:
	sum {m in MEALBREAKS} staff[s,m] <= shift[s] * big_M;
	



	


			

