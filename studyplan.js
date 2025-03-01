const API_BASE_URL = "http://127.0.0.1:5000"; // Flask Backend URL

export const updateStudyPlan = async (progress) => {
  return fetch(${API_BASE_URL}/update_plan, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ progress }),
  }).then((res) => res.json());
};

export const predictPerformance = async (hours_studied) => {
  return fetch(${API_BASE_URL}/predict_performance, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ hours_studied }),
  }).then((res) => res.json());
};

export const recommendLearning = async (topic) => {
  return fetch(${API_BASE_URL}/recommend_learning, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ topic }),
  }).then((res) => res.json());
};

export const analyzeStudy = async (student_input) => {
  return fetch(${API_BASE_URL}/analyze_study, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ student_input }),
  }).then((res) => res.json());
};
