﻿def filename_to_vid( f ):
	pi = pathinfo(f)
	
	ext= pi['extension']
	fn= pi['filename']
	return substr( fn, -11)