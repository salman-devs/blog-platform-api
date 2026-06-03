import api from "./axios";

export const signup = (email, password) =>
  api.post("/auth/signup", { email, password });

export const login = (email, password) =>
  api.post("/auth/login", { email, password });
