import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { api } from '../services/api';

export default function DocumentDetail() {
  const { docId } = useParams();
  const navigate = useNavigate();
  const [document, setDocument] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDoc = async () => {
      setLoading(true);
      try {
        const data = await api.getDocument(docId);
        setDocument(data);
      } catch (err) {
        setError(`Failed to load document: ${err.message}`);
      } finally {
        setLoading(false);
      }
    };
    fetchDoc();
  }, [docId]);

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen gap-4 bg-gray-50">
        <div className="w-12 h-12 border-4 border-blue-500 rounded-full border-t-transparent animate-spin"></div>
        <p className="text-gray-500 font-medium anim-pulse">Loading document contents...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen gap-6 px-4 text-center bg-gray-50">
        <div className="p-4 bg-red-50 rounded-full">
          <svg className="w-12 h-12 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
        <div className="max-w-md">
          <h2 className="mb-2 text-2xl font-bold text-gray-900">Something went wrong</h2>
          <p className="text-gray-600">{error}</p>
        </div>
        <button 
          onClick={() => navigate('/')}
          className="px-6 py-2.5 bg-white border border-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-50 transition-colors shadow-sm"
        >
          Back to Search
        </button>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-white">
      <header className="sticky top-0 z-10 bg-white/80 backdrop-blur-md border-b border-gray-100">
        <div className="max-w-5xl px-6 py-4 mx-auto md:px-10">
          <button 
            className="flex items-center gap-2 mb-4 text-sm font-semibold text-blue-600 transition-transform hover:-translate-x-1" 
            onClick={() => navigate(-1)}
          >
            <span>&larr;</span> Back to Results
          </button>
          <div className="flex flex-col gap-1">
            <h1 className="text-3xl font-extrabold tracking-tight text-gray-900 md:text-4xl">Document {docId}</h1>
            <p className="text-sm font-medium text-gray-400 font-mono tracking-wider uppercase">{document?.filename}</p>
          </div>
        </div>
      </header>

      <main className="max-w-5xl px-6 py-12 mx-auto md:px-10">
        <article className="prose prose-blue max-w-none">
          <div className="p-8 bg-gray-50 border border-gray-100 rounded-3xl md:p-12">
            <pre className="whitespace-pre-wrap font-sans text-lg leading-relaxed text-gray-800">
              {document?.content}
            </pre>
          </div>
        </article>
      </main>
      
      <footer className="px-6 py-12 bg-gray-50 border-t border-gray-100 md:px-10">
        <div className="flex flex-col items-center justify-center max-w-5xl mx-auto gap-6 text-center">
          <div className="flex flex-col gap-2">
            <h3 className="text-lg font-bold text-gray-900">Finished reading?</h3>
            <p className="text-gray-500">Go back and explore more documents in the system.</p>
          </div>
          <button 
            className="px-8 py-3 bg-blue-600 text-white font-bold rounded-2xl shadow-lg shadow-blue-500/25 hover:bg-blue-700 hover:shadow-blue-500/40 hover:-translate-y-0.5 active:translate-y-0 transition-all font-sans"
            onClick={() => navigate('/')}
          >
            Start New Search
          </button>
        </div>
      </footer>
    </div>
  );
}
