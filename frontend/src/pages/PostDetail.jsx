import { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { getPost, likePost, unlikePost, bookmarkPost, unbookmarkPost, deletePost } from "../api/posts";
import { getComments, createComment, deleteComment } from "../api/comments";
import { useAuth } from "../context/AuthContext";

export default function PostDetail() {
  const { id } = useParams();
  const { user } = useAuth();
  const navigate = useNavigate();

  const [post, setPost] = useState(null);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState("");
  const [liked, setLiked] = useState(false);
  const [bookmarked, setBookmarked] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [commentError, setCommentError] = useState("");

  useEffect(() => {
    Promise.all([getPost(id), getComments(id)])
      .then(([postRes, commentsRes]) => {
        setPost(postRes.data);
        setComments(commentsRes.data);
      })
      .catch(() => setError("Failed to load post."))
      .finally(() => setLoading(false));
  }, [id]);

  const handleLike = async () => {
    if (!user) return navigate("/login");
    try {
      if (liked) {
        await unlikePost(id);
        setLiked(false);
      } else {
        await likePost(id);
        setLiked(true);
      }
    } catch {
      alert("Could not update like.");
    }
  };

  const handleBookmark = async () => {
    if (!user) return navigate("/login");
    try {
      if (bookmarked) {
        await unbookmarkPost(id);
        setBookmarked(false);
      } else {
        await bookmarkPost(id);
        setBookmarked(true);
      }
    } catch {
      alert("Could not update bookmark.");
    }
  };

  const handleComment = async (e) => {
    e.preventDefault();
    if (!user) return navigate("/login");
    if (!newComment.trim()) return;
    try {
      const res = await createComment(id, newComment);
      setComments((prev) => [res.data, ...prev]);
      setNewComment("");
      setCommentError("");
    } catch {
      setCommentError("Failed to post comment.");
    }
  };

  const handleDeleteComment = async (commentId) => {
    try {
      await deleteComment(commentId);
      setComments((prev) => prev.filter((c) => c.id !== commentId));
    } catch {
      alert("Could not delete comment.");
    }
  };

  const handleDeletePost = async () => {
    if (!window.confirm("Delete this post?")) return;
    try {
      await deletePost(id);
      navigate("/");
    } catch {
      alert("Could not delete post.");
    }
  };

  if (loading) return <p className="status-msg">Loading...</p>;
  if (error) return <p className="status-msg error">{error}</p>;
  if (!post) return null;

  const date = new Date(post.created_at).toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });

  const isOwner = user && user.id === post.owner_id;

  return (
    <div className="page post-detail">
      <div className="post-detail-header">
        <h1>{post.title}</h1>
        <div className="post-detail-meta">
          <span>✍️ {post.owner.email.split("@")[0]}</span>
          <span>{date}</span>
        </div>
      </div>

      <div className="post-detail-body">
        <p>{post.content}</p>
      </div>

      <div className="post-actions">
        <button
          onClick={handleLike}
          className={`btn-action ${liked ? "active" : ""}`}
        >
          {liked ? "❤️ Liked" : "🤍 Like"}
        </button>
        <button
          onClick={handleBookmark}
          className={`btn-action ${bookmarked ? "active" : ""}`}
        >
          {bookmarked ? "🔖 Saved" : "📄 Bookmark"}
        </button>

        {isOwner && (
          <div className="owner-actions">
            <Link to={`/edit/${post.id}`} className="btn-action">
              ✏️ Edit
            </Link>
            <button onClick={handleDeletePost} className="btn-action danger">
              🗑️ Delete
            </button>
          </div>
        )}
      </div>

      <div className="comments-section">
        <h2>Comments ({comments.length})</h2>

        {user ? (
          <form onSubmit={handleComment} className="comment-form">
            <textarea
              placeholder="Write a comment..."
              value={newComment}
              onChange={(e) => setNewComment(e.target.value)}
              rows={3}
            />
            {commentError && <p className="error">{commentError}</p>}
            <button type="submit">Post Comment</button>
          </form>
        ) : (
          <p>
            <Link to="/login">Login</Link> to leave a comment.
          </p>
        )}

        <div className="comments-list">
          {comments.length === 0 && (
            <p className="status-msg">No comments yet. Be the first!</p>
          )}
          {comments.map((c) => (
            <div key={c.id} className="comment-card">
              <div className="comment-meta">
                <span>👤 {c.user?.email?.split("@")[0] ?? "User"}</span>
                <span>
                  {new Date(c.created_at).toLocaleDateString("en-US", {
                    month: "short",
                    day: "numeric",
                  })}
                </span>
              </div>
              <p>{c.content}</p>
              {user && user.id === c.user_id && (
                <button
                  onClick={() => handleDeleteComment(c.id)}
                  className="btn-delete-comment"
                >
                  Delete
                </button>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}