import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { getPosts, getBookmarks } from "../api/posts";
import { useAuth } from "../context/AuthContext";
import PostCard from "../components/PostCard";

export default function Profile() {
  const { user, logoutUser } = useAuth();
  const navigate = useNavigate();

  const [myPosts, setMyPosts] = useState([]);
  const [bookmarks, setBookmarks] = useState([]);
  const [activeTab, setActiveTab] = useState("posts");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!user) navigate("/login");
  }, [user]);

  useEffect(() => {
    if (!user) return;
    setLoading(true);

    Promise.all([
      getPosts(1, 50, "", user.id),
      getBookmarks(),
    ])
      .then(([postsRes, bookmarksRes]) => {
        setMyPosts(postsRes.data.data);
        setBookmarks(bookmarksRes.data);
      })
      .catch(() => setError("Failed to load profile data."))
      .finally(() => setLoading(false));
  }, [user]);

  const handleLogout = () => {
    logoutUser();
    navigate("/login");
  };

  if (!user) return null;

  return (
    <div className="page">
      <div className="profile-header">
        <div className="profile-avatar">
          {user.email[0].toUpperCase()}
        </div>
        <div className="profile-info">
          <h1>{user.email.split("@")[0]}</h1>
          <p>{user.email}</p>
        </div>
        <button onClick={handleLogout} className="btn-logout">
          Logout
        </button>
      </div>

      <div className="profile-stats">
        <div className="stat">
          <span className="stat-number">{myPosts.length}</span>
          <span className="stat-label">Posts</span>
        </div>
        <div className="stat">
          <span className="stat-number">{bookmarks.length}</span>
          <span className="stat-label">Bookmarks</span>
        </div>
      </div>

      <div className="tabs">
        <button
          className={`tab ${activeTab === "posts" ? "active" : ""}`}
          onClick={() => setActiveTab("posts")}
        >
          My Posts
        </button>
        <button
          className={`tab ${activeTab === "bookmarks" ? "active" : ""}`}
          onClick={() => setActiveTab("bookmarks")}
        >
          Bookmarks
        </button>
      </div>

      {error && <p className="status-msg error">{error}</p>}
      {loading && <p className="status-msg">Loading...</p>}

      {!loading && activeTab === "posts" && (
        <div className="posts-grid">
          {myPosts.length === 0 ? (
            <p className="status-msg">You haven't written any posts yet.</p>
          ) : (
            myPosts.map((post) => <PostCard key={post.id} post={post} />)
          )}
        </div>
      )}

      {!loading && activeTab === "bookmarks" && (
        <div className="posts-grid">
          {bookmarks.length === 0 ? (
            <p className="status-msg">No bookmarks yet.</p>
          ) : (
            bookmarks.map((post) => <PostCard key={post.id} post={post} />)
          )}
        </div>
      )}
    </div>
  );
}