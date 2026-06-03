import api from "./axios";

export const getComments = (postId) =>
  api.get(`/comments/post/${postId}`);

export const createComment = (postId, content) =>
  api.post(`/comments/${postId}`, { content });

export const deleteComment = (commentId) =>
  api.delete(`/comments/${commentId}`);