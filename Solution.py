import math 
class Solution:
    
    def __init__(self, points):
        self.points = points

    def findClosestPair(self):
        #sort points by (x,y) lexicograpphic order 
        #return the closest pair sorted points 
        
        def distance(p1,p2):
            x = (p1[0]-p2[0])**2
            y = (p1[1]-p2[1])**2
            return math.sqrt(x+y) 
        def closest(pts):
            n = len(pts)
            if n ==1:
                return float('inf')
            
            mid = n//2 
            mid_point = pts[mid]
            mx = mid_point[0]
            L_half = pts[:mid]
            R_half = pts[mid:]
            
            d_left = closest(L_half)
            d_right = closest(R_half)
            
            d = min(d_left, d_right)
            
            strip = []
            for p in pts:
                dfm = abs(p[0] - mx)
                if dfm <d:
                    strip.append(p)
                    
            strip = sorted(strip, key=lambda p: p[1])
            
            for i in range(len(strip)):
                j = i+1
                while j<len(strip):
                    point_i = strip[i]
                    point_j = strip[j]
                    
                    y_gap = point_j[1] - point_i[1]
                    
                    if y_gap >= d:
                        break 
                    
                    
                    curr_dist = distance(point_i, point_j)
                    if curr_dist <d:
                        d = curr_dist
                        
                    j += 1 
            return d 
        
        return closest(sorted(self.points, key = lambda p:(p[0],p[1]))) 
'''
closest pair (points)
'''    
    
