import axios from "axios";

const getToken = () => {
  const token = localStorage.getItem("token");
  return token;
};

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  headers: {
    "Content-Type": "application/json",
    ...(getToken() ? { Authorization: `Token ${getToken()}` } : {}),
  },
  withCredentials: true,
});

const updateToken = () => {
  const token = localStorage.getItem("token");
  if (token) {
    apiClient.defaults.headers.common["Authorization"] = `Token ${token}`;
  } else {
    delete apiClient.defaults.headers.common["Authorization"];
  }
};

updateToken();

export default apiClient;
export { updateToken };
