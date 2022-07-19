import shutil
import numpy as np

import iric

from . import util

def case_GridRead():
    shutil.copy("data/case_init_hdf5.cgn", "data/case_grid.cgn")

    fid = iric.cg_iRIC_Open("data/case_grid.cgn", iric.IRIC_MODE_MODIFY)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    isize, jsize = iric.cg_iRIC_Read_Grid2d_Str_Size(fid)
    util.verify_log("cg_iRIC_Read_Grid2d_Str_Size() isize == 11", isize == 11)
    util.verify_log("cg_iRIC_Read_Grid2d_Str_Size() jsize == 11", jsize == 11)

    x, y = iric.cg_iRIC_Read_Grid2d_Coords(fid)

    doubleArr = iric.cg_iRIC_Read_Grid_Real_Node(fid, "node_real")
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[0] == 2", doubleArr[0] == 2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[1] == 2", doubleArr[1] == 2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[2] == 2", doubleArr[2] == 2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[3] == 2", doubleArr[3] == 2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[4] == 2", doubleArr[4] == 2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[5] == 2", doubleArr[5] == 2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[6] == 2", doubleArr[6] == 2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[7] == 0", doubleArr[7] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[8] == 0", doubleArr[8] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Real_Node() value[9] == 0", doubleArr[9] == 0)

    intArr = iric.cg_iRIC_Read_Grid_Integer_Node(fid, "node_int")
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[0] == 0", intArr[0] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[1] == 0", intArr[1] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[2] == 0", intArr[2] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[3] == 0", intArr[3] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[4] == 0", intArr[4] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[5] == 1", intArr[5] == 1)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[6] == 1", intArr[6] == 1)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[7] == 1", intArr[7] == 1)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[8] == 1", intArr[8] == 1)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Node() value[9] == 1", intArr[9] == 1)

    doubleArr = iric.cg_iRIC_Read_Grid_Real_Cell(fid, "cell_real")
    util.verify_log("cg_iRIC_Read_Grid_Real_Cell() value[0] == 4.2", doubleArr[0] == 4.2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Cell() value[1] == 4.2", doubleArr[1] == 4.2)
    util.verify_log("cg_iRIC_Read_Grid_Real_Cell() value[2] == 0", doubleArr[2] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Real_Cell() value[3] == 0", doubleArr[3] == 0)

    intArr = iric.cg_iRIC_Read_Grid_Integer_Cell(fid, "cell_int")
    util.verify_log("cg_iRIC_Read_Grid_Integer_Cell() value[0] == 0", intArr[0] == 0)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Cell() value[15] == 1", intArr[15] == 1)
    util.verify_log("cg_iRIC_Read_Grid_Integer_Cell() value[16] == 0", intArr[16] == 0)


    try:
        grid_handle = iric.cg_iRIC_Read_Grid2d_Open(fid)
        util.verify_log("cg_iRIC_Read_Grid2d_Open ier == 0", True)
    except:
        pass

    area = iric.cg_iRIC_Read_Grid2d_CellArea(grid_handle, 1)
    util.verify_log("cg_iRIC_Read_Grid2d_CellArea() area == 0.017", abs(area - 0.0173) < 0.0001)

    cellNodeCount = iric.cg_iRIC_Read_Grid2d_CellNodeCount(grid_handle, 1)
    util.verify_log("cg_iRIC_Read_Grid2d_CellNodeCount() cellNodeCount == 4", cellNodeCount == 4)

    try:
        nodeIds, weights = iric.cg_iRIC_Read_Grid2d_Interpolate(grid_handle, 0.0, 0.0)
        util.verify_log("cg_iRIC_Read_Grid2d_Interpolate ier == 0", True)
    except:
        pass

    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() nodeIds[0] == 93", nodeIds[0] == 93)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() nodeIds[1] == 94", nodeIds[1] == 94)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() nodeIds[2] == 105", nodeIds[2] == 105)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() nodeIds[3] == 104", nodeIds[3] == 104)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() weights[0] == 0.3863", abs(weights[0] - 0.3863) < 0.0001)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() weights[1] == 0.4012", abs(weights[1] - 0.4012) < 0.0001)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() weights[2] == 0.2123", abs(weights[2] - 0.2123) < 0.0001)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() weights[3] == 0", abs(weights[3] - 0) < 0.0001)

    iric.cg_iRIC_Read_Grid2d_Close(grid_handle)

    iric.cg_iRIC_Close(fid)

    util.remove("data/case_grid.cgn")

