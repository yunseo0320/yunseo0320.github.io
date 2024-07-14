from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 origin에서 CORS 허용 설정

# 컬러 매핑
color_mapping = {
    1: ('Yellow', 'Yellow'),
    2: ('Turquoise', 'Blue'),
    3: ('Pink', 'Pink'),
    4: ('Yellow', 'Green'),
    5: ('Green', 'Green'),
    6: ('Pink', 'Pink'),
    7: ('Turquoise', 'Blue'),
    8: ('Violet', 'Violet'),
    9: ('Orange', 'Green'),
    10: ('Orange', 'Green'),
    11: ('Magenta', 'Magenta'),
    12: ('Violet', 'Red'),
    13: ('Magenta', 'Violet'),
    14: ('Turquoise', 'Turquoise'),
    15: ('Green', 'Green'),
    16: ('Green', 'Violet'),
    17: ('Pink', 'Blue'),
    18: ('Magenta', 'Pink'),
    19: ('Red', 'Orange'),
    20: ('Brown', 'Brown'),
    21: ('Orange', 'Yellow'),
    22: ('Magenta', 'Red'),
    23: ('Violet', 'Blue'),
    24: ('Red', 'Green'),
    25: ('Turquoise', 'Yellow'),
    26: ('Brown', 'Green'),
    27: ('Orange', 'Orange'),
    28: ('Yellow', 'Turquoise'),
    29: ('Turquoise', 'Magenta'),
    30: ('Turquoise', 'Turquoise'),
    31: ('Green', 'Green'),
    32: ('Blue', 'Green'),
    33: ('Pink', 'Pink'),
    34: ('Turquoise', 'Turquoise'),
    35: ('Violet', 'Green'),
    36: ('Violet', 'Violet'),
    37: ('Pink', 'Red'),
    38: ('Yellow', 'Orange'),
    39: ('Green', 'Yellow'),
    40: ('Turquoise', 'Green'),
    41: ('Blue', 'Blue'),
    42: ('Violet', 'Blue'),
    43: ('Brown', 'Brown'),
    44: ('Pink', 'Magenta'),
    45: ('Cream', 'Cream'),
    46: ('Orange', 'Pink'),
    47: ('Yellow', 'Cream'),
    48: ('Violet', 'Pink'),
    49: ('Violet', 'Violet'),
    50: ('Yellow', 'Cream'),
    51: ('Cream', 'Violet'),
    52: ('Cream', 'Red'),
    53: ('Brown', 'Red'),
    54: ('Brown', 'Turquoise'),
    55: ('Pink', 'Red'),
    56: ('Orange', 'Magenta'),
    57: ('Brown', 'Green'),
    58: ('Brown', 'Cream'),
    59: ('Magenta', 'Magenta')
}

# 색상 매핑
color_name_mapping = {
    'Yellow': '#FFFF00',
    'Turquoise': '#40E0D0',
    'Pink': '#FFC0CB',
    'Green': '#008000',
    'Violet': '#EE82EE',
    'Blue': '#0000FF',
    'Red': '#FF0000',
    'Orange': '#FFA500',
    'Brown': '#A52A2A',
    'Cream': '#FFFDD0',
    'Magenta': '#FF00FF'
}

# 사용자 입력 데이터 저장소
user_data = []

