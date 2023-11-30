// graph.js
document.addEventListener("DOMContentLoaded", function() {
    // Retrieve data from the HTML template
    var testDates = JSON.parse("{{ test_dates|safe }}");
    var testMarks = JSON.parse("{{ test_marks|safe }}");

    var interviewDates = JSON.parse("{{ interview_dates|safe }}");
    var interviewPerformance = JSON.parse("{{ interview_performance|safe }}");

    var attendanceDates = JSON.parse("{{ attendance_dates|safe }}");
    var attendancePresent = JSON.parse("{{ attendance_present|safe }}");

    // Create and render the Test Marks chart
    var testCtx = document.getElementById("testChart").getContext("2d");
    var testChart = new Chart(testCtx, {
        type: 'bar',
        data: {
            labels: testDates,
            datasets: [{
                label: 'Test Marks',
                data: testMarks,
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });

    // Create and render the Interview Performance chart
    var interviewCtx = document.getElementById("interviewChart").getContext("2d");
    var interviewChart = new Chart(interviewCtx, {
        type: 'line',
        data: {
            labels: interviewDates,
            datasets: [{
                label: 'Interview Performance',
                data: interviewPerformance,
                fill: false,
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });

    // Create and render the Attendance chart
    var attendanceCtx = document.getElementById("attendanceChart").getContext("2d");
    var attendanceChart = new Chart(attendanceCtx, {
        type: 'bar',
        data: {
            labels: attendanceDates,
            datasets: [{
                label: 'Attendance',
                data: attendancePresent,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 1
                }
            }
        }
    });
});
