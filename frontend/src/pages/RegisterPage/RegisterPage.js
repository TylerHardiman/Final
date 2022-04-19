import React, { useContext } from "react";
import AuthContext from "../../context/AuthContext";
import useCustomForm from "../../hooks/useCustomForm";

const RegisterPage = () => {
  const { registerUser } = useContext(AuthContext);
  const defaultValues = {
    username: "",
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    city: "",
    state: "",
    experiences: "",
    interests: "",
  };
  const [formData, handleInputChange, handleSubmit] = useCustomForm(
    defaultValues,
    registerUser
  );

  return (
    <div className="container">
      <form className="form" onSubmit={handleSubmit}>
        <label>
          Username:{" "}
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleInputChange}
          />
        </label>
        <label>
          First Name:{" "}
          <input
            type="text"
            name="firstName"
            value={formData.firstName}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Last Name:{" "}
          <input
            type="text"
            name="lastName"
            value={formData.lastName}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Email:{" "}
          <input
            type="text"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
          />
        </label>
        <label>
          City:{" "}
          <input
            type="text"
            name="City"
            value={formData.City}
            onChange={handleInputChange}
          />
        </label>
        <label>
          State:{" "}
          <input
            type="text"
            name="State"
            value={formData.State}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Experiences:{" "}
          <input
            type="text"
            name="Experiences"
            value={formData.Experiences}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Interests:{" "}
          <input
            type="text"
            name="Interests"
            value={formData.Interests}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Password:{" "}
          <input
            type="text"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
          />
        </label>
        <p style={{ fontSize: "12px" }}>
          NOTE: Make this an uncommon password with characters, numbers, and
          special characters!
        </p>
        <button>Register!</button>
      </form>
    </div>
  );
};

export default RegisterPage;
