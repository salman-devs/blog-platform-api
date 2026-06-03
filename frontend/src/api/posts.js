import api from "./axios";

export const getPosts = (page = 1, limit = 10, search = "") =>
  api.get("/posts", { params: { page, limit, search } });

export const getPost = (id) =>
  api.get(`/posts/${id}`);

export const createPost = (title, content) =>
  api.post("/posts", { title, content });

export const updatePost = (id, title, content) =>
  api.put(`/posts/${id}`, { title, content });

export const deletePost = (id) =>
  api.delete(`/posts/${id}`);

export const likePost = (id) =>
  api.post(`/likes/${id}`);

export const unlikePost = (id) =>
  api.delete(`/likes/${id}`);

export const bookmarkPost = (id) =>
  api.post(`/bookmarks/${id}`);

export const unbookmarkPost = (id) =>
  api.delete(`/bookmarks/${id}`);

export const getBookmarks = () =>
  api.get("/bookmarks");