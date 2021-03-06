# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.spm.preprocess import Realign
def test_Realign_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    paths=dict(),
    write_mask=dict(field='roptions.mask',
    ),
    register_to_mean=dict(field='eoptions.rtm',
    mandatory=True,
    usedefault=True,
    ),
    weight_img=dict(field='eoptions.weight',
    ),
    write_wrap=dict(field='roptions.wrap',
    ),
    write_interp=dict(field='roptions.interp',
    ),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    interp=dict(field='eoptions.interp',
    ),
    out_prefix=dict(field='roptions.prefix',
    usedefault=True,
    ),
    use_mcr=dict(),
    write_which=dict(minlen=2,
    maxlen=2,
    field='roptions.which',
    usedefault=True,
    ),
    mfile=dict(usedefault=True,
    ),
    matlab_cmd=dict(),
    jobtype=dict(usedefault=True,
    ),
    separation=dict(field='eoptions.sep',
    ),
    wrap=dict(field='eoptions.wrap',
    ),
    quality=dict(field='eoptions.quality',
    ),
    fwhm=dict(field='eoptions.fwhm',
    ),
    in_files=dict(copyfile=True,
    mandatory=True,
    field='data',
    ),
    )
    inputs = Realign.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Realign_outputs():
    output_map = dict(realignment_parameters=dict(),
    modified_in_files=dict(),
    realigned_files=dict(),
    mean_image=dict(),
    )
    outputs = Realign.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
