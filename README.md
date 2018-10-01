# Digital Image Processing 

1. Region Counting:

 	a. Program to binarize a gray-level image based on the assumption that the image has a bimodal histogram. Implement the method to estimate the optimal threshold required to binarize the image. The threshold is to be computed using the average of the expectation of the two distributions. Code should report both the binarized image and the optimal threshold value. Also assume that foreground objects are darker than background objects in the input gray-level image.
	- Starter code available in directory region_analysis/
	- region_analysis/binary_image.py:
		- compute_histogram: Code to compute the histogram in this function, If you return a list it will automatically save the graph in output folder
		- find_optimal_threshold: Code to compute the optimal threshold using the expected values of the bimodal histograms
		- binarize: Code to threshold the input image to create a binary image here. This function should return a binary image which will automatically be saved in output folder. For visualization one can use intensity value of 255 instead of 0 in the binay image and and 0 instead of 1 in binay images. That way the objects appear black over white background
  
 	b. Program to perform blob coloring. The input to the code should be a binary image (0's, and 255's) and the output should be a list of objects or regions in the image. 
	- region_analysis/cell_counting.py:
    	- blob_coloring: Code for blob coloring here, takes as input a binary image and returns a list of objects or regions.
  
 	c. Ignore cells smaller than 15 pixels in area and generate a report of the remaining cells (Cell Number, Area, Location)
	- region_analysis/cell_counting.py:
		- compute_statistics: Code for computing the statistics of each object/region, i.e area and location(centroid) here. Print out the statistics to stdout (using print function print one row for each region). 
		- Example: region number, area and centroid (Region: 1, Area: 1000, Centroid: (10,22))
		- mark_regions_image: Code to create a final cell labeled image. The final image should include an astrix representing the centroid of each cell and two numbers, one representing its Cell Number and another its area. Please see sample output below.
		
		
2. Image Compression:

	Code to compress a binary image using Run length Encoding. 
	- Starter code is available in directory Compression/
	- Compression/Run_Length_Encoding.py
		- encode_image: Code to compute run length code for the binary image. The input to your function will be a binary image(0's and 255's) and output ia a run length code.
		- decode_image: Code to get binary image from run length code returned by encode_image function. The input of the function is run length code, height and width of the binary image The output of the function is binary image reconstructed from run length code.
	
- Example to run the code:
  python dip_hw2_region_analysis.py -i <image-name>