def case_GridReadUnstructured():
    shutil.copy("data/case_unst_hdf5.cgn", "data/case_grid_unstructured.cgn")

    fid = iric.cg_iRIC_Open("data/case_grid_unstructured.cgn", iric.IRIC_MODE_MODIFY)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    elem_size = iric.cg_iRIC_Read_Grid_TriangleElementsSize(fid)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElementsSize() elem_size == 3", elem_size == 3)

    node_count = iric.cg_iRIC_Read_Grid_NodeCount(fid)
    util.verify_log("cg_iRIC_Read_Grid_NodeCount() node_count == 5", node_count == 5)

    x, y = iric.cg_iRIC_Read_Grid2d_Coords(fid)
    elems = iric.cg_iRIC_Read_Grid_TriangleElements(fid)

    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[0] == 1", elems[0] == 1)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[1] == 2", elems[1] == 2)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[2] == 5", elems[2] == 5)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[3] == 4", elems[3] == 4)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[4] == 5", elems[4] == 5)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[5] == 2", elems[5] == 2)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[6] == 4", elems[6] == 4)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[7] == 2", elems[7] == 2)
    util.verify_log("cg_iRIC_Read_Grid_TriangleElements() elems[8] == 3", elems[8] == 3)

    try:
        grid_handle = iric.cg_iRIC_Read_Grid2d_Open(fid)
        util.verify_log("cg_iRIC_Read_Grid2d_Open ier == 0", True)
    except:
        pass

    area = iric.cg_iRIC_Read_Grid2d_CellArea(grid_handle, 1)
    util.verify_log("cg_iRIC_Read_Grid2d_CellArea() area == 0.2067", abs(area - 0.2067) < 0.0001)

    cellNodeCount = iric.cg_iRIC_Read_Grid2d_CellNodeCount(grid_handle, 1)
    util.verify_log("cg_iRIC_Read_Grid2d_CellNodeCount() cellNodeCount == 3", cellNodeCount == 3)

    try:
        nodeIds, weights = iric.cg_iRIC_Read_Grid2d_Interpolate(grid_handle, 0.0, 0.0)
        util.verify_log("cg_iRIC_Read_Grid2d_Interpolate ier == 0", True)
    except:
        pass

    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() nodeIds[0] == 4", nodeIds[0] == 4)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() nodeIds[1] == 5", nodeIds[1] == 5)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() nodeIds[2] == 2", nodeIds[2] == 2)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() weights[0] == 0.5415", abs(weights[0] - 0.5415) < 0.0001)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() weights[1] == 0.0921", abs(weights[1] - 0.0921) < 0.0001)
    util.verify_log("cg_iRIC_Read_Grid2d_Interpolate() weights[2] == 0.3663", abs(weights[2] - 0.3663) < 0.0001)

    iric.cg_iRIC_Read_Grid2d_Close(grid_handle)

    iric.cg_iRIC_Close(fid)

    util.remove("data/case_grid_unstructured.cgn")

def case_GridReadFunc():
    shutil.copy("data/case_gridfunc.cgn", "data/case_gridreadfunc.cgn")

    fid = iric.cg_iRIC_Open("data/case_gridreadfunc.cgn", iric.IRIC_MODE_MODIFY)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    isize, jsize = iric.cg_iRIC_Read_Grid2d_Str_Size(fid)
    util.verify_log("cg_iRIC_Read_Grid2d_Str_Size() isize == 15", isize == 15)
    util.verify_log("cg_iRIC_Read_Grid2d_Str_Size() jsize == 15", jsize == 15)

    x, y = iric.cg_iRIC_Read_Grid2d_Coords(fid)

    timeArr = iric.cg_iRIC_Read_Grid_FunctionalDimension_Real(fid, "Xrain", "Time")
    timeArr = iric.cg_iRIC_Read_Grid_FunctionalTime(fid, "Xrain")

    for i in range(timeArr.size):
        rain = iric.cg_iRIC_Read_Grid_Functional_Real_Node(fid, "Xrain", i + 1)

    iric.cg_iRIC_Close(fid)

    util.remove("data/case_gridreadfunc.cgn")

