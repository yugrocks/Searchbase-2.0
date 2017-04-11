from distutils.core import setup
import py2exe



setup(
    windows=[
        {
            "script":"searchBASE.pyw",
            "icon_resources":[(1,"icons\search.ico")]
        }
    ],
    data_files=[("",["icons\search.ico"])],
)
