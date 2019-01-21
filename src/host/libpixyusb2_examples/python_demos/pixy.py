# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pixy')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pixy')
    _pixy = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pixy', [dirname(__file__)])
        except ImportError:
            import _pixy
            return _pixy
        try:
            _mod = imp.load_module('_pixy', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pixy = swig_import_helper()
    del swig_import_helper
else:
    import _pixy
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class BlockArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BlockArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BlockArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _pixy.new_BlockArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pixy.delete_BlockArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _pixy.BlockArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _pixy.BlockArray___setitem__(self, index, value)

    def cast(self):
        return _pixy.BlockArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_pixy.BlockArray_frompointer)
    else:
        frompointer = _pixy.BlockArray_frompointer
BlockArray_swigregister = _pixy.BlockArray_swigregister
BlockArray_swigregister(BlockArray)

def BlockArray_frompointer(t):
    return _pixy.BlockArray_frompointer(t)
BlockArray_frompointer = _pixy.BlockArray_frompointer

class VectorArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _pixy.new_VectorArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pixy.delete_VectorArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _pixy.VectorArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _pixy.VectorArray___setitem__(self, index, value)

    def cast(self):
        return _pixy.VectorArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_pixy.VectorArray_frompointer)
    else:
        frompointer = _pixy.VectorArray_frompointer
VectorArray_swigregister = _pixy.VectorArray_swigregister
VectorArray_swigregister(VectorArray)

def VectorArray_frompointer(t):
    return _pixy.VectorArray_frompointer(t)
VectorArray_frompointer = _pixy.VectorArray_frompointer

class IntersectionLineArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntersectionLineArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntersectionLineArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _pixy.new_IntersectionLineArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pixy.delete_IntersectionLineArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _pixy.IntersectionLineArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _pixy.IntersectionLineArray___setitem__(self, index, value)

    def cast(self):
        return _pixy.IntersectionLineArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_pixy.IntersectionLineArray_frompointer)
    else:
        frompointer = _pixy.IntersectionLineArray_frompointer
IntersectionLineArray_swigregister = _pixy.IntersectionLineArray_swigregister
IntersectionLineArray_swigregister(IntersectionLineArray)

def IntersectionLineArray_frompointer(t):
    return _pixy.IntersectionLineArray_frompointer(t)
IntersectionLineArray_frompointer = _pixy.IntersectionLineArray_frompointer

class BarcodeArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BarcodeArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BarcodeArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _pixy.new_BarcodeArray(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pixy.delete_BarcodeArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _pixy.BarcodeArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _pixy.BarcodeArray___setitem__(self, index, value)

    def cast(self):
        return _pixy.BarcodeArray_cast(self)
    if _newclass:
        frompointer = staticmethod(_pixy.BarcodeArray_frompointer)
    else:
        frompointer = _pixy.BarcodeArray_frompointer
BarcodeArray_swigregister = _pixy.BarcodeArray_swigregister
BarcodeArray_swigregister(BarcodeArray)

def BarcodeArray_frompointer(t):
    return _pixy.BarcodeArray_frompointer(t)
BarcodeArray_frompointer = _pixy.BarcodeArray_frompointer


def init():
    return _pixy.init()
init = _pixy.init

def changeProg(program_name):
    return _pixy.changeProg(program_name)
changeProg = _pixy.changeProg

def getFrameWidth():
    return _pixy.getFrameWidth()
getFrameWidth = _pixy.getFrameWidth

def getFrameHeight():
    return _pixy.getFrameHeight()
getFrameHeight = _pixy.getFrameHeight

def cccGetBlocks(max_blocks, blocks):
    return _pixy.cccGetBlocks(max_blocks, blocks)
cccGetBlocks = _pixy.cccGetBlocks

def lineGetAllFeatures():
    return _pixy.lineGetAllFeatures()
lineGetAllFeatures = _pixy.lineGetAllFeatures

def lineGetMainFeatures():
    return _pixy.lineGetMainFeatures()
lineGetMainFeatures = _pixy.lineGetMainFeatures

def lineGetIntersections(max_intersections, intersections):
    return _pixy.lineGetIntersections(max_intersections, intersections)
lineGetIntersections = _pixy.lineGetIntersections

def lineGetVectors(max_vectors, vectors):
    return _pixy.lineGetVectors(max_vectors, vectors)
lineGetVectors = _pixy.lineGetVectors

def lineGetBarcodes(max_barcodes, barcodes):
    return _pixy.lineGetBarcodes(max_barcodes, barcodes)
lineGetBarcodes = _pixy.lineGetBarcodes

def setServos(S1_Position, S2_Position):
    return _pixy.setServos(S1_Position, S2_Position)
setServos = _pixy.setServos

def setNextTurn(deg):
    return _pixy.setNextTurn(deg)
setNextTurn = _pixy.setNextTurn

def setLamp(upper, lower):
    return _pixy.setLamp(upper, lower)
setLamp = _pixy.setLamp

def setMode(turnDelayed, manualVector, whiteLine):
    return _pixy.setMode(turnDelayed, manualVector, whiteLine)
setMode = _pixy.setMode

def videoGetRGB(X, Y):
    return _pixy.videoGetRGB(X, Y)
videoGetRGB = _pixy.videoGetRGB
class Block(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Block, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Block, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m_signature"] = _pixy.Block_m_signature_set
    __swig_getmethods__["m_signature"] = _pixy.Block_m_signature_get
    if _newclass:
        m_signature = _swig_property(_pixy.Block_m_signature_get, _pixy.Block_m_signature_set)
    __swig_setmethods__["m_x"] = _pixy.Block_m_x_set
    __swig_getmethods__["m_x"] = _pixy.Block_m_x_get
    if _newclass:
        m_x = _swig_property(_pixy.Block_m_x_get, _pixy.Block_m_x_set)
    __swig_setmethods__["m_y"] = _pixy.Block_m_y_set
    __swig_getmethods__["m_y"] = _pixy.Block_m_y_get
    if _newclass:
        m_y = _swig_property(_pixy.Block_m_y_get, _pixy.Block_m_y_set)
    __swig_setmethods__["m_width"] = _pixy.Block_m_width_set
    __swig_getmethods__["m_width"] = _pixy.Block_m_width_get
    if _newclass:
        m_width = _swig_property(_pixy.Block_m_width_get, _pixy.Block_m_width_set)
    __swig_setmethods__["m_height"] = _pixy.Block_m_height_set
    __swig_getmethods__["m_height"] = _pixy.Block_m_height_get
    if _newclass:
        m_height = _swig_property(_pixy.Block_m_height_get, _pixy.Block_m_height_set)
    __swig_setmethods__["m_angle"] = _pixy.Block_m_angle_set
    __swig_getmethods__["m_angle"] = _pixy.Block_m_angle_get
    if _newclass:
        m_angle = _swig_property(_pixy.Block_m_angle_get, _pixy.Block_m_angle_set)
    __swig_setmethods__["m_index"] = _pixy.Block_m_index_set
    __swig_getmethods__["m_index"] = _pixy.Block_m_index_get
    if _newclass:
        m_index = _swig_property(_pixy.Block_m_index_get, _pixy.Block_m_index_set)
    __swig_setmethods__["m_age"] = _pixy.Block_m_age_set
    __swig_getmethods__["m_age"] = _pixy.Block_m_age_get
    if _newclass:
        m_age = _swig_property(_pixy.Block_m_age_get, _pixy.Block_m_age_set)

    def __init__(self):
        this = _pixy.new_Block()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pixy.delete_Block
    __del__ = lambda self: None
Block_swigregister = _pixy.Block_swigregister
Block_swigregister(Block)

class Vector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m_x0"] = _pixy.Vector_m_x0_set
    __swig_getmethods__["m_x0"] = _pixy.Vector_m_x0_get
    if _newclass:
        m_x0 = _swig_property(_pixy.Vector_m_x0_get, _pixy.Vector_m_x0_set)
    __swig_setmethods__["m_y0"] = _pixy.Vector_m_y0_set
    __swig_getmethods__["m_y0"] = _pixy.Vector_m_y0_get
    if _newclass:
        m_y0 = _swig_property(_pixy.Vector_m_y0_get, _pixy.Vector_m_y0_set)
    __swig_setmethods__["m_x1"] = _pixy.Vector_m_x1_set
    __swig_getmethods__["m_x1"] = _pixy.Vector_m_x1_get
    if _newclass:
        m_x1 = _swig_property(_pixy.Vector_m_x1_get, _pixy.Vector_m_x1_set)
    __swig_setmethods__["m_y1"] = _pixy.Vector_m_y1_set
    __swig_getmethods__["m_y1"] = _pixy.Vector_m_y1_get
    if _newclass:
        m_y1 = _swig_property(_pixy.Vector_m_y1_get, _pixy.Vector_m_y1_set)
    __swig_setmethods__["m_index"] = _pixy.Vector_m_index_set
    __swig_getmethods__["m_index"] = _pixy.Vector_m_index_get
    if _newclass:
        m_index = _swig_property(_pixy.Vector_m_index_get, _pixy.Vector_m_index_set)
    __swig_setmethods__["m_flags"] = _pixy.Vector_m_flags_set
    __swig_getmethods__["m_flags"] = _pixy.Vector_m_flags_get
    if _newclass:
        m_flags = _swig_property(_pixy.Vector_m_flags_get, _pixy.Vector_m_flags_set)

    def __init__(self):
        this = _pixy.new_Vector()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pixy.delete_Vector
    __del__ = lambda self: None
Vector_swigregister = _pixy.Vector_swigregister
Vector_swigregister(Vector)

class IntersectionLine(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntersectionLine, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntersectionLine, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m_index"] = _pixy.IntersectionLine_m_index_set
    __swig_getmethods__["m_index"] = _pixy.IntersectionLine_m_index_get
    if _newclass:
        m_index = _swig_property(_pixy.IntersectionLine_m_index_get, _pixy.IntersectionLine_m_index_set)
    __swig_setmethods__["m_reserved"] = _pixy.IntersectionLine_m_reserved_set
    __swig_getmethods__["m_reserved"] = _pixy.IntersectionLine_m_reserved_get
    if _newclass:
        m_reserved = _swig_property(_pixy.IntersectionLine_m_reserved_get, _pixy.IntersectionLine_m_reserved_set)
    __swig_setmethods__["m_angle"] = _pixy.IntersectionLine_m_angle_set
    __swig_getmethods__["m_angle"] = _pixy.IntersectionLine_m_angle_get
    if _newclass:
        m_angle = _swig_property(_pixy.IntersectionLine_m_angle_get, _pixy.IntersectionLine_m_angle_set)

    def __init__(self):
        this = _pixy.new_IntersectionLine()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pixy.delete_IntersectionLine
    __del__ = lambda self: None
IntersectionLine_swigregister = _pixy.IntersectionLine_swigregister
IntersectionLine_swigregister(IntersectionLine)

# This file is compatible with both classic and new-style classes.


