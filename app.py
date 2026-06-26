<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kraken • Sanctions Compliance Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=SF+Pro+Display:wght@400;500;600&amp;display=swap');
        
        :root {
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
        
        body {
            font-family: var(--font-sans);
        }
        
        .apple-font {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            font-feature-settings: "tnum";
        }
        
        .dashboard-header {
            background: linear-gradient(to right, #0F172A, #1E2937);
        }
        
        .metric-card {
            transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .metric-card:hover {
            transform: translateY(-2px);
        }
        
        .section-title {
            font-weight: 600;
            letter-spacing: -0.025em;
        }
        
        .clean-table {
            border: 1px solid #E2E8F0;
        }
        
        .nav-tab {
            transition: all 0.2s ease;
        }
        
        .nav-tab.active {
            border-bottom: 3px solid #0EA5E9;
            color: #0F172A;
            font-weight: 600;
        }
        
        .kraken-blue {
            color: #0EA5E9;
        }
        
        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 9999px;
        }
        
        .minimal-shadow {
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08);
        }
    </style>
</head>
<body class="bg-slate-50 apple-font">
    <!-- Header -->
    <div class="dashboard-header text-white">
        <div class="max-w-screen-2xl mx-auto px-8 py-6">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-x-4">
                    <div class="w-10 h-10 bg-white rounded-2xl flex items-center justify-center">
                        <i class="fa-solid fa-shield-halved text-slate-900 text-3xl"></i>
                    </div>
                    <div>
                        <h1 class="text-3xl font-semibold tracking-tight">Kraken</h1>
                        <p class="text-slate-400 text-sm -mt-1">Sanctions Compliance</p>
                    </div>
                </div>
                
                <div class="flex items-center gap-x-3">
                    <div class="px-4 py-1.5 bg-white/10 rounded-2xl text-sm flex items-center gap-x-2">
                        <i class="fa-solid fa-globe text-emerald-400"></i>
                        <span class="font-medium">Global Program</span>
                    </div>
                    <div class="text-right">
                        <div class="text-sm text-slate-300">Demo for Interview</div>
                        <div class="text-xs text-slate-400">Sr. Compliance Associate, Sanctions</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="max-w-screen-2xl mx-auto px-8 pt-8 pb-12">
        
        <!-- Top Metrics -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
            <div class="metric-card bg-white rounded-3xl p-6 border border-slate-200 minimal-shadow">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="text-sm font-medium text-slate-500">Active Sanctions Programs</p>
                        <p class="text-4xl font-semibold text-slate-900 mt-1">14</p>
                    </div>
                    <i class="fa-solid fa-globe text-3xl text-slate-300"></i>
                </div>
                <div class="mt-4 text-emerald-600 text-sm font-medium flex items-center gap-x-1">
                    <i class="fa-solid fa-arrow-trend-up"></i>
                    <span>+2 this quarter</span>
                </div>
            </div>
            
            <div class="metric-card bg-white rounded-3xl p-6 border border-slate-200 minimal-shadow">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="text-sm font-medium text-slate-500">Entities Screened (MTD)</p>
                        <p class="text-4xl font-semibold text-slate-900 mt-1">48,291</p>
                    </div>
                    <i class="fa-solid fa-search text-3xl text-slate-300"></i>
                </div>
                <div class="mt-4 text-emerald-600 text-sm font-medium">↑ 12% vs last month</div>
            </div>
            
            <div class="metric-card bg-white rounded-3xl p-6 border border-slate-200 minimal-shadow">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="text-sm font-medium text-slate-500">True Positive Hit Rate</p>
                        <p class="text-4xl font-semibold text-slate-900 mt-1">2.8%</p>
                    </div>
                    <i class="fa-solid fa-bullseye text-3xl text-slate-300"></i>
                </div>
                <div class="mt-4 text-amber-600 text-sm font-medium">Within target range</div>
            </div>
            
            <div class="metric-card bg-white rounded-3xl p-6 border border-slate-200 minimal-shadow">
                <div class="flex justify-between items-start">
                    <div>
                        <p class="text-sm font-medium text-slate-500">Reports Filed On Time</p>
                        <p class="text-4xl font-semibold text-slate-900 mt-1">100%</p>
                    </div>
                    <i class="fa-solid fa-file-export text-3xl text-emerald-500"></i>
                </div>
                <div class="mt-4 text-emerald-600 text-sm font-medium flex items-center gap-x-1">
                    <span>12/12 this period</span>
                </div>
            </div>
        </div>

        <!-- Navigation Tabs -->
        <div class="flex border-b border-slate-200 mb-8">
            <button onclick="showTab(0)" class="nav-tab active px-6 py-3 text-lg font-semibold text-slate-900 border-b-2 border-sky-500" id="tab-0">
                Executive Overview
            </button>
            <button onclick="showTab(1)" class="nav-tab px-6 py-3 text-lg font-semibold text-slate-600 hover:text-slate-900" id="tab-1">
                Regulatory Reporting
            </button>
            <button onclick="showTab(2)" class="nav-tab px-6 py-3 text-lg font-semibold text-slate-600 hover:text-slate-900" id="tab-2">
                Sanctions Intelligence
            </button>
        </div>

        <!-- TAB 0: Executive Overview -->
        <div id="tab-content-0">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Left Column -->
                <div class="lg:col-span-7 space-y-6">
                    <div class="bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow">
                        <div class="flex items-center justify-between mb-6">
                            <h3 class="section-title text-2xl text-slate-900">Sanctions Landscape</h3>
                            <span class="text-xs px-3 py-1 bg-slate-100 text-slate-500 rounded-2xl">Sample + Real OFAC Ready</span>
                        </div>
                        
                        <div class="grid grid-cols-3 gap-4">
                            <div>
                                <div class="text-sm text-slate-500 mb-1">Top Programs</div>
                                <div class="space-y-2 text-sm">
                                    <div class="flex justify-between"><span>Russia-related</span> <span class="font-semibold">38%</span></div>
                                    <div class="flex justify-between"><span>Cyber / Crypto</span> <span class="font-semibold">24%</span></div>
                                    <div class="flex justify-between"><span>Iran</span> <span class="font-semibold">18%</span></div>
                                </div>
                            </div>
                            <div>
                                <div class="text-sm text-slate-500 mb-1">By Entity Type</div>
                                <div class="space-y-2 text-sm">
                                    <div class="flex justify-between"><span>Entities</span> <span class="font-semibold">61%</span></div>
                                    <div class="flex justify-between"><span>Individuals</span> <span class="font-semibold">29%</span></div>
                                    <div class="flex justify-between"><span>Crypto Wallets</span> <span class="font-semibold">10%</span></div>
                                </div>
                            </div>
                            <div>
                                <div class="text-sm text-slate-500 mb-1">Crypto Exposure</div>
                                <div class="mt-2">
                                    <div class="text-3xl font-semibold text-slate-900">147</div>
                                    <div class="text-xs text-emerald-600">Sanctioned addresses monitored</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow">
                        <h3 class="section-title text-xl mb-4">Recent High-Impact Designations</h3>
                        <div class="space-y-3 text-sm">
                            <div class="flex justify-between items-center py-2 border-b border-slate-100">
                                <div><span class="font-medium">Tornado Cash</span> <span class="text-xs text-slate-400">(Aug 2022)</span></div>
                                <span class="px-3 py-0.5 text-xs bg-red-100 text-red-700 rounded-2xl">Critical</span>
                            </div>
                            <div class="flex justify-between items-center py-2 border-b border-slate-100">
                                <div><span class="font-medium">Lazarus Group</span> <span class="text-xs text-slate-400">(Ongoing)</span></div>
                                <span class="px-3 py-0.5 text-xs bg-red-100 text-red-700 rounded-2xl">Critical</span>
                            </div>
                            <div class="flex justify-between items-center py-2">
                                <div><span class="font-medium">Roman Semenov (Tornado Co-founder)</span></div>
                                <span class="px-3 py-0.5 text-xs bg-amber-100 text-amber-700 rounded-2xl">High</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right Column -->
                <div class="lg:col-span-5 bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow">
                    <h3 class="section-title text-xl mb-5">Automation Opportunity</h3>
                    
                    <div class="space-y-5">
                        <div>
                            <div class="flex justify-between text-sm mb-1.5">
                                <span class="font-medium">Current automation rate</span>
                                <span class="font-semibold">34%</span>
                            </div>
                            <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
                                <div class="h-2 bg-sky-500 rounded-full" style="width: 34%"></div>
                            </div>
                        </div>
                        
                        <div class="text-sm">
                            <div class="font-medium mb-2">Top areas for automation (next 90 days)</div>
                            <ul class="space-y-1.5 text-slate-600">
                                <li class="flex items-center gap-x-2"><i class="fa-solid fa-check text-emerald-500 w-4"></i> Name screening QC</li>
                                <li class="flex items-center gap-x-2"><i class="fa-solid fa-check text-emerald-500 w-4"></i> OFAC report narrative drafting</li>
                                <li class="flex items-center gap-x-2"><i class="fa-solid fa-check text-emerald-500 w-4"></i> Low-risk alert triage</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- TAB 1: Regulatory Reporting -->
        <div id="tab-content-1" class="hidden">
            <div class="bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow mb-6">
                <div class="flex items-center justify-between mb-6">
                    <div>
                        <h3 class="section-title text-2xl">Regulatory Reporting Hub</h3>
                        <p class="text-slate-500">OFAC + International filings status</p>
                    </div>
                    <button onclick="generateNarrative()" 
                            class="flex items-center gap-x-2 px-5 py-2.5 bg-slate-900 hover:bg-black text-white text-sm font-semibold rounded-2xl transition-colors">
                        <i class="fa-solid fa-magic"></i>
                        <span>Generate AI Narrative (Claude-style)</span>
                    </button>
                </div>
                
                <div class="overflow-x-auto">
                    <table class="w-full text-sm clean-table rounded-2xl overflow-hidden">
                        <thead class="bg-slate-50">
                            <tr>
                                <th class="text-left px-6 py-4 font-semibold">Report</th>
                                <th class="text-left px-6 py-4 font-semibold">Jurisdiction</th>
                                <th class="text-center px-6 py-4 font-semibold">Due Date</th>
                                <th class="text-center px-6 py-4 font-semibold">Status</th>
                                <th class="text-center px-6 py-4 font-semibold">QC</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            <tr>
                                <td class="px-6 py-4 font-medium">OFAC Annual Report of Blocked Property</td>
                                <td class="px-6 py-4">United States</td>
                                <td class="px-6 py-4 text-center">Mar 15, 2026</td>
                                <td class="px-6 py-4 text-center"><span class="inline-block px-3 py-1 text-xs bg-emerald-100 text-emerald-700 rounded-2xl">Submitted</span></td>
                                <td class="px-6 py-4 text-center"><span class="text-emerald-600 font-medium">Complete</span></td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 font-medium">OFAC Quarterly Blocked Property Report</td>
                                <td class="px-6 py-4">United States</td>
                                <td class="px-6 py-4 text-center">Jan 31, 2026</td>
                                <td class="px-6 py-4 text-center"><span class="inline-block px-3 py-1 text-xs bg-emerald-100 text-emerald-700 rounded-2xl">Submitted</span></td>
                                <td class="px-6 py-4 text-center"><span class="text-emerald-600 font-medium">Complete</span></td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 font-medium">UK Sanctions Reporting</td>
                                <td class="px-6 py-4">United Kingdom</td>
                                <td class="px-6 py-4 text-center">Feb 28, 2026</td>
                                <td class="px-6 py-4 text-center"><span class="inline-block px-3 py-1 text-xs bg-amber-100 text-amber-700 rounded-2xl">In Progress</span></td>
                                <td class="px-6 py-4 text-center"><span class="text-amber-600 font-medium">Pending</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <div class="bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow">
                <h4 class="font-semibold mb-3">AI-Generated Executive Summary</h4>
                <div id="narrative-output" class="text-slate-600 leading-relaxed text-[15px] min-h-[120px] p-5 bg-slate-50 rounded-2xl border border-slate-100">
                    Click the button above to generate a Claude-style narrative summary for leadership.
                </div>
            </div>
        </div>

        <!-- TAB 2: Sanctions Intelligence -->
        <div id="tab-content-2" class="hidden">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Screening Tool -->
                <div class="lg:col-span-5 bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow">
                    <h3 class="section-title text-xl mb-5">Quick Screening</h3>
                    
                    <div class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium text-slate-600 mb-1.5">Entity Name or Crypto Address</label>
                            <input id="screen-input" type="text" placeholder="e.g. Tornado Cash or 0x098B7..." 
                                   class="w-full px-4 py-3 border border-slate-300 rounded-2xl text-sm focus:outline-none focus:border-sky-400">
                        </div>
                        
                        <button onclick="runScreening()" 
                                class="w-full py-3 bg-sky-600 hover:bg-sky-700 text-white font-semibold rounded-2xl transition-colors flex items-center justify-center gap-x-2">
                            <i class="fa-solid fa-search"></i>
                            <span>Screen Now</span>
                        </button>
                    </div>
                    
                    <div id="screen-result" class="mt-5 hidden">
                        <!-- Populated by JS -->
                    </div>
                </div>
                
                <!-- Intelligence Summary -->
                <div class="lg:col-span-7 bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow">
                    <h3 class="section-title text-xl mb-5">Program Breakdown</h3>
                    
                    <div class="grid grid-cols-2 gap-x-8">
                        <div>
                            <div class="text-sm text-slate-500 mb-3">By Sanction Program</div>
                            <div class="space-y-3 text-sm">
                                <div class="flex justify-between items-center"><span>Russia-related</span> <span class="font-semibold">42%</span></div>
                                <div class="flex justify-between items-center"><span>Cyber / Crypto Mixers</span> <span class="font-semibold">27%</span></div>
                                <div class="flex justify-between items-center"><span>Iran</span> <span class="font-semibold">15%</span></div>
                                <div class="flex justify-between items-center"><span>North Korea</span> <span class="font-semibold">9%</span></div>
                            </div>
                        </div>
                        <div>
                            <div class="text-sm text-slate-500 mb-3">Crypto-Specific Risk</div>
                            <div class="mt-1">
                                <div class="flex items-baseline gap-x-2">
                                    <span class="text-4xl font-semibold">147</span>
                                    <span class="text-sm text-slate-500">sanctioned addresses</span>
                                </div>
                                <div class="text-emerald-600 text-sm mt-1">+18 new addresses this month</div>
                            </div>
                            
                            <div class="mt-5 text-xs bg-emerald-50 text-emerald-700 px-4 py-3 rounded-2xl">
                                <strong>Key insight:</strong> Tornado Cash and associated wallets remain the highest volume crypto-related designations.
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
            
            <!-- Real OFAC Data Section -->
            <div class="mt-6 bg-white rounded-3xl p-8 border border-slate-200 minimal-shadow">
                <div class="flex items-center justify-between mb-4">
                    <div>
                        <h3 class="section-title text-xl">Real OFAC Data</h3>
                        <p class="text-sm text-slate-500">Upload the official SDN.CSV for live screening (recommended for interview)</p>
                    </div>
                    <a href="https://sanctionslist.ofac.treas.gov/Home/SdnList" target="_blank" 
                       class="text-sky-600 hover:text-sky-700 text-sm flex items-center gap-x-1">
                        <span>Download latest SDN.CSV</span> <i class="fa-solid fa-external-link-alt text-xs"></i>
                    </a>
                </div>
                
                <div class="flex items-center gap-x-4">
                    <input type="file" id="ofac-upload" accept=".csv" class="hidden" onchange="loadOFACData(event)">
                    <button onclick="document.getElementById('ofac-upload').click()" 
                            class="px-6 py-2.5 border border-slate-300 hover:bg-slate-50 rounded-2xl text-sm font-medium flex items-center gap-x-2">
                        <i class="fa-solid fa-upload"></i>
                        <span>Upload SDN.CSV</span>
                    </button>
                    <span id="ofac-status" class="text-sm text-emerald-600 font-medium"></span>
                </div>
                <p class="text-xs text-slate-400 mt-2">The dashboard will use uploaded data for screening and exploration.</p>
            </div>
        </div>

    </div>

    <script>
        // Tailwind script
        function initializeTailwind() {
            // Already initialized via CDN
        }
        
        // Tab switching
        function showTab(tabIndex) {
            // Hide all tabs
            document.querySelectorAll('[id^="tab-content-"]').forEach(el => el.classList.add('hidden'));
            
            // Show selected tab
            document.getElementById('tab-content-' + tabIndex).classList.remove('hidden');
            
            // Update active tab styling
            document.querySelectorAll('.nav-tab').forEach((tab, index) => {
                if (index === tabIndex) {
                    tab.classList.add('active', 'border-b-2', 'border-sky-500', 'text-slate-900');
                    tab.classList.remove('text-slate-600');
                } else {
                    tab.classList.remove('active', 'border-b-2', 'border-sky-500', 'text-slate-900');
                    tab.classList.add('text-slate-600');
                }
            });
        }
        
        // Simulated AI Narrative Generation (Claude-style)
        function generateNarrative() {
            const output = document.getElementById('narrative-output');
            output.innerHTML = `
                <div class="animate-pulse">
                    <p class="text-slate-700">Generating executive summary using AI...</p>
                </div>
            `;
            
            setTimeout(() => {
                output.innerHTML = `
                    <p class="text-slate-700 leading-relaxed">
                        During the reporting period, Kraken maintained full compliance with all applicable sanctions regimes. 
                        A total of <strong>48,291 entities</strong> were screened with a true positive rate of <strong>2.8%</strong>. 
                        The most significant activity was observed in the Russia-related and Cyber programs, particularly involving 
                        cryptocurrency mixers. All required OFAC and international reports were filed on time with zero material deficiencies. 
                        Automation initiatives have increased efficiency by an estimated <strong>34%</strong> in low-risk alert handling.
                    </p>
                    <div class="mt-4 text-xs text-slate-400">— Generated in the style of Claude (Anthropic) for leadership review</div>
                `;
            }, 1200);
        }
        
        // Screening function
        let ofacData = null; // Will hold uploaded real data
        
        function runScreening() {
            const input = document.getElementById('screen-input').value.trim().toLowerCase();
            const resultDiv = document.getElementById('screen-result');
            
            if (!input) {
                resultDiv.innerHTML = `<div class="text-red-500 text-sm">Please enter a name or address.</div>`;
                resultDiv.classList.remove('hidden');
                return;
            }
            
            let matches = [];
            
            // Check sample data
            const sampleMatches = sampleSanctionsData.filter(item => 
                item.name.toLowerCase().includes(input) || 
                (item.addresses && item.addresses.some(addr => addr.toLowerCase().includes(input)))
            );
            
            matches = [...sampleMatches];
            
            // Check uploaded OFAC data if available
            if (ofacData && ofacData.length > 0) {
                const ofacMatches = ofacData.filter(item => 
                    item.name.toLowerCase().includes(input)
                ).slice(0, 5); // Limit results
                matches = [...matches, ...ofacMatches];
            }
            
            if (matches.length > 0) {
                let html = `<div class="mt-4"><div class="font-semibold text-emerald-700 mb-2">MATCH FOUND</div>`;
                
                matches.forEach(match => {
                    html += `
                        <div class="border border-emerald-200 bg-emerald-50 rounded-2xl p-4 mb-3">
                            <div class="flex justify-between">
                                <div>
                                    <div class="font-semibold">${match.name}</div>
                                    <div class="text-xs text-slate-500">${match.type || 'Entity'} • ${match.country || 'Various'}</div>
                                </div>
                                <div>
                                    <span class="px-3 py-0.5 text-xs rounded-2xl bg-red-100 text-red-700">Critical</span>
                                </div>
                            </div>
                            <div class="text-xs mt-2 text-slate-600">${match.notes || 'Sanctioned under relevant program.'}</div>
                        </div>
                    `;
                });
                
                html += `</div>`;
                resultDiv.innerHTML = html;
            } else {
                resultDiv.innerHTML = `
                    <div class="mt-4 p-4 bg-emerald-50 border border-emerald-200 rounded-2xl">
                        <div class="font-medium text-emerald-700">No direct match found.</div>
                        <div class="text-xs text-emerald-600 mt-1">Recommend enhanced due diligence and blockchain analytics review.</div>
                    </div>
                `;
            }
            
            resultDiv.classList.remove('hidden');
        }
        
        // Sample sanctions data
        const sampleSanctionsData = [
            {
                name: "Tornado Cash",
                type: "Entity",
                country: "Decentralized",
                program: "Cyber-related",
                addresses: ["0x858942737084d477b3a6e4b6e0e3e3e3e3e3e3e3", "0x722122df12d4e14e13ac3b6895a86e84145b6967"],
                notes: "Decentralized Ethereum mixer sanctioned for facilitating money laundering.",
                risk: "Critical"
            },
            {
                name: "Lazarus Group",
                type: "Entity",
                country: "North Korea",
                program: "DPRK",
                addresses: ["0x098B716B8Aaf21512996dC57EB0615e2383E2f96"],
                notes: "State-sponsored hacking group linked to major crypto heists.",
                risk: "Critical"
            },
            {
                name: "Roman Semenov",
                type: "Individual",
                country: "Russia",
                program: "Cyber-related",
                addresses: [],
                notes: "Co-founder of Tornado Cash.",
                risk: "Critical"
            },
            {
                name: "Vladimir Putin",
                type: "Individual",
                country: "Russia",
                program: "Russia-related",
                addresses: [],
                notes: "President of the Russian Federation.",
                risk: "Critical"
            }
        ];
        
        // Load real OFAC data
        function loadOFACData(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            const statusEl = document.getElementById('ofac-status');
            statusEl.innerHTML = `<i class="fa-solid fa-spinner fa-spin mr-2"></i>Processing...`;
            
            const reader = new FileReader();
            reader.onload = function(e) {
                try {
                    const csv = e.target.result;
                    const lines = csv.split('\n');
                    
                    // Simple parsing for common OFAC SDN.CSV structure
                    // OFAC format is usually: ent_num,SDN_Name,SDN_Type,Programs,Country, etc.
                    const parsedData = [];
                    
                    for (let i = 1; i < Math.min(lines.length, 500); i++) { // Limit for performance
                        const row = lines[i].split(',');
                        if (row.length > 3 && row[1]) {
                            parsedData.push({
                                name: row[1].replace(/"/g, '').trim(),
                                type: row[2] ? row[2].replace(/"/g, '').trim() : 'Entity',
                                country: row[4] ? row[4].replace(/"/g, '').trim() : 'Various',
                                program: row[3] ? row[3].replace(/"/g, '').trim() : 'Various',
                                notes: 'Loaded from official OFAC SDN list',
                                risk: 'Critical'
                            });
                        }
                    }
                    
                    ofacData = parsedData;
                    statusEl.innerHTML = `<i class="fa-solid fa-check mr-1"></i> Loaded ${parsedData.length} records`;
                    statusEl.className = 'text-sm text-emerald-600 font-medium';
                    
                    // Optional: Show success toast
                    setTimeout(() => {
                        if (statusEl) statusEl.innerHTML = `Using real OFAC data (${parsedData.length} entities)`;
                    }, 3000);
                    
                } catch (error) {
                    statusEl.innerHTML = `Error parsing file. Please use official SDN.CSV.`;
                    statusEl.className = 'text-sm text-red-500';
                }
            };
            reader.readAsText(file);
        }
        
        // Initialize
        function initializeDashboard() {
            initializeTailwind();
            
            // Show first tab by default
            document.getElementById('tab-content-0').classList.remove('hidden');
            document.getElementById('tab-0').classList.add('active', 'border-b-2', 'border-sky-500', 'text-slate-900');
            
            // Keyboard support for screening
            const screenInput = document.getElementById('screen-input');
            if (screenInput) {
                screenInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        runScreening();
                    }
                });
            }
            
            // Welcome note in console for developer
            console.log('%c[Kraken Dashboard] Interview-ready sanctions dashboard initialized. Use real OFAC upload for maximum impact.', 'color:#64748b');
        }
        
        // Boot the app
        window.onload = initializeDashboard;
    </script>
</body>
</html>
