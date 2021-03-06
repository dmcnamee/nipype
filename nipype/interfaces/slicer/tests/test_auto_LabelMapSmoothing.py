# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.surface import LabelMapSmoothing
def test_LabelMapSmoothing_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    outputVolume=dict(position=-1,
    hash_files=False,
    argstr='%s',
    ),
    numberOfIterations=dict(argstr='--numberOfIterations %d',
    ),
    args=dict(argstr='%s',
    ),
    maxRMSError=dict(argstr='--maxRMSError %f',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    labelToSmooth=dict(argstr='--labelToSmooth %d',
    ),
    inputVolume=dict(position=-2,
    argstr='%s',
    ),
    gaussianSigma=dict(argstr='--gaussianSigma %f',
    ),
    )
    inputs = LabelMapSmoothing.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_LabelMapSmoothing_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = LabelMapSmoothing.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
