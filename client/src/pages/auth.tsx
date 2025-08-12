function Auth() {
  return (
    <div
      className="container login"
      style={{ width: "500px", padding: "40px" }}
    >
      <b>
        <h3 className="text-center mb-4 text-bold">Login</h3>
      </b>

      {/* {error && (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      )} */}

      <form>
        <div className="mb-3">
          <label className="form-label">Email address</label>
          <input type="email" className="form-control form-control-sm" required />
        </div>

        <div className="mb-3">
          <label className="form-label">Password</label>
          <input type="password" className="form-control form-control-sm" required />
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