def case_GridWrite():
    shutil.copy("data/case_nogrid_hdf5.cgn", "data/case_gridwrite1d.cgn")

    fid = iric.cg_iRIC_Open("data/case_gridwrite1d.cgn", iric.IRIC_MODE_MODIFY)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    isize = 10
    x = np.zeros(isize, dtype=np.float64)

    for i in range(isize):
        x[i] = i * 2

    iric.cg_iRIC_Write_Grid1d_Coords(fid, isize, x)
    iric.cg_iRIC_Write_NamedGrid1d_Coords(fid, "testgrid", isize, x)

    iric.cg_iRIC_Close(fid)

    """
    ier, fid = iric.cg_iRIC_Open("case_gridwrite1d.cgn", iric.IRIC_MODE_READ)
    util.verify_log("cg_iRIC_Open() ier == 0", ier == 0)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    ier = iric.cg_goto(fid, 2, "iRICZone", 0, "GridCoordinates", 0, NULL)
    util.verify_log("cg_goto() ier == 0", ier == 0)
    int dim
    char name[32]
    DataType_t datatype
    cgsize_t dimVec[12]
    ier = cg_array_info(1, name, &datatype, &dim, dimVec)
    util.verify_log("cg_array_info() ier == 0", ier == 0)
    util.verify_log("cg_array_info() name == CoordinateX", std::string("CoordinateX") == name)
    util.verify_log("cg_array_info() datatype == RealDouble", datatype == RealDouble)
    util.verify_log("cg_array_info() dim == 1", dim == 1)
    util.verify_log("cg_array_info() dimVec[0] == 10", dimVec[0] == 10)

    std::vector<double> read_x, read_y, read_z
    read_x.assign(dimVec[0], 0)
    ier = cg_array_read(1, read_x.data())
    util.verify_log("cg_array_read() ier == 0", ier == 0)
    util.verify_log("cg_array_read() value valid", x == read_x)

    cg_iRIC_Close(fid)
    """

    util.remove("data/case_gridwrite1d.cgn")

    shutil.copy("data/case_nogrid_hdf5.cgn", "data/case_gridwrite2d.cgn")

    fid = iric.cg_iRIC_Open("data/case_gridwrite2d.cgn", iric.IRIC_MODE_MODIFY)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    isize = 10
    jsize = 8
    x = np.zeros(isize * jsize, dtype=np.float64)
    y = np.zeros(isize * jsize, dtype=np.float64)

    for j in range(jsize):
        for i in range(isize):
            idx = i + isize * j
            x[idx] = i
            y[idx] = j

    iric.cg_iRIC_Write_Grid2d_Coords(fid, isize, jsize, x, y)

    real_node_write = np.zeros(isize * jsize, dtype=np.float64)
    int_node_write = np.zeros(isize * jsize, dtype=np.int32)
    real_cell_write = np.zeros((isize - 1) * (jsize - 1), dtype=np.float64)
    int_cell_write = np.zeros((isize - 1) * (jsize - 1), dtype=np.int32)

    for i in range(real_node_write.size):
        real_node_write[i] = 0.5 * i - 0.01 * i * (i - 50)

    for i in range(int_node_write.size):
        int_node_write[i] = i * i + i * 2 + 6

    for i in range(real_cell_write.size):
        real_cell_write[i] = 0.8 * i - 0.0005 * i * (i - 10)

    for i in range(int_cell_write.size):
        int_cell_write[i] = i * i - i * 4 + 414

    iric.cg_iRIC_Write_Grid_Real_Node(fid, "realnode_test", real_node_write)

    iric.cg_iRIC_Write_Grid_Integer_Node(fid, "intnode_test", int_node_write)

    iric.cg_iRIC_Write_Grid_Real_Cell(fid, "realcell_test", real_cell_write)

    iric.cg_iRIC_Write_Grid_Integer_Cell(fid, "intcell_test", int_cell_write)

    iric.cg_iRIC_Write_NamedGrid2d_Coords(fid, "testgrid", isize, jsize, x, y)

    iric.cg_iRIC_Close(fid)

    """
    ier = cg_iRIC_Open("case_gridwrite2d.cgn", IRIC_MODE_READ, &fid)
    util.verify_log("cg_iRIC_Open() ier == 0", ier == 0)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    cgsize_t size[9]
    ier = cg_zone_read(fid, 1, 1, name, size)
    util.verify_log("cg_zone_read() ier == 0", ier == 0)
    util.verify_log("cg_zone_read() name == iRICZone", strcmp(name, "iRICZone") == 0)
    util.verify_log("cg_zone_read() size[0] == isize",   size[0] == isize)
    util.verify_log("cg_zone_read() size[1] == jsize",   size[1] == jsize)
    util.verify_log("cg_zone_read() size[2] == isize-1", size[2] == isize-1)
    util.verify_log("cg_zone_read() size[3] == jsize-1", size[3] == jsize-1)
    util.verify_log("cg_zone_read() size[4] == 0",       size[4] == 0)
    util.verify_log("cg_zone_read() size[5] == 0",       size[5] == 0)

    ier = cg_goto(fid, 1, "iRICZone", 0, "GridCoordinates", 0, NULL)
    util.verify_log("cg_goto() ier == 0", ier == 0)
    ier = cg_array_info(1, name, &datatype, &dim, dimVec)
    util.verify_log("cg_array_info() ier == 0", ier == 0)
    util.verify_log("cg_array_info() name == CoordinateX", std::string("CoordinateX") == name)
    util.verify_log("cg_array_info() datatype == RealDouble", datatype == RealDouble)

    read_x.assign(dimVec[0] * dimVec[1], 0)
    read_y.assign(dimVec[0] * dimVec[1], 0)

    ier = cg_array_read(1, read_x.data())
    util.verify_log("cg_array_read() ier == 0", ier == 0)
    util.verify_log("cg_array_read() value valid", x == read_x)

    ier = cg_array_read(2, read_y.data())
    util.verify_log("cg_array_read() ier == 0", ier == 0)
    util.verify_log("cg_array_read() value valid", y == read_y)

    ier = cg_goto(fid, 1, "iRICZone", 0, "GridConditions", 0, "realnode_test", 0, NULL)
    util.verify_log("cg_goto() for realnode_test ier == 0", ier == 0)
    ier = cg_array_info(1, name, &datatype, &dim, dimVec)
    std::vector<double> real_node_read
    real_node_read.assign(dimVec[0], 0)
    ier = cg_array_read(1, real_node_read.data())
    util.verify_log("cg_array_read() for realnode_test ier == 0", ier == 0)
    util.verify_log("realnode_test value check", real_node_read == real_node_write)

    ier = cg_goto(fid, 1, "iRICZone", 0, "GridConditions", 0, "intnode_test", 0, NULL)
    util.verify_log("cg_goto() for intnode_test ier == 0", ier == 0)
    ier = cg_array_info(1, name, &datatype, &dim, dimVec)
    std::vector<int> int_node_read
    int_node_read.assign(dimVec[0], 0)
    ier = cg_array_read(1, int_node_read.data())
    util.verify_log("cg_array_read() for intnode_test ier == 0", ier == 0)
    util.verify_log("intnode_test value check", int_node_read == int_node_write)

    ier = cg_goto(fid, 1, "iRICZone", 0, "GridConditions", 0, "realcell_test", 0, NULL)
    util.verify_log("cg_goto() for realcell_test ier == 0", ier == 0)
    ier = cg_array_info(1, name, &datatype, &dim, dimVec)
    std::vector<double> real_cell_read
    real_cell_read.assign(dimVec[0], 0)
    ier = cg_array_read(1, real_cell_read.data())
    util.verify_log("cg_array_read() for realcell_test ier == 0", ier == 0)
    util.verify_log("realcell_test value check", real_cell_read == real_cell_write)

    ier = cg_goto(fid, 1, "iRICZone", 0, "GridConditions", 0, "intcell_test", 0, NULL)
    util.verify_log("cg_goto() for intcell_test ier == 0", ier == 0)
    ier = cg_array_info(1, name, &datatype, &dim, dimVec)
    std::vector<int> int_cell_read
    int_cell_read.assign(dimVec[0], 0)
    ier = cg_array_read(1, int_cell_read.data())
    util.verify_log("cg_array_read() for intcell_test ier == 0", ier == 0)
    util.verify_log("intcell_test value check", int_cell_read == int_cell_write)

    cg_iRIC_Close(fid)
    """

    util.remove("data/case_gridwrite2d.cgn")

    shutil.copy("data/case_nogrid_hdf5.cgn", "data/case_gridwrite3d.cgn")

    fid = iric.cg_iRIC_Open("data/case_gridwrite3d.cgn", iric.IRIC_MODE_MODIFY)

    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    isize = 11
    jsize = 9
    ksize = 5
    size = isize * jsize * ksize
    x = np.zeros(size, dtype=np.float64)
    y = np.zeros(size, dtype=np.float64)
    z = np.zeros(size, dtype=np.float64)

    for k in range(ksize):
        for j in range(jsize):
            for i in range(isize):
                idx = i + isize * j + isize * jsize * k
                x[idx] = i
                y[idx] = j
                z[idx] = k

    iric.cg_iRIC_Write_Grid3d_Coords(fid, isize, jsize, ksize, x, y, z)
    iric.cg_iRIC_Write_NamedGrid3d_Coords(fid, "testgrid", isize, jsize, ksize, x, y, z)

    iric.cg_iRIC_Close(fid)

    """
    ier = cg_iRIC_Open("case_gridwrite3d.cgn", IRIC_MODE_READ, &fid)
    util.verify_log("cg_iRIC_Open() ier == 0", ier == 0)
    util.verify_log("cg_iRIC_Open() fid != 0", fid != 0)

    ier = cg_zone_read(fid, 2, 1, name, size)
    util.verify_log("cg_zone_read() ier == 0", ier == 0)
    util.verify_log("cg_zone_read() name == iRICZone", strcmp(name, "iRICZone") == 0)
    util.verify_log("cg_zone_read() size[0] == isize",   size[0] == isize)
    util.verify_log("cg_zone_read() size[1] == jsize",   size[1] == jsize)
    util.verify_log("cg_zone_read() size[2] == ksize",   size[2] == ksize)
    util.verify_log("cg_zone_read() size[3] == isize-1", size[3] == isize-1)
    util.verify_log("cg_zone_read() size[4] == jsize-1", size[4] == jsize-1)
    util.verify_log("cg_zone_read() size[5] == ksize-1", size[5] == ksize-1)
    util.verify_log("cg_zone_read() size[6] == 0",       size[6] == 0)
    util.verify_log("cg_zone_read() size[7] == 0",       size[7] == 0)
    util.verify_log("cg_zone_read() size[8] == 0",       size[8] == 0)

    ier = cg_goto(fid, 2, "iRICZone", 0, "GridCoordinates", 0, NULL)
    util.verify_log("cg_goto() ier == 0", ier == 0)
    ier = cg_array_info(1, name, &datatype, &dim, dimVec)
    util.verify_log("cg_array_info() ier == 0", ier == 0)
    util.verify_log("cg_array_info() name == CoordinateX", std::string("CoordinateX") == name)
    util.verify_log("cg_array_info() datatype == RealDouble", datatype == RealDouble)

    read_x.assign(dimVec[0] * dimVec[1] * dimVec[2], 0)
    read_y.assign(dimVec[0] * dimVec[1] * dimVec[2], 0)
    read_z.assign(dimVec[0] * dimVec[1] * dimVec[2], 0)

    ier = cg_array_read(1, read_x.data())
    util.verify_log("cg_array_read() ier == 0", ier == 0)
    util.verify_log("cg_array_read() value valid", x == read_x)

    ier = cg_array_read(2, read_y.data())
    util.verify_log("cg_array_read() ier == 0", ier == 0)
    util.verify_log("cg_array_read() value valid", y == read_y)

    ier = cg_array_read(3, read_z.data())
    util.verify_log("cg_array_read() ier == 0", ier == 0)
    util.verify_log("cg_array_read() value valid", z == read_z)

    cg_iRIC_Close(fid)
    """

    util.remove("data/case_gridwrite3d.cgn")

def case_GridCopy():
    shutil.copy("data/case_init_hdf5.cgn", "data/case_grid.cgn")
    shutil.copy("data/case_nogrid_hdf5.cgn", "data/case_gridwrite2d.cgn")

    fid_from = iric.cg_iRIC_Open("data/case_grid.cgn", iric.IRIC_MODE_READ)
    util.verify_log("cg_iRIC_Open() fid_from != 0", fid_from != 0)
    fid_to = iric.cg_iRIC_Open("data/case_gridwrite2d.cgn", iric.iRIC_MODE_MODIFY)
    util.verify_log("cg_iRIC_Open() fid_to != 0", fid_to != 0)
    
    iric.cg_iRIC_Copy_Grid(fid_from, fid_to)

    iric.cg_iRIC_Close(fid_from)
    iric.cg_iRIC_Close(fid_to)

    util.remove("data/case_grid.cgn")
    util.remove("data/case_gridwrite2d.cgn")
