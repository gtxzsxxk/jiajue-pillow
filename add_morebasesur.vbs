' ******************************************************************************
' C:\Users\hanyuan\AppData\Local\Temp\swx15336\Macro1.swb - macro recorded on 05/09/23 by hanyuan
' ******************************************************************************
Dim swApp As Object

Dim Part As Object
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
Dim myRefPlane As Object

Sub main()

Set swApp = Application.SldWorks

Set Part = swApp.ActiveDoc
Dim myModelView As Object
Set myModelView = Part.ActiveView
myModelView.FrameState = swWindowState_e.swWindowMaximized

Dim fname
fname = InputBox("Enter your name:")
MsgBox ("Your name is " & fname)

boolstatus = Part.Extension.SelectByID2("Line1@草图28", "EXTSKETCHSEGMENT", 0, 3.90371190197243E-02, 0, True, 0, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("前视基准面", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
Set myRefPlane = Part.FeatureManager.InsertRefPlane(2112, 0, 16, 0.26179938779915, 0, 0)
Part.ClearSelection2 True

boolstatus = Part.Extension.SelectByID2("Line1@草图28", "EXTSKETCHSEGMENT", 0, 3.90371190197243E-02, 0, True, 0, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("前视基准面", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
Set myRefPlane = Part.FeatureManager.InsertRefPlane(2112, 0, 16, 0.26179938779915 * 2, 0, 0)
Part.ClearSelection2 True

boolstatus = Part.Extension.SelectByID2("Line1@草图28", "EXTSKETCHSEGMENT", 0, 3.90371190197243E-02, 0, True, 0, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("前视基准面", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
Set myRefPlane = Part.FeatureManager.InsertRefPlane(2112, 0, 16, 0.26179938779915 * 3, 0, 0)
Part.ClearSelection2 True

boolstatus = Part.Extension.SelectByID2("Line1@草图28", "EXTSKETCHSEGMENT", 0, 3.90371190197243E-02, 0, True, 0, Nothing, 0)
boolstatus = Part.Extension.SelectByID2("前视基准面", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
Set myRefPlane = Part.FeatureManager.InsertRefPlane(2112, 0, 16, 0.26179938779915 * 4, 0, 0)
Part.ClearSelection2 True

End Sub
