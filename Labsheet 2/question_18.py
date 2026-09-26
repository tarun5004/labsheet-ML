"""Question 18: compare before and after outlier treatment."""
from _common import messy, outlier_mask
frame=messy(); treated=frame[outlier_mask(frame)]; print({'before':len(frame), 'after':len(treated)})
