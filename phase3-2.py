import subprocess

inputs = ["submission_4655966_input20.in",
"submission_4704348_input20.in",
"submission_4710132_inputs_input20.in",
"submission_4712152_inputs_input20.in",
"submission_4712495_input20.in",
"submission_4712879_input20.in",
"submission_4713185_input20.in",
"submission_4713940_inputs_input20.in",
"submission_4714821_input20.in",
"submission_4714871_inputs_input20.in",
"submission_4716033_inputs_input20.in",
"submission_4716649_input20.in",
"submission_4716827_inputs_input20.in",
"submission_4718113_inputs_input20.in",
"submission_4670106_inputs_input35.in",
"submission_4698720_inputs_input35.in",
"submission_4703229_inputs_input35.in",
"submission_4711880_input35.in",
"submission_4713262_inputs_input35.in",
"submission_4714889_inputs_input35.in",
"submission_4716635_inputs_input35.in",
"submission_4717517_input35.in",
"submission_4718430_input35.in",
"submission_4718670_input35.in",
"submission_4718727_input35.in",
"submission_4702791_input35.in",
"submission_4707501_input35.in",
"submission_4709745_input35.in",
"submission_4710132_inputs_input35.in",
"submission_4712590_inputs_input35.in",
"submission_4713185_input35.in",
"submission_4713735_inputs_input35.in",
"submission_4714689_inputs_input35.in",
"submission_4717524_inputs_input35.in",
"submission_4718744_input35.in",
"submission_4612341_inputs_input50.in",
"submission_4692735_inputs_input50.in",
"submission_4712058_inputs_input50.in",
"submission_4712590_inputs_input50.in",
"submission_4715459_inputs_input50.in",
"submission_4716563_input50.in",
"submission_4716708_input50.in",
"submission_4717561_input50.in",
"submission_4717615_input50.in",
"submission_4717962_input50.in",
"submission_4718176_input50.in",
"submission_4718446_inputs_input50.in",
"submission_4718832_input50.in"]


for i in inputs[::-1]:
	out = "outputs3/" + i[:-3] + ".out"
	subprocess.call(["touch", out])
	subprocess.call(["python2", "solver.py", "./allinputs/" + i, out])
	subprocess.call(["python2", "output_validator.py", "./allinputs/" + i, out])
	print out