import { Link } from "react-router-dom";

export default function PostCard({ post }) {
  const preview = post.content.length > 150
    ? post.content.slice(0, 150) + "..."
    : post.content;

  const date = new Date(post.created_at).toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });

  return (
    <div className="post-card">
      <div className="post-card-meta">
        <span className="post-author">✍️ {post.owner.email.split("@")[0]}</span>
        <span className="post-date">{date}</span>
      </div>

      <h2 className="post-title">
        <Link to={`/posts/${post.id}`}>{post.title}</Link>
      </h2>

      <p className="post-preview">{preview}</p>

      <Link to={`/posts/${post.id}`} className="read-more">
        Read more →
      </Link>
    </div>
  );
}