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
boolstatus = Part.Extension.SelectByID2("基准面79", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
Part.SketchManager.InsertSketch True
Part.ClearSelection2 True
Dim skSegment As Object
Set skSegment = Part.SketchManager.CreateCenterLine(0#, 0#, 0#, 0.055288, 0.000611, 0#)
boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 3.85638185466762E-02, 4.20641766462358E-04, -3.43869040104364E-02, False, 0, Nothing, 0)
Part.SketchAddConstraints "sgHORIZONTAL2D"
Part.ClearSelection2 True
boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 3.58776716337902E-02, -3.39115312483637E-04, -3.17007570975504E-02, False, 0, Nothing, 0)
Dim myDisplayDim As Object
Set myDisplayDim = Part.AddDimension2(3.47965194580272E-02, -8.2215950065483E-03, -3.47965194580273E-02)
Part.ClearSelection2 True
Dim myDimension As Object
Set myDimension = Part.Parameter("D1@草图39")
myDimension.SystemValue = 0.045
Part.ClearSelection2 True
Set skSegment = Part.SketchManager.CreateLine(0.045, 0#, 0#, 0.073673, 0#, 0#)
Set skSegment = Part.SketchManager.CreateLine(0.073673, 0#, 0#, 0.073673, 0.009308, 0#)
Part.SetPickMode
Part.ClearSelection2 True
Part.SetPickMode
boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 3.99668485919903E-02, -4.41171668993309E-05, -3.65673679230033E-02, False, 0, Nothing, 0)
Set myDisplayDim = Part.AddDimension2(3.93055457457067E-02, -3.9860746067244E-03, -3.93055457457068E-02)
Part.ClearSelection2 True
Set myDimension = Part.Parameter("D2@草图39")
myDimension.SystemValue = 0.027
boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 5.28106806833536E-02, 3.74325370665808E-03, -4.94112000143667E-02, False, 0, Nothing, 0)
Set myDisplayDim = Part.AddDimension2(5.59205455575255E-02, 4.59347982113014E-03, -5.59205455575257E-02)
boolstatus = Part.Extension.SelectByID2("D2@草图39@零件1.SLDPRT", "DIMENSION", 0, 0, 0, False, 0, Nothing, 0)
Part.ClearSelection2 True
Set myDimension = Part.Parameter("D3@草图39")
myDimension.SystemValue = 0.01
Part.ClearSelection2 True
Set skSegment = Part.SketchManager.CreateLine(0.045, 0#, 0#, 0.045, 0.017811, 0#)
Part.ClearSelection2 True
boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 3.36269144532748E-02, 1.31730342489847E-02, -3.02274337842878E-02, False, 0, Nothing, 0)
Set myDisplayDim = Part.AddDimension2(2.49860393289921E-02, 9.69483650796257E-03, -2.49860393289922E-02)
Part.ClearSelection2 True
Set myDimension = Part.Parameter("D4@草图39")
myDimension.SystemValue = 0.015
boolstatus = Part.Extension.SelectByID2("D4@草图39@零件1.SLDPRT", "DIMENSION", 2.67404342681183E-02, 9.54024994169494E-03, -2.33409535991313E-02, False, 0, Nothing, 0)
Part.EditDelete
Dim equationDriveCurve As Object
Set equationDriveCurve = Part.SketchManager.CreateEquationSpline2("", "-0.029012345679012307*x*x+3.209259259259255*x-70.66666666666656", "", "45", "45+27", False, 0, 0, 0, True, True)
Part.ClearSelection2 True
Part.SketchManager.InsertSketch True
End Sub
