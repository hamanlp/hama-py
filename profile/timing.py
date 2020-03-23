import pstats
p = pstats.Stats('profile/out.profile')
p.sort_stats('time').print_stats(10)
