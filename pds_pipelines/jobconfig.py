from pds_pipelines.config import pds_log, slurm_log, cmd_dir

log_format = '%(asctime)s - %(name)s - %(levelname)s, %(message)s'

jobconfig = {'di': {'logger': 'DIprocess_HPCjob',
                    'handle': pds_log + 'DI.log',
                    'info': 'Starting DI Process HPC Job Submission',
                    'name': 'PDS_DIprocess',
                    'stdout': slurm_log + 'DIprocess_%A_%a.out',
                    'stderr': slurm_log + 'DIprocess_%A_%a.err',
                    'memory': '256',
                    'wallclock': '240:00:00',
                    'partition': 'pds',
                    'cmd': cmd_dir + 'DIprocess.py',
                    'SBfile': slurm_log + 'DIhpc@date@.sbatch'},
             'upc': {'logger': 'UPCprocess_HPCjob',
                    'handle': pds_log + 'UPC.log',
                    'info': 'Starting UPC Process HPC Job Submission',
                    'name': 'PDS_UPCprocess',
                    'stdout': slurm_log + 'UPCprocess_%A_%a.out',
                    'stderr': slurm_log + 'UPCprocess_%A_%a.err',
                    'memory': '8192',
                    'wallclock': '20:00:00',
                    'partition': 'pds',
                    'cmd': cmd_dir + 'UPC_process.py',
                    'SBfile': slurm_log + 'UPChpc@date@.sbatch'},
             'ingest': {'logger': 'INGESTprocess_HPCjob',
                        'handle': pds_log + 'Ingest.log',
                        'info': 'Starting Ingest Process HPC Job Submission',
                        'name': 'PDS_Ingestprocess',
                        'stdout': slurm_log + 'Ingestprocess_%A_%a.out',
                        'stderr': slurm_log + 'Ingestprocess_%A_%a.err',
                        'memory': '8192',
                        'wallclock': '240:00:00',
                        'partition': 'pds',
                        'cmd': cmd_dir + 'IngestProcess.py',
                        'SBfile': slurm_log + 'Ingesthpc@date@.sbatch'},
             'ingest-override': {'logger': 'INGESTprocess_HPCjob',
                        'handle': pds_log + 'Ingest.log',
                        'info': 'Starting Ingest Process HPC Job Submission',
                        'name': 'PDS_Ingestprocess',
                        'stdout': slurm_log + 'Ingestprocess_%A_%a.out',
                        'stderr': slurm_log + 'Ingestprocess_%A_%a.err',
                        'memory': '8192',
                        'wallclock': '240:00:00',
                        'partition': 'pds',
                        'cmd': cmd_dir + 'IngestProcess.py --override',
                        'SBfile': slurm_log + 'Ingesthpc@date@.sbatch'},
             'thumbnail': {'logger': 'Thumbnailprocess_HPCjob',
                           'handle': pds_log + 'Process.log',
                            'info': 'Starting Thumbnail Process HPC Job Submission',
                            'name': 'PDS_Thumbnailprocess',
                            'stdout': slurm_log + 'Thumbnailprocess_%A_%a.out',
                            'stderr': slurm_log + 'Thumbnailprocess_%A_%a.err',
                            'memory': '8192',
                            'wallclock': '20:00:00',
                            'partition': 'pds',
                            'cmd': cmd_dir + 'thumbnail_process.py',
                            'SBfile': slurm_log + 'Thpc@date@.sbatch'},
             'browse': {'logger': 'Browseprocess_HPCjob',
                        'handle': pds_log + 'Process.log',
                        'info': 'Starting Browse Process HPC Job Submission',
                        'name': 'PDS_Browseprocess',
                        'stdout': slurm_log + 'Browseprocess_%A_%a.out',
                        'stderr': slurm_log + 'Browseprocess_%A_%a.err',
                        'memory': '8192',
                        'wallclock': '20:00:00',
                        'partition': 'pds',
                        'cmd': cmd_dir + 'browse_process.py',
                        'SBfile': slurm_log + 'Bhpc@date@.sbatch'},
             'projectionBrowse': {'logger': 'ProjectionBrowseProcess_HPCjob',
                                  'handle': pds_log + 'Process.log',
                                  'info': 'Starting Projection Browse Process HPC Job Submission',
                                  'name': 'PDS_ProjBrowseprocess',
                                  'stdout': slurm_log + 'ProjBrowseprocess_%A_%a.out',
                                  'stderr': slurm_log + 'ProjBrowseprocess_%A_%a.err',
                                  'memory': '8192',
                                  'wallclock': '20:00:00',
                                  'partition': 'pds',
                                  'cmd': cmd_dir + 'projectionbrowse_process.py',
                                  'SBfile': slurm_log + 'Phpc@date@.sbatch'}
             }