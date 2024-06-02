from flask import render_template, Blueprint, jsonify

router = Blueprint('hello_world', __name__, url_prefix='', template_folder='templates')


@router.route('/')
async def hello_world():
    return render_template('hello_world.html')


@router.route('/json')
async def hello_world():
    return jsonify({'hello_world :)': 200})
