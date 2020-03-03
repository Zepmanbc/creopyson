=======
History
=======

0.4.2 (2020-03-03)
------------------

* bugfix:
    * feature_list params correction (ADD: status, paths, no_comp. REMOVE: param, value, encoded)
    * feature_list_params params correction(inc_unnamed)
    * feature_param_exists params correction (name)
    * add test on `status` correct values in feature's functions (feature_delete, feature_list feature_resume, feature_suppress)

modify pipenv config for bleach security alert.

0.4.1 (2020-01-30)
------------------

* bugfix:
    * view_list_exploded(): name param was in request even if empty (`issue#4`_)
    * start_creo(): path decomposition did not worked with Windows style (`issue#5`_)
    * geometry_get_surfaces(): wrong data_key waited in result, need *surflist* (`issue#6`_)

.. _`issue#4`: https://github.com/Zepmanbc/creopyson/issues/4
.. _`issue#5`: https://github.com/Zepmanbc/creopyson/issues/5
.. _`issue#6`: https://github.com/Zepmanbc/creopyson/issues/6

0.4.0 (2019-10-12)
------------------

* Update for `Creoson 2.5.0 release`_.
    * New functions:
        * file_delete_material
        * drawing_get_sheet_format
        * dimension_set_text
    * Add parameters:
        * windchill_clear_workspace: filenames
        * dimension_list: select
        * dimension_list_detail: select
        * feature_resume: `name` can be an integer for *feat_ID*
        * feature_suppress: `name` can be an integer for *feat_ID*
    * New returns:
        * note_get: location
        * dimension_list: dwg_dim
        * dimension_list_detail: dwg_dim
    * Few notes updates

.. _`Creoson 2.5.0 release`: https://github.com/SimplifiedLogic/creoson/releases/tag/v2.5.0

0.3.3 (2019-07-13)
------------------

* bugfix:
    * feature_resume: `with_children` paramt set default to `False` (`issue #3`_)

.. _`issue #3`: https://github.com/Zepmanbc/creopyson/issues/3

0.3.2 (2019-07-03)
------------------

* bugfix:
    * creo_list_dirs: return empty list if there is no folder in the directory (`issue #1`_)

* Add basic usage video on README

.. _`issue #1`: https://github.com/Zepmanbc/creopyson/issues/1


0.3.1 (2019-06-30)
------------------

* bugfixes:
    * view_list: default query name="*"


0.3.0 (2019-06-29)
------------------

* bugfixes:
    * file_set_mass_units: function param correction
    * file_list: function param correction
    * general: set active file when file is optionnal
* improvement:
    * file_open: `activate` and `display` default to True
    * dimension_set: file is optionnal


0.2.0 (2019-06-28)
------------------

* Update for Creoson 2.4.0 release. New functions:
    * parameter_set_designated
    * feature_list_group_features
    * feature_list_pattern_features
* Add missing function: 
    * feature_list_params


0.1.0 (2019-06-22)
------------------

* First release on PyPI.
