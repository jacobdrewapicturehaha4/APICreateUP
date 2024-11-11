#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design=adsk.fusion.Design.cast(app.activeProduct)
        pName = 'Width'
        pUnit = 'mm'
        pComments = "This is the extrusion width!"
        pExpression = 5.0
        pExpressionReal = adsk.core.ValueInput.createByReal(pExpression)
        design.userParameters.add(pName,pExpressionReal,pUnit,pComments)


        ui.messageBox('Check The Parameters.')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
