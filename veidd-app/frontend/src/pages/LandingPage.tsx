import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage: React.FC = () => {
  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold text-gray-900 mb-6">
        Welcome to VEIDD
      </h1>
      <p className="text-xl text-gray-600 mb-8">
        Visual recognition, Evaluation, Intactness, Difficulty, Decisioning for E-waste Processing
      </p>
      <div className="space-x-4">
        <Link
          to="/register"
          className="bg-blue-600 text-white px-6 py-3 rounded-md text-lg font-medium hover:bg-blue-700"
        >
          Get Started
        </Link>
        <Link
          to="/login"
          className="bg-gray-200 text-gray-800 px-6 py-3 rounded-md text-lg font-medium hover:bg-gray-300"
        >
          Login
        </Link>
      </div>
    </div>
  );
};

export default LandingPage; 