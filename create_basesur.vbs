' ******************************************************************************
' C:\Users\hanyuan\AppData\Local\Temp\swx15336\Macro1.swb - macro recorded on 05/09/23 by hanyuan
' ******************************************************************************
Dim swApp As Object

Dim Part As Object
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
Dim Model As Object
Dim strSketchName As String
Dim lineAtSketch As String

Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc
Set Model = swApp.ActiveDoc
Dim myModelView As Object
Set myModelView = Part.ActiveView
myModelView.FrameState = swWindowState_e.swWindowMaximized
boolstatus = Part.Extension.SelectByID2("前视基准面", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

Dim myRefPlane As Object
Set myRefPlane = Part.FeatureManager.InsertRefPlane(8, 0, 0, 0, 0, 0)
Debug.Print (myRefPlane.name & " selected")
Dim name As String
'Set name = Part.GetEntityName(myRefPlane)
boolstatus = Part.Extension.SelectByID2(myRefPlane.name, "PLANE", 0, 0, 0, False, 0, Nothing, 0)
Part.SketchManager.InsertSketch True
Part.ClearSelection2 True
Dim skSegment As Object
Set skSegment = Part.SketchManager.CreateCenterLine(0#, -0.031354, 0#, 0#, 0.04872, 0#)
'Set sketchName = Part.SketchManager.ActiveSketch.name

Debug.Print (Part.SketchManager.ActiveSketch.name)
strSketchName = Part.SketchManager.ActiveSketch.name
Part.SetPickMode
Part.ClearSelection2 True
Part.SketchManager.InsertSketch True
lineAtSketch = skSegment.GetName() + "@" + strSketchName
Debug.Print ("LINE@SKETCH " + lineAtSketch)
boolstatus = Part.Extension.SelectByID2(lineAtSketch, "EXTSKETCHSEGMENT", 0, 0.030480789993285, 0, True, 0, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("前视基准面", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
Set myRefPlane = Part.FeatureManager.InsertRefPlane(2112, 0, 16, 0.5235987755983, 0, 0) ' The Radius.
Part.ClearSelection2 True
End Sub
