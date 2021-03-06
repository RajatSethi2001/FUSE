from .mutation_op import MutationOP
import sys
sys.path.append("..")
import utils


class mOP(MutationOP):
  __comment__ = "Mutation12: Double extension"
  __mutate_type__ = "file"  # (file|request) ; type of target
  __exclusion_op__ = {
'html':['M07', 'M12_ACE', 'M12_ARC', 'M12_ARJ', 'M12_BZ2', 'M12_DFXP', 'M12_EPUB', 'M12_GIF', 'M12_GPX', 'M12_GZIP', 'M12_JPG', 'M12_M4V', 'M12_MPA', 'M12_MPP', 'M12_NUMBERS', 'M12_ONETOC', 'M12_OXPS', 'M12_PAGES', 'M12_PDF', 'M12_PNG', 'M12_TAR_GZ', 'M12_TXT', 'M12_WP', 'M12_WRI', 'M12_XHT', 'M12_XLA', 'M12_XLW', 'M12_XPS', 'M12_ZIP', 'M12_ZIPX']}
                        # operations in this list can be used to extra mutation.
  __resource__ = {} # ({type:resource filename})
  __seed_dependency__ = __exclusion_op__.keys()#["html","js","php"] # seed file dependency for operation

  def operation(self, output, seed_file, resource_file=None):
      if output['filename'] != None and len(output['filename']) > 0:
        filename = output['filename']
      else:
        filename = utils.extract_filename(seed_file)

      output['filename'] = filename + '_M12HTML'

      output['fileext'] = 'html.'+output['fileext']
