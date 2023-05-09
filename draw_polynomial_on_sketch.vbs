' ******************************************************************************
' C:\Users\hanyuan\AppData\Local\Temp\swx15336\Macro1.swb - macro recorded on 05/09/23 by hanyuan
' ******************************************************************************
Dim swApp As Object

Dim Part As Object
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long

Sub main()

Set swApp = Application.SldWorks

Set Part = swApp.ActiveDoc
Dim myModelView As Object
Set myModelView = Part.ActiveView
myModelView.FrameState = swWindowState_e.swWindowMaximized
boolstatus = Part.Extension.SelectByID2("»ù×¼Ãæ78", "PLANE", 3.52968146261616E-02, 4.97973018017701E-02, -2.26801835693101E-02, False, 0, Nothing, 0)
Part.SketchManager.InsertSketch True
Part.ClearSelection2 True
Dim skSegment As Object
Set skSegment = Part.SketchManager.CreateCenterLine(0#, 0#, 0#, 0.051494, 0#, 0#)
Set skSegment = Part.SketchManager.CreateLine(0.051494, 0#, 0#, 0.077358, 0#, 0#)
Set skSegment = Part.SketchManager.CreateLine(0.051494, 0#, 0#, 0.051494, 0.015, 0#)
Set skSegment = Part.SketchManager.CreateLine(0.077358, 0#, 0#, 0.077358, 0.01, 0#)
Part.ClearSelection2 True
boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 3.49134929010702E-02, -4.16105912792432E-04, -3.05496193701998E-02, False, 0, Nothing, 0)
Dim myDisplayDim As Object
Set myDisplayDim = Part.AddDimension2(2.45367033924497E-02, -9.77727992924278E-03, -1.41662723086569E-02)
Part.ClearSelection2 True
Dim myDimension As Object
Set myDimension = Part.Parameter("D1@²ÝÍ¼38")
myDimension.SystemValue = 0.045
boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 3.99321457235744E-02, 1.42387070837323E-04, -0.032136510426034, False, 0, Nothing, 0)
Set myDisplayDim = Part.AddDimension2(0.049050258091531, -6.94183171016569E-03, -2.83191797129661E-02)
boolstatus = Part.Extension.SelectByID2("D1@²ÝÍ¼38@Áã¼þ1.SLDPRT", "DIMENSION", 0, 0, 0, False, 0, Nothing, 0)
Part.ClearSelection2 True
Set myDimension = Part.Parameter("D2@²ÝÍ¼38")
myDimension.SystemValue = 0.027
Part.ClearSelection2 True
boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 3.50386623922513E-02, 6.97359803823314E-03, -2.93112565074198E-02, False, 0, Nothing, 0)
Set myDisplayDim = Part.AddDimension2(0.02940328770157, 8.15430116840038E-03, -1.69759960695615E-02)
Part.ClearSelection2 True
Set myDimension = Part.Parameter("D3@²ÝÍ¼38")
myDimension.SystemValue = 0.015
boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 5.83374860145208E-02, 6.04590272167322E-03, -4.27628385975387E-02, False, 0, Nothing, 0)
Set myDisplayDim = Part.AddDimension2(7.14726369380641E-02, 3.09414489625533E-03, -4.12647461758838E-02)
boolstatus = Part.Extension.SelectByID2("D3@²ÝÍ¼38@Áã¼þ1.SLDPRT", "DIMENSION", 0, 0, 0, False, 0, Nothing, 0)
Part.ClearSelection2 True
Set myDimension = Part.Parameter("D4@²ÝÍ¼38")
myDimension.SystemValue = 0.01
Part.ClearSelection2 True
Dim equationDriveCurve As Object
Set equationDriveCurve = Part.SketchManager.CreateEquationSpline2("", "-0.029012345679012307*x*x+3.209259259259255*x-70.66666666666656", "", "45", "45+27", False, 0, 0, 0, True, True)
boolstatus = Part.Extension.SelectByID2("D3@²ÝÍ¼38@Áã¼þ1.SLDPRT", "DIMENSION", 2.49595474710187E-02, 8.99766054709117E-03, -2.34920767944529E-02, False, 0, Nothing, 0)
Part.EditDelete
Part.SketchManager.InsertSketch True
End Sub
