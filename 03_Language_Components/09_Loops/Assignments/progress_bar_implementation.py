#!/usr/bin/python

"""
Assignment: Progress bar implementation
    [          ]   3
    [*         ]  10
    [**        ]  20
    [***       ]  30
    [****      ]  40
    [*****     ]  50
    [******    ]  60
    [*******   ]  70
    [********  ]  80
    [********* ]  90
    [**********] 100
"""

total_values = range(0,101000)
size = len(total_values)

last_percent = -1 # initialize last percent to -1 

for loop_index, _ in enumerate(total_values):
    # percent_completed = int((loop_index / size) * 100)
    percent_completed = int((loop_index / (size - 1)) * 100)  # Use (size - 1) for correct calculation
    
    # check only for 0,10,20....100 percentages

    if percent_completed % 10 == 0 and percent_completed != last_percent:
        progress_bar = '*' * (percent_completed // 10) + ' ' * (10 - percent_completed // 10)
        print(f"[{progress_bar}] {percent_completed}")
        last_percent = percent_completed  # Update the last printed percentage
    
