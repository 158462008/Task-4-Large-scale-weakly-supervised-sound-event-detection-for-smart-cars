#Code Contributor: Rohan Badlani, Email: rohan.badlani@gmail.com
import os
import sys
from Models import *

def evaluateMetrics(groundtruth_filepath, predicted_filepath, output_filepath):
	#Load GroundTruth to memory, indexed by 
	groundTruthDS = FileFormat(groundtruth_filepath)
	preditedDS = FileFormat(predicted_filepath)
	#output = groundTruthDS.computeMetrics(preditedDS,output_filepath)
	
	print len(groundTruthDS.labelsDict.keys())
	print len(preditedDS.labelsDict.keys())
	#simple audioFileCheck
	#if len(groundTruthDS.labelsDict.keys()) != len(preditedDS.labelsDict.keys()):
	#	print "The prediction file submitted does not have prediction for all the audio files"
	#	sys.exit(1)

	#complex check for audioFile
	#if not groundTruthDS.validatePredictedDS(preditedDS):
	#	print "The prediction file submitted does not have prediction for all the audio files"
	#	sys.exit(1)

	#the submission is valid. Compute Metrics and Push to File
	output = groundTruthDS.computeMetricsString(preditedDS)
	with open(output_filepath, "w") as filepath:
		filepath.write(output)
	filepath.close()

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "Running Instruction: python TaskAEvaluate.py <groundtruth_filepath> <predicted_filepath> <output_filepath>"
	else:
		evaluateMetrics(sys.argv[1], sys.argv[2], sys.argv[3])
