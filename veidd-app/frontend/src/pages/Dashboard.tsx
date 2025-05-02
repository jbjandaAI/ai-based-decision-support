import React from 'react';

const Dashboard: React.FC = () => {
  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold text-gray-800 mb-2">Processing History</h2>
          <p className="text-gray-600">View your recent e-waste processing records</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold text-gray-800 mb-2">New Processing</h2>
          <p className="text-gray-600">Start a new e-waste processing session</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold text-gray-800 mb-2">Reports</h2>
          <p className="text-gray-600">View processing reports and analytics</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard; 