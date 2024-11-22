from flask import Flask, request, jsonify

app = Flask(__name__)


# Endpoint for total weight calculation
@app.route('/total-weight', methods=['POST'])
def calculate_total_weight():
    try:
        workouts = request.get_json()
        if not workouts or not isinstance(workouts, list):
            return jsonify({'error': 'No workouts provided or invalid.'}), 400

        for workout in workouts:
            if 'reps' not in workout or 'weight' not in workout:
                return jsonify({'error': 'Invalid workout entry'}), 400

        total_weight = sum(workout['reps'] * workout['weight'] for workout in workouts)
        return jsonify({'total_weight': total_weight})
    except (TypeError, KeyError):
        return jsonify({'error': 'Invalid input data format'}), 400


# Endpoint for weight conversion
@app.route('/convert-weight', methods=['GET'])
def convert_weight():
    try:
        weight = float(request.args.get('weight'))
        to_unit = request.args.get('to_unit')

        if to_unit == 'kg':
            converted_weight = round(weight * 0.453592, 2)
        elif to_unit == 'lbs':
            converted_weight = round(weight * 2.20462, 2)
        else:
            return jsonify({'error': 'Invalid unit specified'}), 400

        return jsonify({'converted_weight': converted_weight})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input data format'}), 400


# Endpoint for strength progress
@app.route('/strength-progress', methods=['GET'])
def strength_progress():
    try:
        current_weight = float(request.args.get('current_weight'))
        initial_weight = float(request.args.get('initial_weight'))
        weight_difference = current_weight - initial_weight
        return jsonify({'weight_difference': weight_difference})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input data format'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
