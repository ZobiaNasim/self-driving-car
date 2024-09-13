
# Analysis of Lane Detection Techniques on Structured Roads using OpenCV 




## Authors
Akash Punagin1
, Sahana Punagin2
1Department of Computer Science, JSS SMI UG and PG Studies


## Introduction

Computer vision is a field of Artificial Intelligence that enables autonomous vehicles to understand the
world around them. Autonomous Cars are required to perceive their surroundings. Based on their perceptions, they need to make
decisions. c. Lane detection is closely related with Advanced Driver Assistance System (ADAS) and Driver Support System.While it seems easy to detect white or yellow markings on the road, it can be challenging because of unusual lighting or whether
conditions, bizarre curves along the roads, occlusion by other vehicles etc.





## Approach
s are usually white or
yellow, a color filter is applied to accentuate the lane lines. Now, the preprocessing of frames concludes. The Sliding Window
approach is applied to detect lanes and record points in which they are detected. These points are fit to a second degree polynomial
from which Radius of curvature and Offset is calculated, for each frame.




## TOOLS AND LIBRARIES USED 
The document discusses the lane detection algorithm and focuses on image distortions and correction techniques using OpenCV, a widely-used open-source computer vision library. Key distortions include:

1. **Radial Distortion**: Occurs when light bends unevenly near the edges of a lens. There are two types:
   - **Positive Radial Distortion (Barrel)**: Common in wide-angle lenses, curving straight lines inward.
   - **Negative Radial Distortion (Pincushion)**: Common in telephoto lenses, curving straight lines outward.

2. **Tangential Distortion**: Happens when the lens and image plane are not parallel, causing lines to appear slanted.

Distortion can be corrected by calculating the camera matrix and distortion coefficients, commonly using chessboard patterns.


