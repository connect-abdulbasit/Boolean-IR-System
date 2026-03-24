import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function Results({ documents, loading }) {
  const navigate = useNavigate();

  if (loading) return null;
  if (!documents || documents.length === 0) return null;

  const handleDocClick = (docId) => {
    navigate(`/document/${docId}`);
  };

  return (
    <div className="grid grid-cols-1 gap-6 max-w-3xl">
      {documents.map((docId) => (
        <div 
          key={docId} 
          className="group relative p-6 bg-white border border-gray-100 rounded-2xl shadow-sm hover:shadow-md hover:border-blue-100 transition-all cursor-pointer" 
          onClick={() => handleDocClick(docId)}
        >
          <div className="flex flex-col gap-2">
            <h3 className="text-xl font-semibold text-gray-900 group-hover:text-blue-600 transition-colors">
              Document {docId}
            </h3>
            <div className="flex items-center gap-2 text-sm font-medium text-gray-500">
              <span className="px-2 py-0.5 bg-gray-100 rounded text-xs">TEXT</span>
              <span>speech_{docId}.txt</span>
            </div>
            <p className="mt-2 text-sm leading-relaxed text-gray-600 line-clamp-2">
              Deep-dive into the contents of document {docId}. Click to read the full speech and analysis.
            </p>
          </div>
          <div className="absolute right-6 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all text-blue-500">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" />
            </svg>
          </div>
        </div>
      ))}
    </div>
  );
}
