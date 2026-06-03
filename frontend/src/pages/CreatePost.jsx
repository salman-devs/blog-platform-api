import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { createPost, updatePost, getPost } from "../api/posts";
import { useAuth } from "../context/AuthContext";

export default function CreatePost() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const { id } = useParams();

  const isEditing = Boolean(id);

  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!user) navigate("/login");
  }, [user]);

  useEffect(() => {
    if (isEditing) {
      getPost(id)
        .then((res) => {
          setTitle(res.data.title);
          setContent(res.data.content);
        })
        .catch(() => setError("Failed to load post."));
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (!title.trim() || !content.trim()) {
      setError("Title and content are required.");
      return;
    }

    setLoading(true);
    try {
      if (isEditing) {
        await updatePost(id, title, content);
        navigate(`/posts/${id}`);
      } else {
        const res = await createPost(title, content);
        navigate(`/posts/${res.data.id}`);
      }
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page form-page">
      <h1>{isEditing ? "Edit Post" : "Write a New Post"}</h1>

      {error && <p className="error">{error}</p>}

      <form onSubmit={handleSubmit} className="post-form">
        <div className="form-group">
          <label>Title</label>
          <input
            type="text"
            placeholder="Give your post a title..."
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            maxLength={255}
          />
        </div>

        <div className="form-group">
          <label>Content</label>
          <textarea
            placeholder="Write your post here..."
            value={content}
            onChange={(e) => setContent(e.target.value)}
            rows={12}
            maxLength={5000}
          />
          <small>{content.length} / 5000</small>
        </div>

        <button type="submit" className="btn-primary" disabled={loading}>
          {loading ? "Saving..." : isEditing ? "Update Post" : "Publish Post"}
        </button>
      </form>
    </div>
  );
}