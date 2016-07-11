class dmh_options():
    """class to save the AddOn-options

    """ 

def import_data(fileName):
    """import data from a '.dmh'-File

    :param fileName: Path and name of file 
    :type fileName: str. 

    :returns: none -- importing data and saving them in bpy.types.Scene.dmh 

    """ 


def export_data(fileName):
    """export data to a '.dmh'-File

    :param fileName: Path and name of file 
    :type fileName: str. 
    :returns: none -- exporting all data stored in bpy.types.Scene.dmh to file in json format

    """ 


def make_obj():
    """creating an object by using all data stored in options

    :returns: none -- exporting all data stored in bpy.types.Scene.dmh to file in json format

    """ 


def main_function(context):
    """main function of the AddOn

    :returns: 'FINISHED'

    """ 

def copyBmesh(src, sca, rot, loc):
    """copying vertices' coordinates and faces from a source Bmesh to AddOn options

    :param src: source Bmesh that will be copied 
    :type src: bmesh
    :param sca: scaling matrix that will be used for transformation of the source Bmesh  
    :type sca: 4x4-matrix
    :param rot: rotation matrix that will be used for transformation of the source Bmesh  
    :type rot: 4x4-matrix
    :param loc: translationn vector that will be used for transformation of the source Bmesh  
    :type loc: 4D-vector
    :param src: source Bmesh that will be copied 
    :type src: bmesh
    :returns: none -- exporting all data stored in bpy.types.Scene.dmh to file in json format

    """ 

# Function to create the hull for knots of a input object/tree
# createKnots( 
#               input object/tree,
#               target bMesh
#               )
def createKnots(data, knot_type, vertex_pvr, hide_knots, radius, knot_resolution):
    """modelling knots

    :param src: source Bmesh that will be copied 
    :type src: bmesh
    :param sca: scaling matrix that will be used for transformation of the source Bmesh  
    :type sca: 4x4-matrix
    :param rot: rotation matrix that will be used for transformation of the source Bmesh  
    :type rot: 4x4-matrix
    :param loc: translationn vector that will be used for transformation of the source Bmesh  
    :type loc: 4D-vector
    :param src: source Bmesh that will be copied 
    :type src: bmesh
    :returns: none -- exporting all data stored in bpy.types.Scene.dmh to file in json format

    """ 
   
def createEdges(data, edge_pvr, knot_radius, edge_radius, edge_resolution):
    """modelling knots

    :param data: list of verticed, edges, world matrix and bevel weights 
    :type data: list
    :param edge_pvr: option to use edge Pro-Vertex-Radius  
    :type edge_pvr: boolean
    :param knot_radius: radius for the knots  
    :type knot_radius: float
    :param edge_radius: radius for the edges  
    :type edge_radius: float
    :param edge_resolution: resolution for the edges
    :type edge_resolution: integer
    :returns: none -- calling copyBmesh()

    """ 

class dmh_add():
    """Operator class (bpy.types.Operator)

    :returns: 'FINISHED'

    """ 
    '''Add a Wireframe Cover'''
  
def menu_func():
    """Menu function

    :returns: none

    """ 

class DMHImport():
    """Operator class (bpy.types.Operator, ImportHelper)

    :returns: 'FINISHED'

    """ 
 
class DMHExport():
    """Operator class (bpy.types.Operator, ExportHelper)

    :returns: 'FINISHED'

    """     


def menu_func_import():
    """Menu function

    :returns: none

    """ 

def menu_func_export():
    """Menu function

    :returns: none

    """ 

if __name__ == "__main__":
    register()
