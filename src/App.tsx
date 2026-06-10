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
          Vercel + Telegram Bot Tayyor
        </h1>
        <p className="text-slate-500 mb-6 text-center text-lg leading-relaxed">
          Telegram botni Vercel Serverless (FastAPI) yordamida uzluksiz ishlashi uchun barcha kerakli tuzilmalar qo'shildi.
        </p>
        
        <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden mb-6">
          <div className="px-6 py-4 border-b border-slate-100 bg-slate-50">
            <h2 className="font-bold text-slate-700">Vercel'ga yuklash (Deploy) qadamlari:</h2>
          </div>
          <ul className="divide-y divide-slate-100 text-sm">
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-start gap-4">
              <div className="w-6 h-6 mt-0.5 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">1</div>
              <div className="leading-relaxed">
                Loyiha kodini <span className="font-semibold text-slate-800">GitHub</span>'ga yuklang. Vercel uchun maxsus 
                <code className="mx-1 font-mono bg-slate-100 text-slate-600 px-1 py-0.5 rounded text-xs">vercel.json</code> va 
                <code className="mx-1 font-mono bg-slate-100 text-slate-600 px-1 py-0.5 rounded text-xs">api/index.py</code> 
                fayllari qo'shildi.
              </div>
            </li>
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-start gap-4">
              <div className="w-6 h-6 mt-0.5 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">2</div>
              <div className="leading-relaxed">Vercel.com saytiga kirib, loyihangiz repozitoriyasini <strong>Add New Project</strong> orqali ulang. Server framework sifatida <strong>Other</strong> belgilashingiz (yoki avtomat qoldirishingiz) mumkin.</div>
            </li>
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-start gap-4">
               <div className="w-6 h-6 mt-0.5 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">3</div>
               <div className="leading-relaxed">
                 Deploy qilishdan oldin Verceldagi <strong>Environment Variables</strong> qismida parametrlarni kiriting:<br/>
                 <code className="font-mono bg-slate-100 text-slate-600 px-1 py-0.5 rounded text-xs mt-1 inline-block">BOT_TOKEN</code>, <code className="font-mono bg-slate-100 text-slate-600 px-1 py-0.5 rounded text-xs mt-1 inline-block">GEMINI_API_KEY</code>, va
                 <code className="font-mono bg-slate-100 text-slate-600 px-1 py-0.5 rounded text-xs mt-1 inline-block mx-1">DATABASE_URL</code> (Supabase, Neon kabi Postgres bazasi ko'rsatilishi shart).
               </div>
            </li>
            <li className="px-6 py-4 hover:bg-slate-50 text-slate-700 flex items-start gap-4">
               <div className="w-6 h-6 mt-0.5 flex-shrink-0 bg-blue-100 text-blue-600 rounded flex items-center justify-center font-bold text-xs">4</div>
               <div className="leading-relaxed">
                 Deploy jarayoni tugagandan so'ng, Serverga <strong>Webhook</strong> o'rnatish uchun quyidagi havolani brauzerda bosing:<br/>
                 <div className="mt-2 text-xs font-mono bg-blue-50 text-blue-700 p-2 rounded border border-blue-100 break-all select-all">
                   https://&lt;SIZNING-VERCEL-DOMEN&gt;/api/set_webhook?url=https://&lt;SIZNING-VERCEL-DOMEN&gt;
                 </div>
               </div>
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

