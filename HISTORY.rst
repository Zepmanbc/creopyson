=======
History
=======

0.7.5 (2022-12-10)
------------------

* BugFix:
    * Add missing `location` argument on note_set (`issue#62`_)

.. _`issue#62`: https://github.com/Zepmanbc/creopyson/issues/62

0.7.4 (2022-05-16)
------------------

Update for `Creoson 2.8.1 release`_.

* Add parameters:
    * bom_get_paths : get_simpreps
* Documentation update:
    * creo_set_creo_version : Creo 8 support.

.. _`Creoson 2.8.1 release`: https://github.com/SimplifiedLogic/creoson/releases/tag/v2.8.1

0.7.3 (2021-08-29)
------------------

* Add *is not None* almost everywhere to prevent *False* and *None* confusion
* Migrates to Github Workflow
* Remove pipenv stuff

0.7.2 (2021-04-01)
------------------

* change python_requires to ">=3.7"

0.7.1 (2021-03-23)
------------------

* BugFix:
    * `file_get_active` returns `{}` instead of `None` with Creoson 2.8.0

0.7.0 (2021-03-22)
------------------

Update for `Creoson 2.8.0 release`_.

* New functions:
    * creo_set_creo_version (prevent Creo 7 problems)
    * feature_list_selected
* Add parameters:
    * feature_set_param: description
    * parameter_set: description
* Documentation update:
    * drawing_list: add *view_model*, *simp_rep* in Return
    * feature_list_param: add *description* in Return
    * feature_user_select_csys: add *file*, remove "feat_number* in Return object.
    * parameter_list: add *description* in Return
* BugFix:
    file_set_cur_material: now working with Creoson >2.8.0

.. _`Creoson 2.8.0 release`: https://github.com/SimplifiedLogic/creoson/releases/tag/v2.8.0

0.6.2 (2021-02-17)
------------------

Bugfix:

* drawing.get_cur_model: correction data_key (`issue#27`_)

.. _`issue#27`: https://github.com/Zepmanbc/creopyson/issues/27

0.6.1 (2021-01-30)
------------------

Bugfix:

* familytable.list_tree: correction data_key (`issue#21`_)

Documentation update:

* Usage: Add vanilla Creoson
* Usage: Add logging
* Issues template: add Creo version


.. _`issue#21`: https://github.com/Zepmanbc/creopyson/issues/21

0.6.0 (2020-07-16)
------------------

Update for `Creoson 2.7.0 release`_.

* New functions:
    * file_get_accuracy
* Add parameters:
    * interface_mapkey: delay
    * interface_export_pdf interface_export_pdf3d : sheet_range

.. _`Creoson 2.7.0 release`: https://github.com/SimplifiedLogic/creoson/releases/tag/v2.7.0

0.5.2 (2020-07-09)
------------------

Documentation update

* usage: path slashes correction

Docstring correction

* drawing_list_models : correction (`issue#18`_)

Bugfix

* file_get_transform : Does not return *transform* key (`issue#17`_)

.. _`issue#18`: https://github.com/Zepmanbc/creopyson/issues/18
.. _`issue#17`: https://github.com/Zepmanbc/creopyson/issues/17


0.5.1 (2020-05-19)
------------------

Docstring updates:

* interface_import_file: PV extension correction.
* interface_export_image: add infos about valid values in docstrings for dpi and depth.

Features updates:

* interface_mapkey: remove extra white space in script string.
* connection_start_creo: add use_desktop param.

New Feature:

* Add **logging DEBUG** on request & response.

0.5.0 (2020-03-08)
------------------

Update for `Creoson 2.6.0 release`_.

* New functions:
    * interface_import_file
* Add parameters:
    * bom_get_paths: add `has_simprep`
    * file_delete_material: `file` now allows wildcard
    * interface_export_file: add *NEUTRAL* to `file_type`
    * file_load_material: `file_` allows wildcard
* New returns:
    * file_massprops: add inertia matrices to output (`ctr_grav_inertia_tensor`, `coord_sys_inertia`, `coord_sys_inertia_tensor`)

.. _`Creoson 2.6.0 release`: https://github.com/SimplifiedLogic/creoson/releases/tag/v2.6.0

0.4.3 (2020-03-07)
------------------

Update missing features from previous Creoson updates.

* New Features:
    * drawing_set_sheet_format
    * file_get_cur_material
    * file_get_cur_material_wildcard
    * file_list_materials
    * file_list_materials_wildcard
    * file_load_material_file
    * file_set_cur_material

* New param:
    * note_list:
        * add *select* param
        * add *location* in response

0.4.2 (2020-03-03)
------------------

Bugfix:

* feature_list params correction (ADD: status, paths, no_comp. REMOVE: param, value, encoded)
* feature_list_params params correction(inc_unnamed)
* feature_param_exists params correction (name)
* add test on `status` correct values in feature's functions (feature_delete, feature_list feature_resume, feature_suppress)

modify pipenv config for bleach security alert.

0.4.1 (2020-01-30)
------------------

Bugfix:

* view_list_exploded(): name param was in request even if empty (`issue#4`_)
* start_creo(): path decomposition did not worked with Windows style (`issue#5`_)
* geometry_get_surfaces(): wrong data_key waited in result, need *surflist* (`issue#6`_)

.. _`issue#4`: https://github.com/Zepmanbc/creopyson/issues/4
.. _`issue#5`: https://github.com/Zepmanbc/creopyson/issues/5
.. _`issue#6`: https://github.com/Zepmanbc/creopyson/issues/6

0.4.0 (2019-10-12)
------------------

Update for `Creoson 2.5.0 release`_.

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

Bugfix:

* feature_resume: `with_children` paramt set default to `False` (`issue #3`_)

.. _`issue #3`: https://github.com/Zepmanbc/creopyson/issues/3

0.3.2 (2019-07-03)
------------------

Bugfix:

* creo_list_dirs: return empty list if there is no folder in the directory (`issue #1`_)

Add basic usage video on README

.. _`issue #1`: https://github.com/Zepmanbc/creopyson/issues/1


0.3.1 (2019-06-30)
------------------

Bugfixes:

* view_list: default query name="*"


0.3.0 (2019-06-29)
------------------

Bugfixes:

* file_set_mass_units: function param correction
* file_list: function param correction
* general: set active file when file is optionnal

Improvement:

* file_open: `activate` and `display` default to True
* dimension_set: file is optionnal


0.2.0 (2019-06-28)
------------------

Update for Creoson 2.4.0 release. New functions:

* parameter_set_designated
* feature_list_group_features
* feature_list_pattern_features

Add missing function:

* feature_list_params


0.1.0 (2019-06-22)
------------------

First release on PyPI.
