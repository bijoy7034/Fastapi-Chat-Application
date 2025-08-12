import { useState } from "react";
import { useAuthStore } from "../store/authStore";

function Auth() {
  const { loading, error, login } = useAuthStore();

  const [formData, setFormData] = useState({
    username: "",
    password: ""
  });

  const handleOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    login(formData.username, formData.password);
  };

  return (
    <div
      className="container login"
      style={{ width: "500px", padding: "40px" }}
    >
      <b>
        <h3 className="text-center mb-4 text-bold">Login</h3>
      </b>
      {loading && (
        <div className="alert alert-info" role="alert">
          Loading...
        </div>
      )}
      {error && (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Email address</label>
          <input
            name="username" 
            value={formData.username}
            onChange={handleOnChange}
            type="email"
            className="form-control form-control-sm"
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Password</label>
          <input
            name="password" 
            value={formData.password}
            onChange={handleOnChange}
            type="password"
            className="form-control form-control-sm"
            required
          />
        </div>

        <div className="mb-3 form-check">
          <input
            type="checkbox"
            className="form-check-input"
            id="exampleCheck1"
          />
          <label className="form-check-label">Save Login Info</label>
        </div>

        <div className="d-grid gap-2 mb-4 mt-2">
          <button className="btn btn-dark" type="submit">
            Login
          </button>
        </div>
      </form>
    </div>
  );
}

export default Auth;