@app.route('/')
def index():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Color Calculation</title>
            <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
            <style>
                .color-box {
                    display: inline-block;
                    width: 100px;
                    height: 100px;
                    margin: 10px;
                    text-align: center;
                    line-height: 100px;
                    color: #fff;
                    font-weight: bold;
                }
                .results-table {
                    border-collapse: collapse;
                    width: 100%;
                }
                .results-table th, .results-table td {
                    border: 1px solid #ddd;
                    padding: 8px;
                }
                .results-table th {
                    background-color: #f2f2f2;
                    text-align: left;
                }
                .color-name-box {
                    display: inline-block;
                    width: 80px;
                    height: 30px;
                    line-height: 30px;
                    margin: 0 5px;
                    color: #fff;
                    text-align: center;
                    border-radius: 4px;
                }
            </style>
            <script>
                function calculateColors() {
                    var birthdate = document.getElementById('birthdate').value;

                    axios.post('/calculate', { birthdate: birthdate })
                        .then(function (response) {
                            var data = response.data;
                            var resultElement = document.getElementById('result');
                            resultElement.innerHTML = `
                                <h2>생년월일에 따른 컬러 결과</h2>
                                <p>첫 번째 컬러:</p>
                                <div>
                                    <div class="color-box" style="background-color: ${data.first_color_color_1};">
                                        ${data.first_color_name_1}
                                    </div>
                                    <div class="color-box" style="background-color: ${data.first_color_color_2};">
                                        ${data.first_color_name_2}
                                    </div>
                                </div>
                                <p>두 번째 컬러:</p>
                                <div>
                                    <div class="color-box" style="background-color: ${data.second_color_color_1};">
                                        ${data.second_color_name_1}
                                    </div>
                                    <div class="color-box" style="background-color: ${data.second_color_color_2};">
                                        ${data.second_color_name_2}
                                    </div>
                                </div>
                                <p>세 번째 컬러:</p>
                                <div>
                                    <div class="color-box" style="background-color: ${data.third_color_color_1};">
                                        ${data.third_color_name_1}
                                    </div>
                                    <div class="color-box" style="background-color: ${data.third_color_color_2};">
                                        ${data.third_color_name_2}
                                    </div>
                                </div>
                            `;
                        })
                        .catch(function (error) {
                            console.error('Error:', error);
                        });
                }

                function showAllResults() {
                    axios.get('/all_results')
                        .then(function (response) {
                            var data = response.data;
                            var allResultsElement = document.getElementById('allResults');
                            var tableHtml = '<table class="results-table"><tr><th>생년월일</th><th>첫 번째 컬러</th><th>두 번째 컬러</th><th>세 번째 컬러</th></tr>';
                            data.forEach(function(item) {
                                tableHtml += '<tr>';
                                tableHtml += '<td>' + item.birthdate + '</td>';
                                tableHtml += '<td>' +
                                    '<div class="color-name-box" style="background-color: ' + item.first_color_color_1 + ';">' + item.first_color_name_1 + '</div>' +
                                    '<div class="color-name-box" style="background-color: ' + item.first_color_color_2 + ';">' + item.first_color_name_2 + '</div>' +
                                    '</td>';
                                tableHtml += '<td>' +
                                    '<div class="color-name-box" style="background-color: ' + item.second_color_color_1 + ';">' + item.second_color_name_1 + '</div>' +
                                    '<div class="color-name-box" style="background-color: ' + item.second_color_color_2 + ';">' + item.second_color_name_2 + '</div>' +
                                    '</td>';
                                tableHtml += '<td>' +
                                    '<div class="color-name-box" style="background-color: ' + item.third_color_color_1 + ';">' + item.third_color_name_1 + '</div>' +
                                    '<div class="color-name-box" style="background-color: ' + item.third_color_color_2 + ';">' + item.third_color_name_2 + '</div>' +
                                    '</td>';
                                tableHtml += '</tr>';
                            });
                            tableHtml += '</table>';
                            allResultsElement.innerHTML = tableHtml;
                        })
                        .catch(function (error) {
                            console.error('Error:', error);
                        });
                }

                function clearResults() {
                    axios.post('/clear_results')
                        .then(function () {
                            document.getElementById('allResults').innerHTML = '';
                            alert('결과가 초기화되었습니다.');
                        })
                        .catch(function (error) {
                            console.error('Error:', error);
                        });
                }
            </script>
        </head>
        <body>
            <div>
                <label for="birthdate">생년월일(YYYYMMDD):</label>
                <input type="text" id="birthdate" name="birthdate" pattern="[0-9]{8}" title="8자리 숫자를 입력하세요 (예: 20230101)" required>
                <button type="button" onclick="calculateColors()">계산하기</button>
                <button type="button" onclick="showAllResults()">전체결과</button>
                <button type="button" onclick="clearResults()">초기화</button>
            </div>

            <div id="result"></div>
            <div id="allResults"></div>
        </body>
        </html>
    """)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    birthdate = data['birthdate']

    # 두 번째 컬러 계산: 8자리 생년월일의 각 자릿수를 모두 더한 값
    second_color = sum(int(digit) for digit in birthdate)

    # 세 번째 컬러 계산: 두 번째 컬러의 각 자릿수를 모두 더한 값
    second_color_str = str(second_color)  # 숫자를 문자열로 변환하여 각 자릿수 더하기
    third_color = sum(int(digit) for digit in second_color_str)

    # 첫 번째 컬러 계산: 8자리 생년월일에서 마지막 두 자리 숫자
    first_color = int(birthdate[-2:])

    # 컬러에 매칭되는 값 가져오기
    first_color_name_1, first_color_name_2 = color_mapping[first_color]
    second_color_name_1, second_color_name_2 = color_mapping[second_color]
    third_color_name_1, third_color_name_2 = color_mapping[third_color]

    # 색상 매칭 가져오기
    first_color_color_1 = color_name_mapping[first_color_name_1]
    first_color_color_2 = color_name_mapping[first_color_name_2]
    second_color_color_1 = color_name_mapping[second_color_name_1]
    second_color_color_2 = color_name_mapping[second_color_name_2]
    third_color_color_1 = color_name_mapping[third_color_name_1]
    third_color_color_2 = color_name_mapping[third_color_name_2]

    # 사용자 데이터를 저장소에 추가
    user_data.append({
        'birthdate': birthdate,
        'first_color_name_1': first_color_name_1,
        'first_color_name_2': first_color_name_2,
        'second_color_name_1': second_color_name_1,
        'second_color_name_2': second_color_name_2,
        'third_color_name_1': third_color_name_1,
        'third_color_name_2': third_color_name_2,
        'first_color_color_1': first_color_color_1,
        'first_color_color_2': first_color_color_2,
        'second_color_color_1': second_color_color_1,
        'second_color_color_2': second_color_color_2,
        'third_color_color_1': third_color_color_1,
        'third_color_color_2': third_color_color_2
    })

    return jsonify({
        'first_color_name_1': first_color_name_1,
        'first_color_name_2': first_color_name_2,
        'second_color_name_1': second_color_name_1,
        'second_color_name_2': second_color_name_2,
        'third_color_name_1': third_color_name_1,
        'third_color_name_2': third_color_name_2,
        'first_color_color_1': first_color_color_1,
        'first_color_color_2': first_color_color_2,
        'second_color_color_1': second_color_color_1,
        'second_color_color_2': second_color_color_2,
        'third_color_color_1': third_color_color_1,
        'third_color_color_2': third_color_color_2
    })

@app.route('/all_results', methods=['GET'])
def all_results():
    return jsonify(user_data)

@app.route('/clear_results', methods=['POST'])
def clear_results():
    user_data.clear()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
