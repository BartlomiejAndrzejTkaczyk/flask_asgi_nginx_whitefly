from flask import Blueprint

router = Blueprint('loader_io', __name__, url_prefix='')


@router.route('/loaderio-52aa7b4162f947685d0dca51d9e24c8f/', methods=['GET'])
def loader_io():
    return 'loaderio-52aa7b4162f947685d0dca51d9e24c8f'
