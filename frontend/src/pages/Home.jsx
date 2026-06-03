import { useState, useEffect } from "react";
import { getPosts } from "../api/posts";
import PostCard from "../components/PostCard";

export default function Home() {
  const [posts, setPosts] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState("");
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const limit = 10;

  useEffect(() => {
    setLoading(true);
    getPosts(page, limit, query)
      .then((res) => {
        setPosts(res.data.data);
        setTotal(res.data.total);
      })
      .catch(() => setError("Failed to load posts."))
      .finally(() => setLoading(false));
  }, [page, query]);

  const handleSearch = (e) => {
    e.preventDefault();
    setPage(1);
    setQuery(search);
  };

  const totalPages = Math.ceil(total / limit);

  return (
    <div className="page">
      <div className="home-header">
        <h1>Latest Posts</h1>
        <form onSubmit={handleSearch} className="search-form">
          <input
            type="text"
            placeholder="Search posts..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
          <button type="submit">Search</button>
        </form>
      </div>

      {loading && <p className="status-msg">Loading...</p>}
      {error && <p className="status-msg error">{error}</p>}

      {!loading && posts.length === 0 && (
        <p className="status-msg">No posts found.</p>
      )}

      <div className="posts-grid">
        {posts.map((post) => (
          <PostCard key={post.id} post={post} />
        ))}
      </div>

      {totalPages > 1 && (
        <div className="pagination">
          <button
            onClick={() => setPage((p) => p - 1)}
            disabled={page === 1}
          >
            ← Prev
          </button>
          <span>Page {page} of {totalPages}</span>
          <button
            onClick={() => setPage((p) => p + 1)}
            disabled={page === totalPages}
          >
            Next →
          </button>
        </div>
      )}
    </div>
  );
}