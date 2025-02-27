#ifndef IRICLIB_GRID_H
#define IRICLIB_GRID_H

#include "iriclib_global.h"

#ifdef __cplusplus
extern "C" {
#endif

int IRICLIBDLL cg_iRIC_Read_Grid2d_Str_Size_WithGridId(int fid, int gid, int* isize, int* jsize);
int IRICLIBDLL cg_iRIC_Read_Grid2d_Coords_WithGridId(int fid, int gid, double* x_arr, double* y_arr);
int IRICLIBDLL cg_iRIC_Read_Grid3d_Str_Size_WithGridId(int fid, int gid, int* isize, int* jsize, int* ksize);
int IRICLIBDLL cg_iRIC_Read_Grid3d_Coords_WithGridId(int fid, int gid, double* x_arr, double* y_arr, double* z_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_CellType_WithGridId(int fid, int gid, int* type);
int IRICLIBDLL cg_iRIC_Read_Grid_TriangleElementsSize_WithGridId(int fid, int gid, int* tsize);
int IRICLIBDLL cg_iRIC_Read_Grid_TriangleElementsSize2_WithGridId(int fid, int gid, int* tsize);
int IRICLIBDLL cg_iRIC_Read_Grid_TriangleElements_WithGridId(int fid, int gid, int* id_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_LineElementsSize_WithGridId(int fid, int gid, int* tsize);
int IRICLIBDLL cg_iRIC_Read_Grid_LineElementsSize2_WithGridId(int fid, int gid, int* tsize);
int IRICLIBDLL cg_iRIC_Read_Grid_LineElements_WithGridId(int fid, int gid, int* id_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_NodeCount_WithGridId(int fid, int gid, int* count);
int IRICLIBDLL cg_iRIC_Read_Grid_CellCount_WithGridId(int fid, int gid, int* count);
int IRICLIBDLL cg_iRIC_Read_Grid_IFaceCount_WithGridId(int fid, int gid, int* count);
int IRICLIBDLL cg_iRIC_Read_Grid_JFaceCount_WithGridId(int fid, int gid, int* count);
int IRICLIBDLL cg_iRIC_Read_Grid_KFaceCount_WithGridId(int fid, int gid, int* count);
int IRICLIBDLL cg_iRIC_Read_Grid_Real_Node_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Integer_Node_WithGridId(int fid, int gid, const char* name, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Real_Cell_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Integer_Cell_WithGridId(int fid, int gid, const char* name, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Real_IFace_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Integer_IFace_WithGridId(int fid, int gid, const char* name, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Real_JFace_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Integer_JFace_WithGridId(int fid, int gid, const char* name, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_FunctionalDimensionSize_WithGridId(int fid, int gid, const char* name, const char* dimname, int* count);
int IRICLIBDLL cg_iRIC_Read_Grid_FunctionalDimension_Integer_WithGridId(int fid, int gid, const char* name, const char* dimname, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_FunctionalDimension_Real_WithGridId(int fid, int gid, const char* name, const char* dimname, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_FunctionalTimeSize_WithGridId(int fid, int gid, const char* name, int* count);
int IRICLIBDLL cg_iRIC_Read_Grid_FunctionalTime_WithGridId(int fid, int gid, const char* name, double* time_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Integer_Node_WithGridId(int fid, int gid, const char* name, int dimid, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Real_Node_WithGridId(int fid, int gid, const char* name, int dimid, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Integer_Cell_WithGridId(int fid, int gid, const char* name, int dimid, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Real_Cell_WithGridId(int fid, int gid, const char* name, int dimid, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Integer_IFace_WithGridId(int fid, int gid, const char* name, int dimid, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Real_IFace_WithGridId(int fid, int gid, const char* name, int dimid, double* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Integer_JFace_WithGridId(int fid, int gid, const char* name, int dimid, int* v_arr);
int IRICLIBDLL cg_iRIC_Read_Grid_Functional_Real_JFace_WithGridId(int fid, int gid, const char* name, int dimid, double* v_arr);

int IRICLIBDLL cg_iRIC_Write_Grid1d_Coords_WithGridId(int fid, int isize, double* x_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_Grid2d_Coords_WithGridId(int fid, int isize, int jsize, double* x_arr, double* y_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_Grid3d_Coords_WithGridId(int fid, int isize, int jsize, int ksize, double* x_arr, double* y_arr, double* z_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_NamedGrid1d_Coords_WithGridId(int fid, const char* name, int isize, double* x_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_NamedGrid2d_Coords_WithGridId(int fid, const char* name, int isize, int jsize, double* x_arr, double* y_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_NamedGrid3d_Coords_WithGridId(int fid, const char* name, int isize, int jsize, int ksize, double* x_arr, double* y_arr, double* z_arr, int* gid);

int IRICLIBDLL cg_iRIC_Write_Grid2d_Unst_Triangles_WithGridId(int fid, int psize, double* x_arr, double* y_arr, int csize, int* idx_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_Grid2d_Unst_Lines_WithGridId(int fid, int psize, double* x_arr, double* y_arr, int csize, int* idx_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_Grid3d_Unst_Lines_WithGridId(int fid, int psize, double* x_arr, double* y_arr, double* z_arr, int csize, int* idx_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_NamedGrid2d_Unst_Triangles_WithGridId(int fid, const char* name, int psize, double* x_arr, double* y_arr, int csize, int* idx_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_NamedGrid2d_Unst_Lines_WithGridId(int fid, const char* name, int psize, double* x_arr, double* y_arr, int csize, int* idx_arr, int* gid);
int IRICLIBDLL cg_iRIC_Write_NamedGrid3d_Unst_Lines_WithGridId(int fid, const char* name, int psize, double* x_arr, double* y_arr, double* z_arr, int csize, int* idx_arr, int* gid);

int IRICLIBDLL cg_iRIC_Write_Grid_Real_Node_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Write_Grid_Integer_Node_WithGridId(int fid, int gid, const char* name, int* v_arr);
int IRICLIBDLL cg_iRIC_Write_Grid_Real_Cell_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Write_Grid_Integer_Cell_WithGridId(int fid, int gid, const char* name, int* v_arr);
int IRICLIBDLL cg_iRIC_Write_Grid_Real_IFace_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Write_Grid_Integer_IFace_WithGridId(int fid, int gid, const char* name, int* v_arr);
int IRICLIBDLL cg_iRIC_Write_Grid_Real_JFace_WithGridId(int fid, int gid, const char* name, double* v_arr);
int IRICLIBDLL cg_iRIC_Write_Grid_Integer_JFace_WithGridId(int fid, int gid, const char* name, int* v_arr);

int IRICLIBDLL cg_iRIC_Copy_Grid_WithGridId(int fid_from, int fid_to, int gid);

#ifdef __cplusplus
}
#endif

#endif // IRICLIB_GRID_H
