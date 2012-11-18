"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os
from nipype.interfaces.slicer.base import SlicerCommandLine


class IntensityDifferenceMetricInputSpec(CommandLineInputSpec):
    sensitivityThreshold = traits.Float(desc="This parameter should be between 0 and 1, and defines how sensitive the metric should be to the intensity changes.", argstr="--sensitivityThreshold %f")
    changingBandSize = traits.Int(desc="How far (in mm) from the boundary of the segmentation should the intensity changes be considered.", argstr="--changingBandSize %d")
    outputVolume = traits.Either(traits.Bool, File(), position=-1, hash_files=False, desc="Output volume to keep the results of change quantification.", argstr="%s")
    reportFileName = traits.Either(traits.Bool, File(), hash_files=False, desc="Report file name", argstr="--reportFileName %s")


class IntensityDifferenceMetricOutputSpec(TraitedSpec):
    outputVolume = File(position=-1, desc="Output volume to keep the results of change quantification.", exists=True)
    reportFileName = File(desc="Report file name", exists=True)


class IntensityDifferenceMetric(SlicerCommandLine):
    """title: 
  Intensity Difference Change Detection (FAST)
  

category: 
  Quantification.ChangeQuantification
  

description: 
  Quantifies the changes between two spatially aligned images based on the pixel-wise difference of image intensities.
  

version: 0.1

contributor: Andrey Fedorov

acknowledgements: 


"""

    input_spec = IntensityDifferenceMetricInputSpec
    output_spec = IntensityDifferenceMetricOutputSpec
    _cmd = "/home/raid3/gorgolewski/software/slicer/Slicer --launch IntensityDifferenceMetric "
    _outputs_filenames = {'outputVolume':'outputVolume.nii','reportFileName':'reportFileName'}