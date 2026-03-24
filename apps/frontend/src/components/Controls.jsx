import React, { useState } from 'react';
import { api } from '../services/api';
import '../styles/Controls.css';

export default function Controls({ onBuildSuccess }) {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleBuildIndexes = async () => {
    setLoading(true);
    setMessage('');
    setError('');

    try {
      const response = await api.buildIndexes();
      setMessage(response.message || 'Indexes built successfully!');
      onBuildSuccess?.();
    } catch (err) {
      setError(`Failed to build indexes: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="controls">
      <button
        onClick={handleBuildIndexes}
        disabled={loading}
        className="build-button"
      >
        {loading ? 'Building...' : 'Build Indexes'}
      </button>
      
      {message && <div className="success-message">{message}</div>}
      {error && <div className="error-message">{error}</div>}
    </div>
  );
}
