#python

lx.eval("tool.drop")
lx.eval("tool.clearTask axis")
lx.eval("tool.clearTask snap")
lx.eval("tool.clearTask falloff")


if lx.eval("select.typeFrom vertex;edge;polygon;item;pivot;center;ptag ?"):
    lx.eval("select.drop vertex")
    
elif lx.eval("select.typeFrom edge;vertex;polygon;item;pivot;center;ptag ?"):
    lx.eval("select.drop edge")
    
elif lx.eval("select.typeFrom polygon;vertex;edge;item;pivot;center;ptag ?"):
    lx.eval("select.drop polygon")
    
elif lx.eval("select.typeFrom item;vertex;polygon;edge;pivot;center;ptag ?"):
    lx.eval("select.drop edge")
    
elif lx.eval("select.typeFrom pivot;vertex;polygon;item;edge;center;ptag ?"):
    lx.eval("select.drop pivot")
    
elif lx.eval("select.typeFrom center;vertex;polygon;item;pivot;edge;ptag ?"):
    lx.eval("select.drop center")
    
elif lx.eval("select.typeFrom ptag;vertex;polygon;item;pivot;center;edge ?"):
    lx.eval("select.drop ptag")