/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';

export default function App() {
  return (
    <div className="min-h-screen bg-[#F8FAFC] flex items-center justify-center p-6 font-sans text-slate-800">
      <div className="max-w-2xl bg-white rounded-xl shadow-sm p-8 border border-slate-200">
        <div className="flex items-center justify-center w-16 h-16 bg-blue-500 text-white rounded-lg mb-6 mx-auto shadow-md">
          <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
          </svg>
        </div>
        <h1 className="text-3xl font-bold tracking-tight text-center text-slate-800 mb-4">
          Professional Telegram Bot Tayyor
        </h1>
        <p className="text-slate-500 mb-6 text-center text-lg leading-relaxed">
          Telegram botining barcha backend (Python, Aiogram 3, PostgreSQL, va Gemini API) fayllari muvaffaqiyatli yaratildi.
        </p>
        
        <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden mb-6">
          <div className="px-6 py-4 border-b border-slate-100 bg-slate-50">
            <h2 className="font-bold text-slate-700">Loyihani ishga tushirish qadamlari:</h2>
          </div>
          <ul className="divide-y divide-slate-100 text-sm">
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-center gap-4">
              <div className="w-6 h-6 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">1</div>
              <div>Loyiha fayllarini (ZIP yoki GitHub orqali) yuklab oling.</div>
            </li>
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-center gap-4">
              <div className="w-6 h-6 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">2</div>
              <div>Python 3.12 o'rnatilganligiga ishonch hosil qiling.</div>
            </li>
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-center gap-4">
               <div className="w-6 h-6 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">3</div>
               <div>Kutubxonalarni o'rnating: <code className="font-mono font-bold bg-blue-50 text-blue-700 px-2 py-0.5 rounded border border-blue-100 ml-1">pip install -r requirements.txt</code></div>
            </li>
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-start gap-4">
               <div className="w-6 h-6 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs mt-0.5">4</div>
               <div className="leading-relaxed"><code className="font-mono bg-slate-100 text-slate-600 px-2 py-0.5 rounded mr-1">.env</code> fayl yarating (namuna sifatida <code className="font-mono bg-slate-100 text-slate-600 px-2 py-0.5 rounded mr-1">.env.example</code> dan foydalaning) va ma'lumotlarni kiritib chiqing.</div>
            </li>
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-center gap-4">
               <div className="w-6 h-6 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">5</div>
               <div>Botni ishga tushiring: <code className="font-mono font-bold bg-blue-50 text-blue-700 px-2 py-0.5 rounded border border-blue-100 ml-1">python main.py</code></div>
            </li>
          </ul>
        </div>
        
        <div className="text-center text-[10px] text-slate-400 uppercase font-bold tracking-widest mt-6">
          Ushbu sahifa faqatgina loyihaning frontend qismi.<br/>Bot server tomonida ishlashi kerak.
        </div>
      </div>
    </div>
  );
}

