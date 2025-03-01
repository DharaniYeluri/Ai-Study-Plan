const API_BASE_URL = "http://127.0.0.1:5000"; // Backend URL

export const getStudyPlan = async (userId) => {
  try {
    const response = await fetch(${API_BASE_URL}/studyplan?userId=${userId});
    if (!response.ok) {
      throw new Error("Failed to fetch study plan");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching study plan:", error);
    return null;
  }
};
