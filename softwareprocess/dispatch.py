from operations.adjust import Adjust
from operations.predict import Predict


def dispatch(values=None):

    # Validate parm
    if values is None:
        return {'error': 'parameter is missing'}
    if not(isinstance(values, dict)):
        return {'error': 'parameter is not a dictionary'}
    if not('op' in values):
        values['error'] = 'no op  is specified'
        return values

    # Perform designated function
    if values['op'] == 'adjust':
        validated = Adjust.validate_parameter(values)
        if validated is True:
            adj = Adjust(values)
            return adj.perform()
        else:
            values['error'] = validated
        return values    # <-------------- replace this with your implementation
    elif values['op'] == 'predict':
        validated = Predict.validate_parameter(values)
        if validated is True:
            predict = Predict(values)
            return predict.perform()
        else:
            values['error'] = validated
        return values    # This calculation is stubbed out
    elif values['op'] == 'correct':
        return values    # This calculation is stubbed out
    elif values['op'] == 'locate':
        return values    # This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values
