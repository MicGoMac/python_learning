﻿$zip = new ZipArchive();
				$zip_filename = $dir.'/'.'aviva_admin_report_'.date('Y-m-d').'.zip';

				if ($zip->open($zip_filename, ZipArchive::CREATE)!==TRUE) {
					echo ("cannot open <$zip_filename>\n");
				}
				else {
					
					foreach($files_be_zipped as $value) {
						$zip->addFile($dir.'/'.$value,iconv('UTF-8','big5',$value));
					}
					
				}
				
				$zip->close();
				
				$this->response->file($zip_filename,
				array('download' => true, 'name' => 'aviva_admin_report_'.date('Y-m-d').'.zip'));
				return $this->response;
