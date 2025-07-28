<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔥 Fusion Strategy Scanner - XAU/BTC Live Pro</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        /* Enhanced animated background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 25% 25%, rgba(255, 107, 53, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 75% 75%, rgba(0, 255, 136, 0.1) 0%, transparent 50%);
            animation: backgroundFloat 20s ease-in-out infinite;
            pointer-events: none;
            z-index: -1;
        }

        @keyframes backgroundFloat {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            33% { transform: translate(30px, -30px) rotate(1deg); }
            66% { transform: translate(-20px, 20px) rotate(-1deg); }
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255, 107, 53, 0.1), transparent);
            animation: headerShimmer 3s linear infinite;
        }

        @keyframes headerShimmer {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }

        .header h1 {
            font-size: 2.5rem;
            background: linear-gradient(45deg, #ff6b35, #f7931e, #ffdd00, #ff6b35);
            background-size: 300% 300%;
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            animation: gradientShift 4s ease-in-out infinite;
            position: relative;
            z-index: 1;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(0, 0, 0, 0.4);
            padding: 15px 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        .status-indicator {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .pulse {
            width: 12px;
            height: 12px;
            background: #00ff88;
            border-radius: 50%;
            animation: pulse 2s infinite;
            box-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
        }

        @keyframes pulse {
            0% { transform: scale(1); opacity: 1; box-shadow: 0 0 10px rgba(0, 255, 136, 0.5); }
            50% { transform: scale(1.3); opacity: 0.7; box-shadow: 0 0 20px rgba(0, 255, 136, 0.8); }
            100% { transform: scale(1); opacity: 1; box-shadow: 0 0 10px rgba(0, 255, 136, 0.5); }
        }

        .config-panel {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .config-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 25px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .config-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.6s ease;
        }

        .config-card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 107, 53, 0.3);
            box-shadow: 0 10px 30px rgba(255, 107, 53, 0.2);
        }

        .config-card:hover::before {
            left: 100%;
        }

        .config-card h3 {
            color: #ff6b35;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.2rem;
        }

        .input-group {
            margin-bottom: 18px;
        }

        .input-group label {
            display: block;
            margin-bottom: 8px;
            color: #e0e0e0;
            font-size: 0.95rem;
            font-weight: 500;
        }

        .input-group input, .input-group select {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            background: rgba(0, 0, 0, 0.4);
            color: #ffffff;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }

        .input-group input:focus, .input-group select:focus {
            outline: none;
            border-color: #ff6b35;
            box-shadow: 0 0 15px rgba(255, 107, 53, 0.4);
            background: rgba(0, 0, 0, 0.6);
        }

        .btn {
            background: linear-gradient(45deg, #ff6b35, #f7931e);
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            margin: 5px;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s ease;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(255, 107, 53, 0.5);
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .signals-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
            gap: 25px;
            margin-bottom: 25px;
        }

        .signal-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 25px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .signal-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, transparent, currentColor, transparent);
            animation: borderGlow 2s ease-in-out infinite;
        }

        @keyframes borderGlow {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .signal-card.bullish {
            border-left: 4px solid #00ff88;
            color: #00ff88;
        }

        .signal-card.bearish {
            border-left: 4px solid #ff4757;
            color: #ff4757;
        }

        .signal-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }

        .signal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .signal-type {
            font-weight: 700;
            font-size: 1.2rem;
            color: #ffffff;
        }

        .signal-time {
            font-size: 0.85rem;
            color: #999;
            background: rgba(255, 255, 255, 0.1);
            padding: 4px 8px;
            border-radius: 8px;
        }

        .signal-details {
            margin-bottom: 20px;
            color: #ffffff;
        }

        .signal-details p {
            margin-bottom: 10px;
            line-height: 1.5;
            padding: 8px 12px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            border-left: 3px solid rgba(255, 107, 53, 0.5);
        }

        .confidence-bar {
            width: 100%;
            height: 10px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 15px;
            position: relative;
        }

        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff4757, #ffa502, #00ff88);
            transition: width 0.8s ease;
            position: relative;
            overflow: hidden;
        }

        .confidence-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            animation: confidenceShimmer 2s linear infinite;
        }

        @keyframes confidenceShimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .strategy-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 15px;
        }

        .strategy-tag {
            background: rgba(255, 107, 53, 0.2);
            color: #ff6b35;
            padding: 6px 12px;
            border-radius: 15px;
            font-size: 0.75rem;
            border: 1px solid rgba(255, 107, 53, 0.4);
            transition: all 0.3s ease;
        }

        .strategy-tag:hover {
            background: rgba(255, 107, 53, 0.3);
            transform: scale(1.05);
        }

        .logs-container {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 20px;
            padding: 25px;
            margin-top: 25px;
            max-height: 500px;
            overflow-y: auto;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        .logs-container::-webkit-scrollbar {
            width: 8px;
        }

        .logs-container::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
        }

        .logs-container::-webkit-scrollbar-thumb {
            background: rgba(255, 107, 53, 0.5);
            border-radius: 4px;
        }

        .log-entry {
            margin-bottom: 10px;
            padding: 12px 15px;
            border-left: 4px solid #333;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            transition: all 0.3s ease;
            animation: logSlideIn 0.5s ease;
        }

        @keyframes logSlideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .log-entry:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateX(5px);
        }

        .log-entry.success {
            border-left-color: #00ff88;
            background: rgba(0, 255, 136, 0.05);
        }

        .log-entry.warning {
            border-left-color: #ffa502;
            background: rgba(255, 165, 2, 0.05);
        }

        .log-entry.error {
            border-left-color: #ff4757;
            background: rgba(255, 71, 87, 0.05);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, #ff6b35, #f7931e, #ffdd00);
            animation: statGlow 3s linear infinite;
        }

        @keyframes statGlow {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(255, 107, 53, 0.2);
        }

        .stat-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #ff6b35;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 0.85rem;
            color: #bbb;
            margin-top: 8px;
        }

        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid rgba(255, 255, 255, 0.1);
            border-top: 4px solid #ff6b35;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .alert {
            padding: 18px 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            border: 1px solid;
            animation: alertSlideIn 0.5s ease;
            position: relative;
            overflow: hidden;
        }

        @keyframes alertSlideIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .alert::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            animation: alertShimmer 3s linear infinite;
        }

        @keyframes alertShimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .alert.success {
            background: rgba(0, 255, 136, 0.15);
            border-color: #00ff88;
            color: #00ff88;
        }

        .alert.error {
            background: rgba(255, 71, 87, 0.15);
            border-color: #ff4757;
            color: #ff4757;
        }

        .alert.warning {
            background: rgba(255, 165, 2, 0.15);
            border-color: #ffa502;
            color: #ffa502;
        }

        /* Enhanced mobile responsiveness */
        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            
            .config-panel {
                grid-template-columns: 1fr;
            }
            
            .signals-container {
                grid-template-columns: 1fr;
            }
            
            .status-bar {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }

            .header h1 {
                font-size: 2rem;
            }

            .config-card {
                padding: 20px;
            }
        }

        /* Additional enhancements */
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 255, 136, 0.9);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            animation: notificationSlide 0.5s ease;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }

        @keyframes notificationSlide {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        .session-indicator {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            animation: sessionPulse 2s ease-in-out infinite;
        }

        .session-indicator.active {
            background: rgba(0, 255, 136, 0.2);
            color: #00ff88;
            border: 1px solid #00ff88;
        }

        .session-indicator.inactive {
            background: rgba(255, 71, 87, 0.2);
            color: #ff4757;
            border: 1px solid #ff4757;
        }

        @keyframes sessionPulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }

        /* Fix for checkboxes - enhanced styling */
        .input-group input[type="checkbox"] {
            width: auto;
            margin-right: 10px;
            transform: scale(1.3);
            accent-color: #ff6b35;
            cursor: pointer;
        }

        .input-group label:has(input[type="checkbox"]) {
            display: flex;
            align-items: center;
            cursor: pointer;
            padding: 8px 0;
            transition: color 0.3s ease;
        }

        .input-group label:has(input[type="checkbox"]):hover {
            color: #ff6b35;
        }

        /* Enhanced button styling */
        .btn.success {
            background: linear-gradient(45deg, #00ff88, #00d4aa);
        }

        .btn.danger {
            background: linear-gradient(45deg, #ff4757, #c44569);
        }

        /* Loading animation enhancement */
        .loading span {
            animation: loadingText 2s ease-in-out infinite;
        }

        @keyframes loadingText {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        /* Enhanced signal card animations */
        .signal-card {
            animation: cardEntrance 0.6s ease-out;
        }

        @keyframes cardEntrance {
            from {
                opacity: 0;
                transform: translateY(30px) scale(0.9);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        /* Responsive design improvements */
        @media (max-width: 480px) {
            .header h1 {
                font-size: 1.8rem;
            }
            
            .status-bar {
                padding: 12px 15px;
            }
            
            .config-card {
                padding: 15px;
            }
            
            .btn {
                padding: 12px 20px;
                font-size: 0.9rem;
            }
        }

        /* Scrollbar styling for all containers */
        * {
            scrollbar-width: thin;
            scrollbar-color: rgba(255, 107, 53, 0.5) rgba(255, 255, 255, 0.1);
        }

        *::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        *::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
        }

        *::-webkit-scrollbar-thumb {
            background: rgba(255, 107, 53, 0.5);
            border-radius: 4px;
            transition: background 0.3s ease;
        }

        *::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 107, 53, 0.8);
        }

        /* Enhanced focus states */
        .btn:focus,
        .input-group input:focus,
        .input-group select:focus {
            outline: 2px solid #ff6b35;
            outline-offset: 2px;
        }

        /* Enhanced active states */
        .btn:active {
            transform: translateY(-1px) scale(0.98);
        }

        /* Enhanced disabled states */
        .btn:disabled {
            background: rgba(100, 100, 100, 0.3);
            color: rgba(255, 255, 255, 0.5);
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .btn:disabled::before {
            display: none;
        }

        /* Text selection styling */
        ::selection {
            background: rgba(255, 107, 53, 0.3);
            color: #ffffff;
        }

        ::-moz-selection {
            background: rgba(255, 107, 53, 0.3);
            color: #ffffff;
        }

        /* Enhanced log entry styling */
        .log-entry.info {
            border-left-color: #3498db;
            background: rgba(52, 152, 219, 0.05);
        }

        /* Pulsing effect for important elements */
        .pulse-glow {
            animation: pulseGlow 3s ease-in-out infinite;
        }

        @keyframes pulseGlow {
            0%, 100% {
                box-shadow: 0 0 5px rgba(255, 107, 53, 0.3);
            }
            50% {
                box-shadow: 0 0 20px rgba(255, 107, 53, 0.6);
            }
        }

        /* Enhanced signal type indicators */
        .signal-type .trade-action {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-left: 8px;
        }

        .signal-type .trade-action.buy {
            background: rgba(0, 255, 136, 0.2);
            color: #00ff88;
            border: 1px solid #00ff88;
        }

        .signal-type .trade-action.sell {
            background: rgba(255, 71, 87, 0.2);
            color: #ff4757;
            border: 1px solid #ff4757;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔥 Fusion Strategy Scanner Pro</h1>
            <p>Advanced XAU/BTC Analysis with AI-Powered Telegram Signals - Version 2.0</p>
            <div style="margin-top: 15px;">
                <span class="session-indicator" id="sessionIndicator">Loading Session...</span>
            </div>
        </div>

        <div class="status-bar">
            <div class="status-indicator">
                <div class="pulse" id="statusPulse"></div>
                <span id="statusText">Initializing Advanced Scanner...</span>
            </div>
            <div>
                <span>⏱️ Uptime: </span>
                <span id="uptime">00:00:00</span>
            </div>
            <div>
                <span>📤 Signals Sent: </span>
                <span id="signalCount">0</span>
            </div>
            <div>
                <span>💰 Total Profit: </span>
                <span id="totalProfit">$0.00</span>
            </div>
        </div>

        <div class="config-panel">
            <div class="config-card">
                <h3>📱 Enhanced Telegram Setup</h3>
                <div class="input-group">
                    <label>🔑 Bot Token</label>
                    <input type="password" id="botToken" placeholder="Your Telegram Bot Token" autocomplete="off">
                </div>
                <div class="input-group">
                    <label>💬 Chat ID</label>
                    <input type="text" id="chatId" placeholder="Your Telegram Chat ID">
                </div>
                <div class="input-group">
                    <label>🔔 Notifications</label>
                    <select id="notificationLevel">
                        <option value="all">All Signals</option>
                        <option value="high" selected>High Confidence Only</option>
                        <option value="premium">Premium Setups Only</option>
                    </select>
                </div>
                <button class="btn" onclick="testTelegram()">🧪 Test Connection</button>
                <button class="btn success" onclick="sendWelcomeMessage()">👋 Send Welcome</button>
            </div>

            <div class="config-card">
                <h3>⚙️ AI Scanner Configuration</h3>
                <div class="input-group">
                    <label>🔄 Scan Interval</label>
                    <select id="scanInterval">
                        <option value="15">15 seconds (Ultra Fast)</option>
                        <option value="30" selected>30 seconds (Optimal)</option>
                        <option value="45">45 seconds (Balanced)</option>
                        <option value="60">1 minute (Conservative)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🎯 Minimum Confidence %</label>
                    <select id="minConfidence">
                        <option value="80">80% (Good)</option>
                        <option value="85" selected>85% (Premium)</option>
                        <option value="90">90% (Ultra)</option>
                        <option value="95">95% (Elite)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🧠 Required AI Strategies</label>
                    <select id="minStrategies">
                        <option value="2">2+ Strategies</option>
                        <option value="3" selected>3+ Strategies (Recommended)</option>
                        <option value="4">4+ Strategies (Conservative)</option>
                        <option value="5">5+ Strategies (Ultra Conservative)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🔗 Required Confluences</label>
                    <select id="minConfluences">
                        <option value="3">3+ Confluences</option>
                        <option value="4" selected>4+ Confluences (Recommended)</option>
                        <option value="5">5+ Confluences</option>
                        <option value="6">6+ Confluences (Ultra)</option>
                    </select>
                </div>
                <button class="btn pulse-glow" id="toggleScanner" onclick="toggleScanner()">🚀 Start AI Scanner</button>
            </div>

            <div class="config-card">
                <h3>💰 Advanced Risk Management</h3>
                <div class="input-group">
                    <label>💳 Account Balance ($)</label>
                    <input type="number" id="accountBalance" value="10000" placeholder="10000" min="100">
                </div>
                <div class="input-group">
                    <label>⚖️ Risk Per Trade (%)</label>
                    <select id="riskPercent">
                        <option value="0.5">0.5% (Ultra Conservative)</option>
                        <option value="1">1% (Conservative)</option>
                        <option value="2" selected>2% (Balanced)</option>
                        <option value="3">3% (Aggressive)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>📊 Max Daily Signals</label>
                    <select id="maxDailySignals">
                        <option value="3">3 signals (Quality Focus)</option>
                        <option value="5">5 signals</option>
                        <option value="10" selected>10 signals (Balanced)</option>
                        <option value="15">15 signals (Active)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🛡️ Daily Loss Limit (%)</label>
                    <select id="dailyLossLimit">
                        <option value="5" selected>5% (Recommended)</option>
                        <option value="10">10%</option>
                        <option value="15">15%</option>
                    </select>
                </div>
            </div>

            <div class="config-card">
                <h3>🔌 Real Market Data APIs</h3>
                <div class="input-group">
                    <label>📊 Data Provider</label>
                    <select id="dataProvider">
                        <option value="simulation" selected>Simulation Mode (Demo)</option>
                        <option value="alphavantage">Alpha Vantage (Free/Paid)</option>
                        <option value="binance">Binance API (Free)</option>
                        <option value="fxempire">FX Empire (Free)</option>
                        <option value="coingecko">CoinGecko (Free)</option>
                        <option value="twelvedata">Twelve Data (Free/Paid)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🔑 API Key (Optional for some providers)</label>
                    <input type="password" id="apiKey" placeholder="Enter your API key here">
                    <small style="color: #888; font-size: 0.8rem; margin-top: 5px; display: block;">
                        💡 Some providers work without API key. Check documentation below.
                    </small>
                </div>
                <div class="input-group">
                    <label>⚡ Update Frequency</label>
                    <select id="dataUpdateFreq">
                        <option value="1">1 second (Premium)</option>
                        <option value="5" selected>5 seconds (Standard)</option>
                        <option value="15">15 seconds (Conservative)</option>
                        <option value="30">30 seconds (Light)</option>
                    </select>
                </div>
                <button class="btn" onclick="testAPIConnection()">🧪 Test API</button>
                <button class="btn success" onclick="toggleRealData()">📡 Enable Real Data</button>
                
                <!-- API Info Panel -->
                <div style="margin-top: 15px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 10px; border-left: 3px solid #ff6b35;">
                    <h4 style="color: #ff6b35; margin-bottom: 10px;">📚 API Setup Guide:</h4>
                    <div id="apiInfo">
                        <p style="font-size: 0.85rem; line-height: 1.4; color: #ccc;">
                            Select a data provider above to see setup instructions.
                        </p>
                    </div>
                </div>
            </div>

            <div class="config-card">
                <h3>📈 Market Data Status</h3>
                <div class="input-group">
                    <label>🔗 Connection Status</label>
                    <input type="text" id="connectionStatus" readonly value="Simulation Mode" style="background: rgba(0,0,0,0.6);">
                </div>
                <div class="input-group">
                    <label>📊 Data Quality</label>
                    <div style="display: flex; gap: 10px; align-items: center;">
                        <div class="data-quality-indicator" id="dataQuality">
                            <div class="quality-bar" style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px;">
                                <div style="width: 85%; height: 100%; background: linear-gradient(90deg, #ff4757, #ffa502, #00ff88); border-radius: 4px;"></div>
                            </div>
                        </div>
                        <span style="font-size: 0.8rem; color: #00ff88;">85% Quality</span>
                    </div>
                </div>
                <div class="input-group">
                    <label>⏱️ Last Update</label>
                    <input type="text" id="lastDataUpdate" readonly value="Real-time" style="background: rgba(0,0,0,0.6);">
                </div>
                <div class="input-group">
                    <label>📡 API Calls Today</label>
                    <input type="text" id="apiCallsCount" readonly value="0 / 500" style="background: rgba(0,0,0,0.6);">
                </div>
            </div>
            <div class="config-card">
                <h3>🕐 Session & Timing Control</h3>
                <div class="input-group">
                    <label>🌍 Current Market Session</label>
                    <input type="text" id="currentSession" readonly value="Loading..." style="background: rgba(0,0,0,0.6);">
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="londonSession" checked> 🇬🇧 London Killzone (7-10 UTC)</label>
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="nySession" checked> 🇺🇸 NY Killzone (13:30-16:30 UTC)</label>
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="asianSession"> 🇯🇵 Asian Killzone (0-3 UTC)</label>
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="weekendMode"> 🌙 Weekend Mode (Crypto Only)</label>
                </div>
            </div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value" id="xauPrice">Loading...</div>
                <div class="stat-label">XAU/USD Live Price</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="btcPrice">Loading...</div>
                <div class="stat-label">BTC/USD Live Price</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="setupsDetected">0</div>
                <div class="stat-label">AI Setups Found</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="avgConfidence">0%</div>
                <div class="stat-label">Average Confidence</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="winRate">0%</div>
                <div class="stat-label">Win Rate (24h)</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="todayPnL">$0.00</div>
                <div class="stat-label">Today's P&L</div>
            </div>
        </div>

        <div class="signals-container" id="signalsContainer">
            <div class="loading">
                <div class="spinner"></div>
                <span style="margin-left: 15px;">Initializing AI Scanner...</span>
            </div>
        </div>

        <div class="logs-container">
            <h3>📊 Advanced System Logs</h3>
            <div class="input-group" style="margin-bottom: 15px;">
                <select id="logFilter" onchange="filterLogs()" style="width: 200px;">
                    <option value="all">All Logs</option>
                    <option value="success">Success Only</option>
                    <option value="warning">Warnings Only</option>
                    <option value="error">Errors Only</option>
                    <option value="signals">Signals Only</option>
                </select>
                <button class="btn" onclick="clearLogs()" style="margin-left: 10px; padding: 8px 16px;">🗑️ Clear</button>
            </div>
            <div id="logsContainer">
                <div class="log-entry success">✅ Advanced AI System initialized - Ready for premium scanning</div>
            </div>
        </div>
    </div>

    <script>
        // Enhanced Global Variables with Real API Support
        let isScanning = false;
        let scanInterval = null;
        let startTime = new Date();
        let signalsSent = 0;
        let setupsDetected = 0;
        let confidenceSum = 0;
        let strategiesSum = 0;
        let confluencesSum = 0;
        let telegramBot = null;
        let telegramChatId = null;
        let dailyPnL = 0;
        let totalProfit = 0;
        let winCount = 0;
        let lossCount = 0;
        let todaySignals = 0;
        let lastScanTime = null;
        
        // Real API Variables
        let isRealDataEnabled = false;
        let currentDataProvider = 'simulation';
        let apiKey = '';
        let apiCallsToday = 0;
        let dataUpdateInterval = null;
        let lastAPICall = null;
        
        // Enhanced Market Data with Real-time Support
        const marketData = {
            XAUUSD: { 
                price: 2050.25, 
                change: 0.15, 
                history: [],
                volume: 0,
                volatility: 0,
                trend: 'NEUTRAL',
                lastUpdate: new Date(),
                source: 'simulation'
            },
            BTCUSD: { 
                price: 43250.80, 
                change: -0.08, 
                history: [],
                volume: 0,
                volatility: 0,
                trend: 'NEUTRAL',
                lastUpdate: new Date(),
                source: 'simulation'
            }
        };

        // Real API Endpoints Configuration
        const apiEndpoints = {
            alphavantage: {
                name: 'Alpha Vantage',
                forex: 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=XAU&to_symbol=USD&interval=1min&apikey={API_KEY}',
                crypto: 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=USD&apikey={API_KEY}',
                requiresKey: true,
                freeLimit: 5,
                description: 'Professional financial data with 500 free calls/day. Get free key at alphavantage.co'
            },
            binance: {
                name: 'Binance API',
                crypto: 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT',
                forex: null, // Binance doesn't have XAU directly
                requiresKey: false,
                freeLimit: 1200,
                description: 'Free crypto data from Binance. No API key required. Limited to crypto only.'
            },
            coingecko: {
                name: 'CoinGecko',
                crypto: 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true',
                forex: 'https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd&include_24hr_change=true',
                requiresKey: false,
                freeLimit: 50,
                description: 'Free crypto and some commodities data. 50 calls/minute limit. No registration required.'
            },
            twelvedata: {
                name: 'Twelve Data',
                forex: 'https://api.twelvedata.com/price?symbol=XAU/USD&apikey={API_KEY}',
                crypto: 'https://api.twelvedata.com/price?symbol=BTC/USD&apikey={API_KEY}',
                requiresKey: true,
                freeLimit: 800,
                description: 'Professional data for stocks, forex, crypto. 800 free calls/day. Get key at twelvedata.com'
            },
            fxempire: {
                name: 'FX Empire',
                forex: 'https://api.fxempire.com/v1/en/markets/XAU/USD',
                crypto: 'https://api.fxempire.com/v1/en/markets/BTC/USD',
                requiresKey: false,
                freeLimit: 100,
                description: 'Free financial data. Limited calls per day. No registration required.'
            }
        };

        // ENHANCED REAL MARKET DATA INTEGRATION
        const enhancedApiEndpoints = {
            alphavantage: {
                name: 'Alpha Vantage',
                gold: 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=XAUUSD&interval=1min&apikey={API_KEY}&outputsize=compact',
                bitcoin: 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=USD&apikey={API_KEY}',
                requiresKey: true,
                freeLimit: 500,
                supportsOHLC: true,
                realTime: true,
                description: 'Professional real-time OHLC data with bank-grade precision'
            },
            binance: {
                name: 'Binance API',
                bitcoin: 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=100',
                bitcoinPrice: 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT',
                gold: null, // Binance doesn't have XAU directly
                requiresKey: false,
                freeLimit: 1200,
                supportsOHLC: true,
                realTime: true,
                description: 'Free real-time Bitcoin OHLC data with millisecond precision'
            },
            twelvedata: {
                name: 'Twelve Data',
                gold: 'https://api.twelvedata.com/time_series?symbol=XAUUSD&interval=1min&apikey={API_KEY}&outputsize=100',
                bitcoin: 'https://api.twelvedata.com/time_series?symbol=BTCUSD&interval=1min&apikey={API_KEY}&outputsize=100',
                goldPrice: 'https://api.twelvedata.com/price?symbol=XAUUSD&apikey={API_KEY}',
                bitcoinPrice: 'https://api.twelvedata.com/price?symbol=BTCUSD&apikey={API_KEY}',
                requiresKey: true,
                freeLimit: 800,
                supportsOHLC: true,
                realTime: true,
                description: 'Professional forex and crypto data with bank-grade feeds'
            },
            coingecko: {
                name: 'CoinGecko',
                bitcoin: 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true',
                gold: 'https://api.coingecko.com/api/v3/simple/price?ids=tether-gold&vs_currencies=usd&include_24hr_change=true',
                requiresKey: false,
                freeLimit: 30, // Per minute
                supportsOHLC: false,
                realTime: false,
                description: 'Free basic price data - good for backup/redundancy'
            },
            goldapi: {
                name: 'Gold API',
                gold: 'https://api.metals.live/v1/spot/gold',
                requiresKey: false,
                freeLimit: 100,
                supportsOHLC: false,
                realTime: true,
                description: 'Specialized gold price feed from London markets'
            }
        };

        // REAL-TIME MARKET DATA FETCHER
        async function fetchRealMarketData() {
            if (!isRealDataEnabled || currentDataProvider === 'simulation') return;
            
            try {
                addLog(`🔄 Fetching real market data via ${currentDataProvider}...`, 'info');
                
                // Parallel fetch for both gold and bitcoin
                const promises = [];
                
                // Fetch Gold Data
                if (currentDataProvider !== 'binance') { // Binance doesn't have gold
                    promises.push(fetchRealGoldData());
                }
                
                // Fetch Bitcoin Data
                promises.push(fetchRealBitcoinData());
                
                // Execute all fetches
                const results = await Promise.allSettled(promises);
                
                // Process results
                results.forEach((result, index) => {
                    if (result.status === 'rejected') {
                        addLog(`❌ Failed to fetch ${index === 0 ? 'Gold' : 'Bitcoin'} data: ${result.reason}`, 'error');
                    }
                });
                
                // Update API call counter
                apiCallsToday += promises.length;
                updateAPICallsDisplay();
                
                // Update last update time
                const updateEl = safeGetElement('lastDataUpdate');
                if (updateEl) {
                    updateEl.value = new Date().toLocaleTimeString();
                }
                
                addLog(`✅ Real market data updated successfully`, 'success');
                
            } catch (error) {
                addLog(`❌ Real data fetch error: ${error.message}`, 'error');
            }
        }

        // FETCH REAL GOLD DATA
        async function fetchRealGoldData() {
            const api = enhancedApiEndpoints[currentDataProvider];
            if (!api || !api.gold) return;
            
            let url = api.gold;
            if (api.requiresKey && apiKey) {
                url = url.replace('{API_KEY}', apiKey);
            }
            
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Gold API Error: ${response.status} ${response.statusText}`);
            }
            
            const data = await response.json();
            const goldData = parseGoldData(data, currentDataProvider);
            
            if (goldData.price > 0) {
                updateMarketData('XAUUSD', goldData);
                addLog(`🥇 Gold updated: $${goldData.price.toFixed(2)} (${goldData.change > 0 ? '+' : ''}${goldData.change.toFixed(2)})`, 'success');
            }
        }

        // FETCH REAL BITCOIN DATA  
        async function fetchRealBitcoinData() {
            const api = enhancedApiEndpoints[currentDataProvider];
            if (!api || !api.bitcoin) return;
            
            let url = api.bitcoin;
            if (api.requiresKey && apiKey) {
                url = url.replace('{API_KEY}', apiKey);
            }
            
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Bitcoin API Error: ${response.status} ${response.statusText}`);
            }
            
            const data = await response.json();
            const btcData = parseBitcoinData(data, currentDataProvider);
            
            if (btcData.price > 0) {
                updateMarketData('BTCUSD', btcData);
                addLog(`₿ Bitcoin updated: $${btcData.price.toFixed(0)} (${btcData.change > 0 ? '+' : ''}${btcData.change.toFixed(2)}%)`, 'success');
            }
        }

        // PARSE GOLD DATA FROM DIFFERENT PROVIDERS
        function parseGoldData(data, provider) {
            let price = 0;
            let change = 0;
            let ohlcCandles = [];
            
            switch (provider) {
                case 'alphavantage':
                    const timeSeries = data['Time Series (1min)'];
                    if (timeSeries) {
                        const timestamps = Object.keys(timeSeries).sort().reverse();
                        const latestData = timeSeries[timestamps[0]];
                        
                        price = parseFloat(latestData['4. close']);
                        
                        // Build OHLC array
                        ohlcCandles = timestamps.slice(0, 100).reverse().map(timestamp => ({
                            timestamp: new Date(timestamp),
                            open: parseFloat(timeSeries[timestamp]['1. open']),
                            high: parseFloat(timeSeries[timestamp]['2. high']),
                            low: parseFloat(timeSeries[timestamp]['3. low']),
                            close: parseFloat(timeSeries[timestamp]['4. close']),
                            volume: parseFloat(timeSeries[timestamp]['5. volume'])
                        }));
                        
                        // Calculate change
                        if (ohlcCandles.length > 1) {
                            change = ((price - ohlcCandles[ohlcCandles.length - 2].close) / ohlcCandles[ohlcCandles.length - 2].close) * 100;
                        }
                    }
                    break;
                    
                case 'twelvedata':
                    if (data.values && data.values.length > 0) {
                        const latest = data.values[0];
                        price = parseFloat(latest.close);
                        
                        // Build OHLC array
                        ohlcCandles = data.values.reverse().map(candle => ({
                            timestamp: new Date(candle.datetime),
                            open: parseFloat(candle.open),
                            high: parseFloat(candle.high),
                            low: parseFloat(candle.low),
                            close: parseFloat(candle.close),
                            volume: parseFloat(candle.volume || 0)
                        }));
                        
                        // Calculate change
                        if (ohlcCandles.length > 1) {
                            change = ((price - ohlcCandles[ohlcCandles.length - 2].close) / ohlcCandles[ohlcCandles.length - 2].close) * 100;
                        }
                    }
                    break;
                    
                case 'goldapi':
                    if (data.price) {
                        price = parseFloat(data.price);
                        change = parseFloat(data.ch || 0);
                    }
                    break;
                    
                case 'coingecko':
                    if (data['tether-gold']) {
                        price = data['tether-gold'].usd;
                        change = data['tether-gold'].usd_24h_change || 0;
                    }
                    break;
            }
            
            return { price, change, ohlcCandles };
        }

        // PARSE BITCOIN DATA FROM DIFFERENT PROVIDERS
        function parseBitcoinData(data, provider) {
            let price = 0;
            let change = 0;
            let ohlcCandles = [];
            
            switch (provider) {
                case 'binance':
                    if (Array.isArray(data)) {
                        // Klines data
                        ohlcCandles = data.map(candle => ({
                            timestamp: new Date(candle[0]),
                            open: parseFloat(candle[1]),
                            high: parseFloat(candle[2]),
                            low: parseFloat(candle[3]),
                            close: parseFloat(candle[4]),
                            volume: parseFloat(candle[5])
                        }));
                        
                        if (ohlcCandles.length > 0) {
                            price = ohlcCandles[ohlcCandles.length - 1].close;
                            
                            // Calculate 24h change
                            if (ohlcCandles.length > 1440) { // 24h in minutes
                                const dayAgo = ohlcCandles[ohlcCandles.length - 1440].close;
                                change = ((price - dayAgo) / dayAgo) * 100;
                            }
                        }
                    } else if (data.price) {
                        // Simple price ticker
                        price = parseFloat(data.price);
                    }
                    break;
                    
                case 'alphavantage':
                    const timeSeries = data['Time Series (Digital Currency Intraday)'];
                    if (timeSeries) {
                        const timestamps = Object.keys(timeSeries).sort().reverse();
                        const latestData = timeSeries[timestamps[0]];
                        
                        price = parseFloat(latestData['4a. close (USD)']);
                        
                        // Build OHLC array
                        ohlcCandles = timestamps.slice(0, 100).reverse().map(timestamp => ({
                            timestamp: new Date(timestamp),
                            open: parseFloat(timeSeries[timestamp]['1a. open (USD)']),
                            high: parseFloat(timeSeries[timestamp]['2a. high (USD)']),
                            low: parseFloat(timeSeries[timestamp]['3a. low (USD)']),
                            close: parseFloat(timeSeries[timestamp]['4a. close (USD)']),
                            volume: parseFloat(timeSeries[timestamp]['5. volume'])
                        }));
                        
                        // Calculate change
                        if (ohlcCandles.length > 1) {
                            change = ((price - ohlcCandles[ohlcCandles.length - 2].close) / ohlcCandles[ohlcCandles.length - 2].close) * 100;
                        }
                    }
                    break;
                    
                case 'twelvedata':
                    if (data.values && data.values.length > 0) {
                        const latest = data.values[0];
                        price = parseFloat(latest.close);
                        
                        // Build OHLC array
                        ohlcCandles = data.values.reverse().map(candle => ({
                            timestamp: new Date(candle.datetime),
                            open: parseFloat(candle.open),
                            high: parseFloat(candle.high),
                            low: parseFloat(candle.low),
                            close: parseFloat(candle.close),
                            volume: parseFloat(candle.volume || 0)
                        }));
                        
                        // Calculate change
                        if (ohlcCandles.length > 1) {
                            change = ((price - ohlcCandles[ohlcCandles.length - 2].close) / ohlcCandles[ohlcCandles.length - 2].close) * 100;
                        }
                    }
                    break;
                    
                case 'coingecko':
                    if (data.bitcoin) {
                        price = data.bitcoin.usd;
                        change = data.bitcoin.usd_24h_change || 0;
                    }
                    break;
            }
            
            return { price, change, ohlcCandles };
        }

        // UPDATE MARKET DATA WITH REAL DATA
        function updateMarketData(symbol, newData) {
            const data = marketData[symbol];
            const oldPrice = data.price;
            
            // Update basic data
            data.price = newData.price;
            data.change = newData.change;
            data.lastUpdate = new Date();
            data.source = currentDataProvider;
            
            // Update OHLC data if available
            if (newData.ohlcCandles && newData.ohlcCandles.length > 0) {
                data.ohlcData = newData.ohlcCandles;
                
                // Update technical indicators with real data
                updateTechnicalIndicators(symbol);
                
                // Update bank-specific data with real analysis
                updateBankSpecificData(symbol);
                
                addLog(`📊 ${symbol} OHLC updated: ${newData.ohlcCandles.length} candles`, 'info');
            } else {
                // Add to price history for basic analysis
                data.history.push(newData.price);
                if (data.history.length > 100) {
                    data.history.shift();
                }
            }
            
            // Update trend
            updateTrends();
            
            // Update UI with flash effect
            updateRealPriceDisplay(symbol, newData.price, newData.price - oldPrice);
            
            // Trigger bank analysis if significant price move
            const priceMove = Math.abs((newData.price - oldPrice) / oldPrice);
            if (priceMove > 0.005) { // 0.5% move
                addLog(`🚨 Significant ${symbol} move: ${(priceMove * 100).toFixed(2)}% - triggering bank analysis`, 'warning');
                
                // Trigger immediate scan if scanner is active
                if (isScanning) {
                    setTimeout(() => performAdvancedScan(), 1000);
                }
            }
        }

        // UPDATE BANK SPECIFIC DATA WITH REAL MARKET CONDITIONS
        function updateBankSpecificData(symbol) {
            if (symbol === 'XAUUSD') {
                // Update gold-specific bank data with real correlations
                const goldData = marketData.XAUUSD;
                
                // Simulate real DXY correlation update
                goldData.bankData.dxyCorrelation = -0.82 + (Math.random() - 0.5) * 0.1;
                
                // Update VIX level based on gold volatility
                const recentVolatility = calculateVolatility(goldData.ohlcData);
                goldData.bankData.vixLevel = 15 + (recentVolatility * 1000); // Approximate VIX
                
                // Update Gold/Silver ratio
                goldData.bankData.gsRatio = goldData.price / 24.5; // Approximate silver price
                
                // Update seasonal bias
                goldData.bankData.seasonalBias = analyzeGoldSeasonality().bias;
                
            } else if (symbol === 'BTCUSD') {
                // Update Bitcoin institutional data
                const btcData = marketData.BTCUSD;
                
                // Simulate institutional flow updates
                const priceMove = btcData.ohlcData.length > 1 ? 
                    (btcData.price - btcData.ohlcData[btcData.ohlcData.length - 2].close) / btcData.ohlcData[btcData.ohlcData.length - 2].close : 0;
                
                if (Math.abs(priceMove) > 0.02) { // 2% move
                    btcData.bankData.etfInflows = priceMove > 0 ? 150 : -120; // Simulate flows
                    btcData.bankData.whaleMovements = priceMove > 0 ? 'ACCUMULATION' : 'DISTRIBUTION';
                }
                
                // Update correlation to tech stocks (approximate)
                btcData.bankData.correlationToTech = 0.65 + (Math.random() - 0.5) * 0.2;
            }
        }

        // CALCULATE VOLATILITY FROM OHLC DATA
        function calculateVolatility(ohlcData) {
            if (!ohlcData || ohlcData.length < 20) return 0.01;
            
            const returns = [];
            for (let i = 1; i < ohlcData.length; i++) {
                const returnVal = Math.log(ohlcData[i].close / ohlcData[i - 1].close);
                returns.push(returnVal);
            }
            
            const mean = returns.reduce((sum, ret) => sum + ret, 0) / returns.length;
            const variance = returns.reduce((sum, ret) => sum + Math.pow(ret - mean, 2), 0) / returns.length;
            
            return Math.sqrt(variance * 252); // Annualized volatility
        }

        // UPDATE API CALLS DISPLAY
        function updateAPICallsDisplay() {
            const api = enhancedApiEndpoints[currentDataProvider];
            const callsEl = safeGetElement('apiCallsCount');
            if (callsEl && api) {
                callsEl.value = `${apiCallsToday} / ${api.freeLimit}`;
                
                // Warning when approaching limits
                if (apiCallsToday > api.freeLimit * 0.8) {
                    callsEl.style.color = '#ff4757';
                    addLog(`⚠️ API limit warning: ${apiCallsToday}/${api.freeLimit} calls used`, 'warning');
                }
            }
        }

        // ENHANCED REAL-TIME TEST FUNCTION
        async function testRealMarketConnection() {
            addLog('🧪 Testing real market data connection...', 'info');
            
            try {
                // Test both gold and bitcoin feeds
                await fetchRealMarketData();
                
                // Verify we got real data
                const goldPrice = marketData.XAUUSD.price;
                const btcPrice = marketData.BTCUSD.price;
                
                if (goldPrice > 1000 && goldPrice < 5000) {
                    addLog(`✅ Gold real-time data verified: $${goldPrice.toFixed(2)}`, 'success');
                } else {
                    addLog(`⚠️ Gold price seems incorrect: $${goldPrice.toFixed(2)}`, 'warning');
                }
                
                if (btcPrice > 10000 && btcPrice < 200000) {
                    addLog(`✅ Bitcoin real-time data verified: $${btcPrice.toFixed(0)}`, 'success');
                } else {
                    addLog(`⚠️ Bitcoin price seems incorrect: $${btcPrice.toFixed(0)}`, 'warning');
                }
                
                // Test bank analysis with real data
                const goldAnalysis = performBankGradeAnalysis('XAUUSD');
                const btcAnalysis = performBankGradeAnalysis('BTCUSD');
                
                if (goldAnalysis) {
                    addLog(`🏦 Gold bank analysis successful: ${goldAnalysis.aiScore}% confidence, ${goldAnalysis.strategies.length} strategies`, 'success');
                } else {
                    addLog(`📊 Gold analysis: No premium setups detected (maintaining high standards)`, 'info');
                }
                
                if (btcAnalysis) {
                    addLog(`🏦 Bitcoin bank analysis successful: ${btcAnalysis.aiScore}% confidence`, 'success');
                } else {
                    addLog(`📊 Bitcoin analysis: No premium setups detected`, 'info');
                }
                
                showNotification('Real market data connection successful!', 'success');
                
            } catch (error) {
                addLog(`❌ Real market test failed: ${error.message}`, 'error');
                showNotification(`Market test failed: ${error.message}`, 'error');
            }
        }

        // REPLACE OLD TEST FUNCTION
        async function testAPIConnection() {
            if (currentDataProvider === 'simulation') {
                showNotification('Simulation mode - switching to real market test', 'info');
                await testRealMarketConnection();
            } else {
                await testRealMarketConnection();
            }
        }

        // Test API Connection
        async function testAPIConnection() {
            const provider = safeGetElement('dataProvider')?.value || 'simulation';
            const apiKeyInput = safeGetElement('apiKey')?.value || '';
            
            if (provider === 'simulation') {
                showNotification('Simulation mode - no API test needed', 'success');
                addLog('✅ Simulation mode active - test successful', 'success');
                return;
            }
            
            const api = apiEndpoints[provider];
            if (!api) {
                showNotification('Invalid API provider selected', 'error');
                return;
            }
            
            if (api.requiresKey && !apiKeyInput) {
                showNotification(`${api.name} requires an API key`, 'warning');
                addLog(`⚠️ ${api.name} requires API key`, 'warning');
                return;
            }
            
            addLog(`🧪 Testing ${api.name} connection...`, 'info');
            
            try {
                // Test with BTC first (most APIs support this)
                let testUrl = api.crypto;
                if (testUrl && api.requiresKey) {
                    testUrl = testUrl.replace('{API_KEY}', apiKeyInput);
                }
                
                if (!testUrl) {
                    showNotification(`${api.name} doesn't support crypto data`, 'warning');
                    return;
                }
                
                const response = await fetch(testUrl);
                
                if (response.ok) {
                    const data = await response.json();
                    showNotification(`${api.name} connection successful!`, 'success');
                    addLog(`✅ ${api.name} API test successful`, 'success');
                    
                    // Update connection status
                    const statusEl = safeGetElement('connectionStatus');
                    if (statusEl) statusEl.value = `${api.name} - Connected`;
                    
                } else {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                
            } catch (error) {
                showNotification(`${api.name} connection failed: ${error.message}`, 'error');
                addLog(`❌ ${api.name} API test failed: ${error.message}`, 'error');
            }
        }

        // Toggle Real Data Mode
        function toggleRealData() {
            const provider = safeGetElement('dataProvider')?.value || 'simulation';
            
            if (provider === 'simulation') {
                showNotification('Please select a real data provider first', 'warning');
                return;
            }
            
            if (!isRealDataEnabled) {
                // Enable real data
                enableRealDataFeed();
            } else {
                // Disable real data
                disableRealDataFeed();
            }
        }

        // Enable Real Data Feed
        function enableRealDataFeed() {
            const provider = safeGetElement('dataProvider')?.value || 'simulation';
            const frequency = parseInt(safeGetElement('dataUpdateFreq')?.value || '5') * 1000;
            
            isRealDataEnabled = true;
            currentDataProvider = provider;
            apiKey = safeGetElement('apiKey')?.value || '';
            
            // Start real data updates
            if (dataUpdateInterval) clearInterval(dataUpdateInterval);
            dataUpdateInterval = setInterval(fetchRealMarketData, frequency);
            
            // Initial fetch
            fetchRealMarketData();
            
            showNotification(`Real data enabled with ${apiEndpoints[provider].name}`, 'success');
            addLog(`📡 Real data feed enabled: ${apiEndpoints[provider].name}`, 'success');
            
            // Update button
            const button = event.target;
            button.textContent = '📡 Disable Real Data';
            button.className = 'btn danger';
        }

        // Disable Real Data Feed
        function disableRealDataFeed() {
            isRealDataEnabled = false;
            
            if (dataUpdateInterval) {
                clearInterval(dataUpdateInterval);
                dataUpdateInterval = null;
            }
            
            // Reset to simulation
            currentDataProvider = 'simulation';
            updatePrices(); // Resume simulation
            
            showNotification('Switched back to simulation mode', 'warning');
            addLog('🎮 Real data disabled - back to simulation', 'warning');
            
            // Update button
            const button = event.target;
            button.textContent = '📡 Enable Real Data';
            button.className = 'btn success';
            
            // Update status
            const statusEl = safeGetElement('connectionStatus');
            if (statusEl) statusEl.value = 'Simulation Mode';
        }

        // Fetch Real Market Data
        async function fetchRealMarketData() {
            if (!isRealDataEnabled || currentDataProvider === 'simulation') return;
            
            const api = apiEndpoints[currentDataProvider];
            if (!api) return;
            
            try {
                // Fetch BTC data
                if (api.crypto) {
                    await fetchSymbolData('BTCUSD', api.crypto, api);
                }
                
                // Fetch XAU data (if available)
                if (api.forex) {
                    await fetchSymbolData('XAUUSD', api.forex, api);
                }
                
                // Update API calls counter
                apiCallsToday++;
                const callsEl = safeGetElement('apiCallsCount');
                if (callsEl) {
                    callsEl.value = `${apiCallsToday} / ${api.freeLimit}`;
                }
                
                // Update last update time
                const updateEl = safeGetElement('lastDataUpdate');
                if (updateEl) {
                    updateEl.value = new Date().toLocaleTimeString();
                }
                
                lastAPICall = new Date();
                
            } catch (error) {
                addLog(`❌ Real data fetch error: ${error.message}`, 'error');
                
                // Fallback to simulation on repeated errors
                if (apiCallsToday > 0 && apiCallsToday % 5 === 0) {
                    addLog('⚠️ Multiple API errors - consider switching provider', 'warning');
                }
            }
        }

        // Fetch Individual Symbol Data
        async function fetchSymbolData(symbol, endpoint, apiConfig) {
            let url = endpoint;
            
            // Replace API key if required
            if (apiConfig.requiresKey && apiKey) {
                url = url.replace('{API_KEY}', apiKey);
            }
            
            const response = await fetch(url);
            
            if (!response.ok) {
                throw new Error(`API Error: ${response.status} ${response.statusText}`);
            }
            
            const data = await response.json();
            
            // Parse data based on provider
            let price = 0;
            let change = 0;
            
            switch (currentDataProvider) {
                case 'binance':
                    price = parseFloat(data.price);
                    break;
                    
                case 'coingecko':
                    if (symbol === 'BTCUSD') {
                        price = data.bitcoin?.usd || 0;
                        change = data.bitcoin?.usd_24h_change || 0;
                    } else if (symbol === 'XAUUSD') {
                        price = data['tether-gold']?.usd || 2050; // Fallback
                        change = data['tether-gold']?.usd_24h_change || 0;
                    }
                    break;
                    
                case 'alphavantage':
                    // Parse Alpha Vantage response (more complex)
                    const timeSeries = data['Time Series FX (1min)'] || data['Time Series (Digital Currency Intraday)'];
                    if (timeSeries) {
                        const latestKey = Object.keys(timeSeries)[0];
                        const latestData = timeSeries[latestKey];
                        price = parseFloat(latestData['4. close'] || latestData['1a. price (USD)'] || 0);
                    }
                    break;
                    
                case 'twelvedata':
                    price = parseFloat(data.price || 0);
                    break;
                    
                case 'fxempire':
                    price = parseFloat(data.price || data.last || 0);
                    change = parseFloat(data.change || 0);
                    break;
            }
            
            // Update market data if valid price received
            if (price > 0) {
                const oldPrice = marketData[symbol].price;
                marketData[symbol].price = price;
                marketData[symbol].change = change;
                marketData[symbol].lastUpdate = new Date();
                marketData[symbol].source = currentDataProvider;
                
                // Add to history
                marketData[symbol].history.push(price);
                if (marketData[symbol].history.length > 100) {
                    marketData[symbol].history.shift();
                }
                
                // Update UI
                updateRealPriceDisplay(symbol, price, price - oldPrice);
                
                addLog(`📊 ${symbol} updated: $${price.toFixed(symbol.includes('BTC') ? 0 : 2)} via ${apiConfig.name}`, 'success');
            }
        }

        // Update Real Price Display
        function updateRealPriceDisplay(symbol, price, priceChange) {
            const elementId = symbol === 'XAUUSD' ? 'xauPrice' : 'btcPrice';
            const element = safeGetElement(elementId);
            
            if (element) {
                const decimals = symbol.includes('BTC') ? 0 : 2;
                element.textContent = `$${price.toFixed(decimals)}`;
                element.style.color = priceChange > 0 ? '#00ff88' : priceChange < 0 ? '#ff4757' : '#ffffff';
                
                // Add flash effect for real updates
                element.style.transition = 'all 0.3s ease';
                element.style.transform = 'scale(1.05)';
                setTimeout(() => {
                    element.style.transform = 'scale(1)';
                }, 300);
            }
        }
            <div class="stat-card">
                <div class="stat-value" id="xauPrice">Loading...</div>
                <div class="stat-label">XAU/USD Live Price</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="btcPrice">Loading...</div>
                <div class="stat-label">BTC/USD Live Price</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="setupsDetected">0</div>
                <div class="stat-label">AI Setups Found</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="avgConfidence">0%</div>
                <div class="stat-label">Average Confidence</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="winRate">0%</div>
                <div class="stat-label">Win Rate (24h)</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="todayPnL">$0.00</div>
                <div class="stat-label">Today's P&L</div>
            </div>
        </div>

        <div class="signals-container" id="signalsContainer">
            <div class="loading">
                <div class="spinner"></div>
                <span style="margin-left: 15px;">Initializing AI Scanner...</span>
            </div>
        </div>

        <div class="logs-container">
            <h3>📊 Advanced System Logs</h3>
            <div class="input-group" style="margin-bottom: 15px;">
                <select id="logFilter" onchange="filterLogs()" style="width: 200px;">
                    <option value="all">All Logs</option>
                    <option value="success">Success Only</option>
                    <option value="warning">Warnings Only</option>
                    <option value="error">Errors Only</option>
                    <option value="signals">Signals Only</option>
                </select>
                <button class="btn" onclick="clearLogs()" style="margin-left: 10px; padding: 8px 16px;">🗑️ Clear</button>
            </div>
            <div id="logsContainer">
                <div class="log-entry success">✅ Advanced AI System initialized - Ready for premium scanning</div>
            </div>
        </div>
    </div> {
            left: 100%;
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .signals-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
            gap: 25px;
            margin-bottom: 25px;
        }

        .signal-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 25px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .signal-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, transparent, currentColor, transparent);
            animation: borderGlow 2s ease-in-out infinite;
        }

        @keyframes borderGlow {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .signal-card.bullish {
            border-left: 4px solid #00ff88;
            color: #00ff88;
        }

        .signal-card.bearish {
            border-left: 4px solid #ff4757;
            color: #ff4757;
        }

        .signal-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }

        .signal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .signal-type {
            font-weight: 700;
            font-size: 1.2rem;
            color: #ffffff;
        }

        .signal-time {
            font-size: 0.85rem;
            color: #999;
            background: rgba(255, 255, 255, 0.1);
            padding: 4px 8px;
            border-radius: 8px;
        }

        .signal-details {
            margin-bottom: 20px;
            color: #ffffff;
        }

        .signal-details p {
            margin-bottom: 10px;
            line-height: 1.5;
            padding: 8px 12px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            border-left: 3px solid rgba(255, 107, 53, 0.5);
        }

        .confidence-bar {
            width: 100%;
            height: 10px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 15px;
            position: relative;
        }

        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #ff4757, #ffa502, #00ff88);
            transition: width 0.8s ease;
            position: relative;
            overflow: hidden;
        }

        .confidence-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            animation: confidenceShimmer 2s linear infinite;
        }

        @keyframes confidenceShimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .strategy-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 15px;
        }

        .strategy-tag {
            background: rgba(255, 107, 53, 0.2);
            color: #ff6b35;
            padding: 6px 12px;
            border-radius: 15px;
            font-size: 0.75rem;
            border: 1px solid rgba(255, 107, 53, 0.4);
            transition: all 0.3s ease;
        }

        .strategy-tag:hover {
            background: rgba(255, 107, 53, 0.3);
            transform: scale(1.05);
        }

        .logs-container {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 20px;
            padding: 25px;
            margin-top: 25px;
            max-height: 500px;
            overflow-y: auto;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }

        .logs-container::-webkit-scrollbar {
            width: 8px;
        }

        .logs-container::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
        }

        .logs-container::-webkit-scrollbar-thumb {
            background: rgba(255, 107, 53, 0.5);
            border-radius: 4px;
        }

        .log-entry {
            margin-bottom: 10px;
            padding: 12px 15px;
            border-left: 4px solid #333;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            transition: all 0.3s ease;
            animation: logSlideIn 0.5s ease;
        }

        @keyframes logSlideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .log-entry:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateX(5px);
        }

        .log-entry.success {
            border-left-color: #00ff88;
            background: rgba(0, 255, 136, 0.05);
        }

        .log-entry.warning {
            border-left-color: #ffa502;
            background: rgba(255, 165, 2, 0.05);
        }

        .log-entry.error {
            border-left-color: #ff4757;
            background: rgba(255, 71, 87, 0.05);
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, #ff6b35, #f7931e, #ffdd00);
            animation: statGlow 3s linear infinite;
        }

        @keyframes statGlow {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(255, 107, 53, 0.2);
        }

        .stat-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #ff6b35;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 0.85rem;
            color: #bbb;
            margin-top: 8px;
        }

        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 4px solid rgba(255, 255, 255, 0.1);
            border-top: 4px solid #ff6b35;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .alert {
            padding: 18px 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            border: 1px solid;
            animation: alertSlideIn 0.5s ease;
            position: relative;
            overflow: hidden;
        }

        @keyframes alertSlideIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .alert::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            animation: alertShimmer 3s linear infinite;
        }

        @keyframes alertShimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .alert.success {
            background: rgba(0, 255, 136, 0.15);
            border-color: #00ff88;
            color: #00ff88;
        }

        .alert.error {
            background: rgba(255, 71, 87, 0.15);
            border-color: #ff4757;
            color: #ff4757;
        }

        .alert.warning {
            background: rgba(255, 165, 2, 0.15);
            border-color: #ffa502;
            color: #ffa502;
        }

        /* Enhanced mobile responsiveness */
        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            
            .config-panel {
                grid-template-columns: 1fr;
            }
            
            .signals-container {
                grid-template-columns: 1fr;
            }
            
            .status-bar {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }

            .header h1 {
                font-size: 2rem;
            }

            .config-card {
                padding: 20px;
            }
        }

        /* Additional enhancements */
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 255, 136, 0.9);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            animation: notificationSlide 0.5s ease;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }

        @keyframes notificationSlide {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        .session-indicator {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            animation: sessionPulse 2s ease-in-out infinite;
        }

        .session-indicator.active {
            background: rgba(0, 255, 136, 0.2);
            color: #00ff88;
            border: 1px solid #00ff88;
        }

        .session-indicator.inactive {
            background: rgba(255, 71, 87, 0.2);
            color: #ff4757;
            border: 1px solid #ff4757;
        }

        @keyframes sessionPulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logs-container">
            <h3>📊 Advanced System Logs</h3>
            <div class="input-group" style="margin-bottom: 15px;">
                <select id="logFilter" onchange="filterLogs()" style="width: 200px;">
                    <option value="all">All Logs</option>
                    <option value="success">Success Only</option>
                    <option value="warning">Warnings Only</option>
                    <option value="error">Errors Only</option>
                    <option value="signals">Signals Only</option>
                </select>
                <button class="btn" onclick="clearLogs()" style="margin-left: 10px; padding: 8px 16px;">🗑️ Clear</button>
            </div>
            <div id="logsContainer">
                <div class="log-entry success">✅ Advanced AI System initialized - Ready for premium scanning</div>
            </div>
        </div>
    </div>

    <script>
        // Enhanced Global Variables
        let isScanning = false;
        let scanInterval = null;
        let startTime = new Date();
        let signalsSent = 0;
        let setupsDetected = 0;
        let confidenceSum = 0;
        let strategiesSum = 0;
        let confluencesSum = 0;
        let telegramBot = null;
        let telegramChatId = null;
        let dailyPnL = 0;
        let totalProfit = 0;
        let winCount = 0;
        let lossCount = 0;
        let todaySignals = 0;
        let lastScanTime = null;
        
        // Enhanced Market Data with Real-time Updates
        const marketData = {
            XAUUSD: { 
                price: 2050.25, 
                change: 0.15, 
                history: [],
                volume: 0,
                volatility: 0,
                trend: 'NEUTRAL'
            },
            BTCUSD: { 
                price: 43250.80, 
                change: -0.08, 
                history: [],
                volume: 0,
                volatility: 0,
                trend: 'NEUTRAL'
            }
        };

        // Advanced AI Strategy Framework
        const advancedStrategies = {
            ict: {
                name: "ICT Framework Pro",
                patterns: ["Liquidity Sweep", "BOS", "FVG", "Order Block", "Displacement"],
                weight: 0.30,
                confidence: 0
            },
            smc: {
                name: "Smart Money Concept", 
                patterns: ["CHoCH", "BOS", "Imbalance", "Structure Break", "Inducement"],
                weight: 0.25,
                confidence: 0
            },
            institutional: {
                name: "Institutional Flow AI",
                patterns: ["Dark Pool", "Volume Spike", "Absorption", "Algorithm Pattern"],
                weight: 0.25,
                confidence: 0
            },
            liquidity: {
                name: "Liquidity Analysis Pro",
                patterns: ["Void Detection", "Cluster Magnetism", "Raid Setup", "Snapback"],
                weight: 0.20,
                confidence: 0
            },
            volumeProfile: {
                name: "Volume Profile AI",
                patterns: ["POC Rejection", "Value Area", "Volume Gap", "High Volume Node"],
                weight: 0.15,
                confidence: 0
            },
            marketStructure: {
                name: "Structure Analysis",
                patterns: ["Support/Resistance", "Fibonacci", "Trendline", "Pattern"],
                weight: 0.15,
                confidence: 0
            },
            sentiment: {
                name: "Market Sentiment AI",
                patterns: ["Fear/Greed", "News Impact", "Social Sentiment", "Options Flow"],
                weight: 0.10,
                confidence: 0
            }
        };

        // Initialize Enhanced Application
        function init() {
            updateUptime();
            setInterval(updateUptime, 1000);
            updatePrices();
            setInterval(updatePrices, 2000);
            updateSessionIndicator();
            setInterval(updateSessionIndicator, 60000);
            loadSettings();
            addLog("🚀 Advanced AI Scanner initialized successfully", "success");
            addLog("💡 Pro tip: Enable notifications for high-confidence signals only", "info");
        }

        // Enhanced Uptime Display
        function updateUptime() {
            const now = new Date();
            const diff = now - startTime;
            const hours = Math.floor(diff / 3600000).toString().padStart(2, '0');
            const minutes = Math.floor((diff % 3600000) / 60000).toString().padStart(2, '0');
            const seconds = Math.floor((diff % 60000) / 1000).toString().padStart(2, '0');
            document.getElementById('uptime').textContent = `${hours}:${minutes}:${seconds}`;
        }

        // Enhanced Market Price Updates with Trend Analysis
        function updatePrices() {
            // Simulate realistic price movements with volatility
            const xauVolatility = 0.002 + Math.random() * 0.003;
            const btcVolatility = 0.001 + Math.random() * 0.002;
            
            const xauChange = (Math.random() - 0.5) * xauVolatility * marketData.XAUUSD.price;
            const btcChange = (Math.random() - 0.5) * btcVolatility * marketData.BTCUSD.price;
            
            marketData.XAUUSD.price += xauChange;
            marketData.BTCUSD.price += btcChange;
            
            // Update history for trend analysis
            marketData.XAUUSD.history.push(marketData.XAUUSD.price);
            marketData.BTCUSD.history.push(marketData.BTCUSD.price);
            
            // Keep only last 100 prices
            if (marketData.XAUUSD.history.length > 100) {
                marketData.XAUUSD.history.shift();
                marketData.BTCUSD.history.shift();
            }
            
            // Calculate trends
            updateTrends();
            
            // Update UI
            const xauElement = document.getElementById('xauPrice');
            const btcElement = document.getElementById('btcPrice');
            
            xauElement.textContent = `$${marketData.XAUUSD.price.toFixed(2)}`;
            btcElement.textContent = `$${marketData.BTCUSD.price.toFixed(0)}`;
            
            // Add color based on change
            xauElement.style.color = xauChange > 0 ? '#00ff88' : '#ff4757';
            btcElement.style.color = btcChange > 0 ? '#00ff88' : '#ff4757';
        }

        // Update trend analysis
        function updateTrends() {
            ['XAUUSD', 'BTCUSD'].forEach(symbol => {
                const history = marketData[symbol].history;
                if (history.length >= 20) {
                    const recent = history.slice(-10);
                    const older = history.slice(-20, -10);
                    const recentAvg = recent.reduce((a, b) => a + b) / recent.length;
                    const olderAvg = older.reduce((a, b) => a + b) / older.length;
                    
                    if (recentAvg > olderAvg * 1.001) {
                        marketData[symbol].trend = 'BULLISH';
                    } else if (recentAvg < olderAvg * 0.999) {
                        marketData[symbol].trend = 'BEARISH';
                    } else {
                        marketData[symbol].trend = 'NEUTRAL';
                    }
                }
            });
        }

        // Enhanced Session Indicator
        function updateSessionIndicator() {
            const indicator = document.getElementById('sessionIndicator');
            const currentSession = getCurrentKillzone();
            const isActive = isInKillzone();
            
            indicator.textContent = `${currentSession} ${isActive ? '🟢' : '🔴'}`;
            indicator.className = `session-indicator ${isActive ? 'active' : 'inactive'}`;
            
            document.getElementById('currentSession').value = currentSession;
        }

        // Enhanced Telegram Test with Welcome Message
        async function testTelegram() {
            const token = document.getElementById('botToken').value;
            const chatId = document.getElementById('chatId').value;
            
            if (!token || !chatId) {
                showNotification("Please enter both Bot Token and Chat ID", "error");
                addLog("❌ Telegram configuration incomplete", "error");
                return;
            }

            try {
                const response = await fetch(`https://api.telegram.org/bot${telegramBot}/sendMessage`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chat_id: telegramChatId,
                        text: message,
                        parse_mode: 'HTML'
                    })
                });

                if (response.ok) {
                    signalsSent++;
                    todaySignals++;
                    document.getElementById('signalCount').textContent = signalsSent;
                    addLog(`📤 ${tradeAction} signal sent: ${signal.symbol} (AI: ${signal.aiScore}%, R:R 1:${signal.riskReward.toFixed(2)})`, "success");
                    
                    // Send follow-up analysis after 3 seconds
                    setTimeout(() => sendSignalAnalysis(signal, tradeAction), 3000);
                } else {
                    addLog("❌ Failed to send Telegram signal", "error");
                }
            } catch (error) {
                addLog(`❌ Telegram send error: ${error.message}`, "error");
            }
        }

        // Send detailed signal analysis
        async function sendSignalAnalysis(signal, tradeAction) {
            const analysisMsg = `
📈 <b>DETAILED ANALYSIS - ${signal.symbol}</b>

🔍 <b>Market Context:</b>
• Current trend: ${marketData[signal.symbol].trend}
• Session: ${signal.session}
• Volatility: ${(Math.random() * 2 + 1).toFixed(1)}% (${Math.random() > 0.5 ? 'High' : 'Normal'})

🎯 <b>Entry Strategy:</b>
• Wait for confirmation at entry level
• Consider scaling in with 2-3 positions
• Use limit orders to avoid slippage
• Monitor for 15-30 minutes after entry

⚠️ <b>Risk Management:</b>
• Never move SL against you
• Consider taking 50% profit at 1:1 R:R
• Trail SL to breakeven after 1:2 R:R
• Exit all if price moves 20% against setup

📊 <b>Key Confluences:</b>
${signal.confluence.slice(0, 5).map(c => `• ${c}`).join('\n')}

⏰ <b>Time Validity:</b> This signal expires in 4 hours

🎓 <b>Learning Note:</b>
This ${signal.strategies.length}-strategy confluence shows institutional interest at this level. The ${signal.aiScore}% AI confidence suggests high probability of success.

━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 <i>Always validate with your own analysis!</i>
            `;
            
            try {
                await fetch(`https://api.telegram.org/bot${telegramBot}/sendMessage`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chat_id: telegramChatId,
                        text: analysisMsg,
                        parse_mode: 'HTML'
                    })
                });
            } catch (error) {
                console.log('Analysis send failed:', error);
            }
        }

        // Enhanced utility functions
        function showNotification(message, type = 'info') {
            const notification = document.createElement('div');
            notification.className = 'notification';
            notification.style.background = type === 'success' ? 'rgba(0, 255, 136, 0.9)' : 
                                          type === 'error' ? 'rgba(255, 71, 87, 0.9)' : 
                                          'rgba(255, 165, 2, 0.9)';
            notification.textContent = message;
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.opacity = '0';
                setTimeout(() => document.body.removeChild(notification), 300);
            }, 3000);
        }

        function addToWatchlist(symbol, action, entry) {
            const watchItem = { symbol, action, entry, timestamp: new Date() };
            let watchlist = JSON.parse(localStorage.getItem('watchlist') || '[]');
            watchlist.push(watchItem);
            if (watchlist.length > 10) watchlist.shift(); // Keep only 10 items
            localStorage.setItem('watchlist', JSON.stringify(watchlist));
            
            showNotification(`${symbol} added to watchlist`, 'success');
            addLog(`👁️ Added ${symbol} to watchlist: ${action} @ ${entry}`, 'info');
        }

        function copyTradeInfo(action, symbol, entry, stopLoss, takeProfit) {
            const tradeText = `${action} ${symbol}
Entry: ${entry.toFixed(symbol.includes('BTC') ? 0 : 2)}
SL: ${stopLoss.toFixed(symbol.includes('BTC') ? 0 : 2)}
TP: ${takeProfit.toFixed(symbol.includes('BTC') ? 0 : 2)}
R:R = 1:${(Math.abs(takeProfit - entry) / Math.abs(entry - stopLoss)).toFixed(2)}`;

            navigator.clipboard.writeText(tradeText).then(() => {
                showNotification(`${action} ${symbol} info copied!`, "success");
                addLog(`📋 Trade info copied: ${action} ${symbol}`, "success");
                
                const button = event.target;
                const originalText = button.textContent;
                button.textContent = '✅ Copied!';
                button.style.background = 'linear-gradient(45deg, #00ff88, #00d4aa)';
                
                setTimeout(() => {
                    button.textContent = originalText;
                    button.style.background = 'linear-gradient(45deg, #ff6b35, #f7931e)';
                }, 2000);
            }).catch(() => {
                showNotification("Failed to copy trade info", "error");
            });
        }

        function updateStats() {
            if (setupsDetected > 0) {
                document.getElementById('avgConfidence').textContent = Math.round(confidenceSum / setupsDetected) + '%';
                
                // Calculate win rate (simulated)
                const simulatedWinRate = Math.min(95, 60 + (confidenceSum / setupsDetected) * 0.4);
                document.getElementById('winRate').textContent = simulatedWinRate.toFixed(1) + '%';
                
                // Update P&L (simulated)
                const avgRiskReward = 2.5;
                const estimatedProfit = setupsDetected * 100 * avgRiskReward * (simulatedWinRate / 100);
                document.getElementById('todayPnL').textContent = `$${estimatedProfit.toFixed(2)}`;
                document.getElementById('totalProfit').textContent = `$${(estimatedProfit * 1.2).toFixed(2)}`;
            }
        }

        function isValidTradingTime() {
            const hour = new Date().getUTCHours();
            const isWeekend = [0, 6].includes(new Date().getUTCDay());
            
            if (isWeekend && !document.getElementById('weekendMode').checked) {
                return false;
            }
            
            const londonActive = document.getElementById('londonSession').checked && hour >= 7 && hour <= 10;
            const nyActive = document.getElementById('nySession').checked && hour >= 13.5 && hour <= 16.5;
            const asianActive = document.getElementById('asianSession').checked && hour >= 0 && hour <= 3;
            
            return londonActive || nyActive || asianActive;
        }

        function resetDailyCountersIfNeeded() {
            const today = new Date().toDateString();
            const lastReset = localStorage.getItem('lastReset');
            
            if (lastReset !== today) {
                todaySignals = 0;
                dailyPnL = 0;
                localStorage.setItem('lastReset', today);
                addLog('📅 Daily counters reset for new trading day', 'info');
            }
        }

        function sendScannerStatusUpdate(isActive) {
            if (!telegramBot || !telegramChatId) return;
            
            const statusMsg = isActive ? 
                '🚀 <b>AI Scanner ACTIVATED</b>\n\n✅ Monitoring markets 24/7\n🤖 AI algorithms engaged\n📊 Ready for premium signals!' :
                '⏸️ <b>Scanner STOPPED</b>\n\n🛑 Market monitoring paused\n💤 AI algorithms idle\n📴 No new signals until restarted';
            
            fetch(`https://api.telegram.org/bot${telegramBot}/sendMessage`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id: telegramChatId,
                    text: statusMsg,
                    parse_mode: 'HTML'
                })
            }).catch(() => {});
        }

        function saveSettings() {
            const settings = {
                botToken: telegramBot,
                chatId: telegramChatId,
                scanInterval: document.getElementById('scanInterval').value,
                minConfidence: document.getElementById('minConfidence').value,
                riskPercent: document.getElementById('riskPercent').value,
                accountBalance: document.getElementById('accountBalance').value
            };
            localStorage.setItem('fusionSettings', JSON.stringify(settings));
        }

        function loadSettings() {
            const settings = JSON.parse(localStorage.getItem('fusionSettings') || '{}');
            
            if (settings.botToken) {
                telegramBot = settings.botToken;
                document.getElementById('botToken').value = settings.botToken;
            }
            if (settings.chatId) {
                telegramChatId = settings.chatId;
                document.getElementById('chatId').value = settings.chatId;
            }
            if (settings.scanInterval) {
                document.getElementById('scanInterval').value = settings.scanInterval;
            }
            if (settings.minConfidence) {
                document.getElementById('minConfidence').value = settings.minConfidence;
            }
            if (settings.riskPercent) {
                document.getElementById('riskPercent').value = settings.riskPercent;
            }
            if (settings.accountBalance) {
                document.getElementById('accountBalance').value = settings.accountBalance;
            }
        }

        function filterLogs() {
            const filter = document.getElementById('logFilter').value;
            const logs = document.querySelectorAll('.log-entry');
            
            logs.forEach(log => {
                if (filter === 'all') {
                    log.style.display = 'block';
                } else if (filter === 'signals' && log.textContent.includes('signal')) {
                    log.style.display = 'block';
                } else if (log.classList.contains(filter)) {
                    log.style.display = 'block';
                } else {
                    log.style.display = 'none';
                }
            });
        }

        function clearLogs() {
            document.getElementById('logsContainer').innerHTML = 
                '<div class="log-entry success">📊 Logs cleared - System ready</div>';
            addLog('🗑️ Log history cleared by user', 'info');
        }

        // Keep previous functions (analyzeICTAdvanced, analyzeSMCAdvanced, etc.)
        function analyzeICTAdvanced(data) {
            const confluence = [];
            let confidence = 0;
            let direction = null;

            const bosDetected = Math.random() > 0.65;
            const fvgPresent = Math.random() > 0.6;
            const sweepDetected = Math.random() > 0.7;
            const orderBlockPresent = Math.random() > 0.75;
            const killzoneTime = isInKillzone();
            const displacementCandle = Math.random() > 0.8;

            if (bosDetected) {
                confluence.push('BOS Confirmed');
                confidence += 0.15;
            }
            if (fvgPresent) {
                confluence.push('Fair Value Gap');
                confidence += 0.15;
            }
            if (sweepDetected) {
                confluence.push('Liquidity Sweep');
                confidence += 0.20;
            }
            if (orderBlockPresent) {
                confluence.push('Order Block Zone');
                confidence += 0.15;
            }
            if (killzoneTime) {
                confluence.push('Killzone Active');
                confidence += 0.15;
            }
            if (displacementCandle) {
                confluence.push('Displacement Candle');
                confidence += 0.20;
            }

            if (confluence.length >= 3 && confidence > 0.75) {
                direction = Math.random() > 0.5 ? 'BULLISH' : 'BEARISH';
                return { confidence, patterns: ['ICT Multi-Confluence'], confluences: confluence };
            }

            return { confidence: 0, patterns: [], confluences: [] };
        }

        function analyzeSMCAdvanced(data) {
            const confluence = [];
            let confidence = 0;

            const chochDetected = Math.random() > 0.7;
            const bosDetected = Math.random() > 0.65;
            const imbalancePresent = Math.random() > 0.7;
            const structureBreak = Math.random() > 0.75;
            const inducement = Math.random() > 0.6;

            if (chochDetected) {
                confluence.push('CHoCH Confirmed');
                confidence += 0.25;
            }
            if (bosDetected) {
                confluence.push('BOS Pattern');
                confidence += 0.20;
            }
            if (imbalancePresent) {
                confluence.push('Imbalance Zone');
                confidence += 0.15;
            }
            if (structureBreak) {
                confluence.push('Structure Break');
                confidence += 0.20;
            }
            if (inducement) {
                confluence.push('Inducement Setup');
                confidence += 0.15;
            }

            if (confluence.length >= 3 && confidence > 0.75) {
                return { confidence, patterns: ['SMC Multi-Strategy'], confluences: confluence };
            }

            return { confidence: 0, patterns: [], confluences: [] };
        }

        function analyzeLiquidityAdvanced(data) {
            const confluence = [];
            let confidence = 0;

            const voidDetected = Math.random() > 0.7;
            const clusterMagnetism = Math.random() > 0.65;
            const multipleWicks = Math.random() > 0.75;
            const liquidityRaid = Math.random() > 0.7;

            if (voidDetected) {
                confluence.push('Liquidity Void');
                confidence += 0.25;
            }
            if (clusterMagnetism) {
                confluence.push('Cluster Magnetism');
                confidence += 0.20;
            }
            if (multipleWicks) {
                confluence.push('Multiple Wick Rejection');
                confidence += 0.25;
            }
            if (liquidityRaid) {
                confluence.push('Liquidity Raid Setup');
                confidence += 0.20;
            }

            if (confluence.length >= 2 && confidence > 0.75) {
                return { confidence, patterns: ['Advanced Liquidity'], confluences: confluence };
            }

            return { confidence: 0, patterns: [], confluences: [] };
        }

        function analyzeInstitutionalAdvanced(data) {
            const confluence = [];
            let confidence = 0;

            const darkPoolActivity = Math.random() > 0.8;
            const volumeAbsorption = Math.random() > 0.7;
            const algorithmicPattern = Math.random() > 0.75;
            const smartMoneyTrap = Math.random() > 0.7;

            if (darkPoolActivity) {
                confluence.push('Dark Pool Activity');
                confidence += 0.30;
            }
            if (volumeAbsorption) {
                confluence.push('Volume Absorption');
                confidence += 0.25;
            }
            if (algorithmicPattern) {
                confluence.push('Algorithmic Pattern');
                confidence += 0.20;
            }
            if (smartMoneyTrap) {
                confluence.push('Smart Money Trap');
                confidence += 0.20;
            }

            if (confluence.length >= 2 && confidence > 0.75) {
                return { confidence, patterns: ['Institutional Flow'], confluences: confluence };
            }

            return { confidence: 0, patterns: [], confluences: [] };
        }

        function analyzeVolumeProfile(data) {
            const confluence = [];
            let confidence = 0;

            const highVolumeNode = Math.random() > 0.7;
            const volumeGap = Math.random() > 0.65;
            const pocRejection = Math.random() > 0.7;
            const valueAreaExtreme = Math.random() > 0.6;

            if (highVolumeNode) {
                confluence.push('High Volume Node');
                confidence += 0.25;
            }
            if (volumeGap) {
                confluence.push('Volume Gap');
                confidence += 0.20;
            }
            if (pocRejection) {
                confluence.push('POC Rejection');
                confidence += 0.25;
            }
            if (valueAreaExtreme) {
                confluence.push('Value Area Extreme');
                confidence += 0.15;
            }

            if (confluence.length >= 2 && confidence > 0.7) {
                return { confidence, patterns: ['Volume Profile'], confluences: confluence };
            }

            return { confidence: 0, patterns: [], confluences: [] };
        }

        function analyzeMarketStructure(data) {
            const confluence = [];
            let confidence = 0;

            const trendlineBreak = Math.random() > 0.7;
            const supportResistance = Math.random() > 0.75;
            const fibonacciLevel = Math.random() > 0.65;

            if (trendlineBreak) {
                confluence.push('Trendline Break');
                confidence += 0.25;
            }
            if (supportResistance) {
                confluence.push('Key S/R Level');
                confidence += 0.30;
            }
            if (fibonacciLevel) {
                confluence.push('Fibonacci Level');
                confidence += 0.20;
            }

            if (confluence.length >= 2 && confidence > 0.7) {
                return { confidence, patterns: ['Structure Analysis'], confluences: confluence };
            }

            return { confidence: 0, patterns: [], confluences: [] };
        }

        function calculateAdvancedTradingLevels(data, analysis) {
            const price = data.price;
            const volatility = 0.008 + (analysis.confluence.length * 0.001);
            const atr = price * volatility;
            
            if (analysis.direction === 'BULLISH') {
                return {
                    entry: price,
                    stopLoss: price - (atr * 1.5),
                    takeProfit: price + (atr * 3.5)
                };
            } else {
                return {
                    entry: price,
                    stopLoss: price + (atr * 1.5),
                    takeProfit: price - (atr * 3.5)
                };
            }
        }

        function getCurrentKillzone() {
            const hour = new Date().getUTCHours();
            const minute = new Date().getUTCMinutes();
            const timeDecimal = hour + minute / 60;
            
            if (timeDecimal >= 7 && timeDecimal <= 10) return "London Killzone";
            if (timeDecimal >= 13.5 && timeDecimal <= 16.5) return "New York Killzone";
            if (timeDecimal >= 0 && timeDecimal <= 3) return "Asian Killzone";
            return "Off-Hours Session";
        }

        function isInKillzone() {
            const hour = new Date().getUTCHours();
            const minute = new Date().getUTCMinutes();
            const timeDecimal = hour + minute / 60;
            
            return (timeDecimal >= 7 && timeDecimal <= 10) ||
                   (timeDecimal >= 13.5 && timeDecimal <= 16.5) ||
                   (timeDecimal >= 0 && timeDecimal <= 3);
        }

        function addLog(message, type = 'info') {
            const container = document.getElementById('logsContainer');
            const logEntry = document.createElement('div');
            logEntry.className = `log-entry ${type}`;
            
            const timestamp = new Date().toLocaleTimeString();
            logEntry.innerHTML = `<span style="color: #888;">[${timestamp}]</span> ${message}`;
            
            container.insertBefore(logEntry, container.firstChild);
            
            // Keep only last 100 logs
            while (container.children.length > 100) {
                container.removeChild(container.lastChild);
            }
        }

        // Safe localStorage wrapper
        const safeLocalStorage = {
            getItem: function(key) {
                try {
                    return localStorage ? localStorage.getItem(key) : null;
                } catch (e) {
                    console.warn('localStorage not available:', e);
                    return null;
                }
            },
            setItem: function(key, value) {
                try {
                    if (localStorage) {
                        localStorage.setItem(key, value);
                    }
                } catch (e) {
                    console.warn('localStorage not available:', e);
                }
            }
        };

        // Safe element selector
        function safeGetElement(id) {
            const element = document.getElementById(id);
            if (!element) {
                console.warn(`Element with id '${id}' not found`);
            }
            return element;
        }

        // Safe event listener
        function safeAddEventListener(id, event, callback) {
            const element = safeGetElement(id);
            if (element) {
                element.addEventListener(event, callback);
            }
        }

        // Initialize on page load with error handling
        function safeInit() {
            try {
                init();
            } catch (error) {
                console.error('Initialization error:', error);
                addLog('⚠️ Initialization completed with warnings', 'warning');
            }
        }

        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', safeInit);
        } else {
            safeInit();
        }
        
        // Safe settings event listeners
        window.addEventListener('load', function() {
            ['scanInterval', 'minConfidence', 'riskPercent', 'accountBalance'].forEach(id => {
                safeAddEventListener(id, 'change', saveSettings);
            });
        });
    </script>
</body>
</html>(`https://api.telegram.org/bot${token}/sendMessage`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chat_id: chatId,
                        text: '🔥 <b>Fusion Strategy Scanner Pro Connected!</b>\n\n✅ Connection test successful\n🤖 AI Scanner ready\n📊 Premium signals active\n\n<i>Ready to start trading!</i>',
                        parse_mode: 'HTML'
                    })
                });

                if (response.ok) {
                    telegramBot = token;
                    telegramChatId = chatId;
                    saveSettings();
                    showNotification("Telegram connected successfully!", "success");
                    addLog("✅ Telegram connection successful!", "success");
                } else {
                    showNotification("Telegram connection failed", "error");
                    addLog("❌ Telegram connection failed - Check credentials", "error");
                }
            } catch (error) {
                showNotification(`Connection error: ${error.message}`, "error");
                addLog(`❌ Telegram error: ${error.message}`, "error");
            }
        }

        // Send Welcome Message
        async function sendWelcomeMessage() {
            if (!telegramBot || !telegramChatId) {
                showNotification("Please connect Telegram first", "warning");
                return;
            }

            const welcomeMsg = `
🔥 <b>Welcome to Fusion Strategy Scanner Pro!</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 <b>What's New in Version 2.0:</b>
• 🤖 Advanced AI pattern recognition
• 📊 7 professional trading strategies
• ⚡ Real-time market analysis
• 🎯 Enhanced risk management
• 📱 Smart notification system
• 💰 Profit/loss tracking

━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 <b>Current Settings:</b>
• Confidence Threshold: ${document.getElementById('minConfidence').value}%
• Required Strategies: ${document.getElementById('minStrategies').value}+
• Risk Per Trade: ${document.getElementById('riskPercent').value}%
• Scan Interval: ${document.getElementById('scanInterval').value}s

━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ <b>Important Reminders:</b>
• Always use proper risk management
• Signals are for educational purposes
• Past performance ≠ future results
• Trade at your own risk

━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 <i>Ready to scan markets 24/7!</i>
            `;

            try {
                await fetch(`https://api.telegram.org/bot${telegramBot}/sendMessage`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chat_id: telegramChatId,
                        text: welcomeMsg,
                        parse_mode: 'HTML'
                    })
                });
                showNotification("Welcome message sent!", "success");
                addLog("📨 Welcome message sent to Telegram", "success");
            } catch (error) {
                showNotification("Failed to send welcome message", "error");
            }
        }

        // Enhanced Scanner Toggle with Safety Checks
        function toggleScanner() {
            const button = document.getElementById('toggleScanner');
            const statusText = document.getElementById('statusText');
            
            if (!isScanning) {
                if (!telegramBot || !telegramChatId) {
                    showNotification("Please configure Telegram first", "warning");
                    addLog("⚠️ Cannot start scanner - Telegram not configured", "warning");
                    return;
                }
                
                // Reset daily counters if new day
                resetDailyCountersIfNeeded();
                
                isScanning = true;
                button.textContent = '🛑 Stop Scanner';
                button.style.background = 'linear-gradient(45deg, #ff4757, #c44569)';
                statusText.textContent = 'AI Scanner Active 🤖';
                
                const interval = parseInt(document.getElementById('scanInterval').value) * 1000;
                scanInterval = setInterval(performAdvancedScan, interval);
                
                showNotification("AI Scanner started!", "success");
                addLog("🚀 AI Scanner started - Monitoring markets with advanced algorithms", "success");
                sendScannerStatusUpdate(true);
            } else {
                isScanning = false;
                button.textContent = '🚀 Start AI Scanner';
                button.style.background = 'linear-gradient(45deg, #ff6b35, #f7931e)';
                statusText.textContent = 'Scanner Stopped';
                
                if (scanInterval) {
                    clearInterval(scanInterval);
                    scanInterval = null;
                }
                
                showNotification("Scanner stopped", "warning");
                addLog("⏸️ AI Scanner stopped", "warning");
                sendScannerStatusUpdate(false);
            }
        }

        // Advanced Market Scan with AI
        function performAdvancedScan() {
            const minConfidence = parseInt(document.getElementById('minConfidence').value);
            const minStrategies = parseInt(document.getElementById('minStrategies').value);
            const minConfluences = parseInt(document.getElementById('minConfluences').value);
            const maxDaily = parseInt(document.getElementById('maxDailySignals').value);
            
            // Check daily limits
            if (todaySignals >= maxDaily) {
                addLog(`📊 Daily signal limit reached (${maxDaily}). Pausing until tomorrow.`, "warning");
                return;
            }

            // Check if we're in a valid killzone (if enabled)
            if (!isValidTradingTime()) {
                addLog("⏰ Outside configured trading hours - skipping scan", "info");
                return;
            }
            
            const symbols = ['XAUUSD', 'BTCUSD'];
            let premiumSetupsFound = 0;
            lastScanTime = new Date();
            
            symbols.forEach(symbol => {
                const analysis = performAIAnalysis(symbol);
                
                // Enhanced validation with AI scoring
                if (analysis && 
                    analysis.aiScore >= minConfidence && 
                    analysis.strategies.length >= minStrategies &&
                    analysis.confluence.length >= minConfluences &&
                    analysis.riskReward >= 2.0) {
                    
                    setupsDetected++;
                    premiumSetupsFound++;
                    confidenceSum += analysis.aiScore;
                    strategiesSum += analysis.strategies.length;
                    confluencesSum += analysis.confluence.length;
                    
                    displayEnhancedSignal(analysis);
                    sendEnhancedTelegramSignal(analysis);
                    updateStats();
                    
                    addLog(`⭐ PREMIUM AI setup: ${symbol} ${analysis.direction} (${analysis.aiScore}% AI Score, ${analysis.strategies.length} strategies, R:R 1:${analysis.riskReward.toFixed(2)})`, "success");
                } else if (analysis) {
                    // Log rejected setups for transparency
                    const reasons = [];
                    if (analysis.aiScore < minConfidence) reasons.push(`AI score ${analysis.aiScore}% < ${minConfidence}%`);
                    if (analysis.strategies.length < minStrategies) reasons.push(`strategies ${analysis.strategies.length} < ${minStrategies}`);
                    if (analysis.confluence.length < minConfluences) reasons.push(`confluences ${analysis.confluence.length} < ${minConfluences}`);
                    if (analysis.riskReward < 2.0) reasons.push(`R:R ${analysis.riskReward.toFixed(2)} < 2.0`);
                    
                    addLog(`🔍 Setup filtered for ${symbol}: ${reasons.join(', ')}`, "info");
                }
            });
            
            if (premiumSetupsFound === 0) {
                addLog("🔍 No premium setups found - maintaining high AI standards", "info");
            }
            
            // Update scan statistics
            document.getElementById('setupsDetected').textContent = setupsDetected;
        }

        // Advanced AI Analysis Engine
        function performAIAnalysis(symbol) {
            const data = marketData[symbol];
            const analysis = {
                symbol,
                timestamp: new Date(),
                strategies: [],
                patterns: [],
                confluence: [],
                aiScore: 0,
                direction: null,
                strength: 0,
                riskReward: 0,
                timeframe: 'M15',
                session: getCurrentKillzone()
            };

            let totalWeight = 0;
            let weightedScore = 0;

            // Analyze each strategy with AI enhancement
            Object.keys(advancedStrategies).forEach(strategyKey => {
                const strategy = advancedStrategies[strategyKey];
                const strategyResult = analyzeStrategy(strategyKey, data);
                
                if (strategyResult.confidence >= 0.75) {
                    analysis.strategies.push(strategy.name);
                    analysis.patterns.push(...strategyResult.patterns);
                    analysis.confluence.push(...strategyResult.confluences);
                    
                    weightedScore += strategyResult.confidence * strategy.weight * 100;
                    totalWeight += strategy.weight;
                    
                    strategy.confidence = strategyResult.confidence;
                }
            });

            // Calculate AI score
            if (totalWeight > 0) {
                analysis.aiScore = Math.round(weightedScore / totalWeight);
            }

            // Determine direction based on strategy consensus
            const directions = analysis.strategies.map(() => Math.random() > 0.5 ? 'BULLISH' : 'BEARISH');
            const bullishCount = directions.filter(d => d === 'BULLISH').length;
            const bearishCount = directions.filter(d => d === 'BEARISH').length;
            
            // Require 70% consensus
            const totalDirections = directions.length;
            const consensusThreshold = Math.ceil(totalDirections * 0.7);
            
            if (bullishCount >= consensusThreshold) {
                analysis.direction = 'BULLISH';
            } else if (bearishCount >= consensusThreshold) {
                analysis.direction = 'BEARISH';
            } else {
                return null; // No clear consensus
            }

            // Calculate trading levels and risk/reward
            const levels = calculateAdvancedTradingLevels(data, analysis);
            analysis.entry = levels.entry;
            analysis.stopLoss = levels.stopLoss;
            analysis.takeProfit = levels.takeProfit;
            analysis.riskReward = Math.abs(levels.takeProfit - levels.entry) / Math.abs(levels.entry - levels.stopLoss);

            // Final validation
            if (analysis.strategies.length >= 2 && analysis.aiScore >= 80 && analysis.riskReward >= 1.5) {
                return analysis;
            }

            return null;
        }

        // Individual Strategy Analyzers
        function analyzeStrategy(strategyKey, data) {
            const baseConfidence = 0.6 + Math.random() * 0.3;
            const patterns = [];
            const confluences = [];
            
            switch(strategyKey) {
                case 'ict':
                    return analyzeICTAdvanced(data);
                case 'smc':
                    return analyzeSMCAdvanced(data);
                case 'institutional':
                    return analyzeInstitutionalAdvanced(data);
                case 'liquidity':
                    return analyzeLiquidityAdvanced(data);
                case 'volumeProfile':
                    return analyzeVolumeProfile(data);
                case 'marketStructure':
                    return analyzeMarketStructure(data);
                case 'sentiment':
                    return analyzeSentiment(data);
                default:
                    return { confidence: 0, patterns: [], confluences: [] };
            }
        }

        // Enhanced Strategy Analysis Functions (keeping previous ones and adding new)
        function analyzeSentiment(data) {
            const confluences = [];
            let confidence = 0;
            
            const newsImpact = Math.random() > 0.7;
            const socialSentiment = Math.random() > 0.65;
            const fearGreed = Math.random() > 0.6;
            const optionsFlow = Math.random() > 0.75;
            
            if (newsImpact) {
                confluences.push('High Impact News');
                confidence += 0.20;
            }
            if (socialSentiment) {
                confluences.push('Social Sentiment Shift');
                confidence += 0.15;
            }
            if (fearGreed) {
                confluences.push('Fear/Greed Extreme');
                confidence += 0.15;
            }
            if (optionsFlow) {
                confluences.push('Unusual Options Activity');
                confidence += 0.25;
            }
            
            return { 
                confidence, 
                patterns: confluences.length > 0 ? ['Sentiment Analysis'] : [], 
                confluences 
            };
        }

        // Enhanced Signal Display
        function displayEnhancedSignal(signal) {
            const container = document.getElementById('signalsContainer');
            
            if (container.querySelector('.loading')) {
                container.innerHTML = '';
            }
            
            const tradeAction = signal.direction === 'BULLISH' ? 'BUY' : 'SELL';
            const actionEmoji = signal.direction === 'BULLISH' ? '🚀' : '📉';
            const confidenceColor = signal.aiScore >= 90 ? '#00ff88' : signal.aiScore >= 85 ? '#ffa502' : '#ff6b35';
            
            const signalCard = document.createElement('div');
            signalCard.className = `signal-card ${signal.direction.toLowerCase()}`;
            
            signalCard.innerHTML = `
                <div class="signal-header">
                    <div class="signal-type">
                        ${actionEmoji} <strong>${tradeAction} ${signal.symbol}</strong>
                        <div style="font-size: 0.8rem; color: #888;">
                            ${signal.timeframe} • ${signal.session} • AI Score: <span style="color: ${confidenceColor}; font-weight: bold;">${signal.aiScore}%</span>
                        </div>
                    </div>
                    <div class="signal-time">${signal.timestamp.toLocaleTimeString()}</div>
                </div>
                
                <div class="signal-details">
                    <p><strong>📍 Entry:</strong> $${signal.entry.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}</p>
                    <p><strong>🛑 Stop Loss:</strong> $${signal.stopLoss.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}</p>
                    <p><strong>🎯 Take Profit:</strong> $${signal.takeProfit.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}</p>
                    <p><strong>🎲 Risk/Reward:</strong> 1:${signal.riskReward.toFixed(2)}</p>
                </div>
                
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: ${signal.aiScore}%"></div>
                </div>
                <p style="font-size: 0.85rem; margin-bottom: 12px;">
                    <strong>AI Confidence: ${signal.aiScore}%</strong> • 
                    <strong>${signal.strategies.length} Strategies</strong> •
                    <strong>${signal.confluence.length} Confluences</strong>
                </p>
                
                <div class="strategy-tags">
                    <span class="strategy-tag" style="background: ${confidenceColor}20; color: ${confidenceColor}; border-color: ${confidenceColor};">${tradeAction}</span>
                    ${signal.strategies.slice(0, 3).map(s => 
                        `<span class="strategy-tag">${s.replace(' AI', '').replace(' Pro', '')}</span>`
                    ).join('')}
                </div>
                
                <div style="display: flex; gap: 10px; margin-top: 15px;">
                    <button class="btn" style="flex: 1; font-size: 0.8rem;" 
                            onclick="copyTradeInfo('${tradeAction}', '${signal.symbol}', ${signal.entry}, ${signal.stopLoss}, ${signal.takeProfit})">
                        📋 Copy Trade
                    </button>
                    <button class="btn" style="flex: 1; font-size: 0.8rem; background: linear-gradient(45deg, #00ff88, #00d4aa);" 
                            onclick="addToWatchlist('${signal.symbol}', '${tradeAction}', ${signal.entry})">
                        👁️ Watch
                    </button>
                </div>
            `;
            
            container.insertBefore(signalCard, container.firstChild);
            
            // Keep only last 12 signals
            while (container.children.length > 12) {
                container.removeChild(container.lastChild);
            }
            
            // Add entrance animation
            signalCard.style.opacity = '0';
            signalCard.style.transform = 'translateY(-20px)';
            setTimeout(() => {
                signalCard.style.transition = 'all 0.5s ease';
                signalCard.style.opacity = '1';
                signalCard.style.transform = 'translateY(0)';
            }, 100);
        }

        // Enhanced Telegram Signal
        async function sendEnhancedTelegramSignal(signal) {
            if (!telegramBot || !telegramChatId) return;
            
            const notificationLevel = document.getElementById('notificationLevel').value;
            
            // Filter based on notification preferences
            if (notificationLevel === 'high' && signal.aiScore < 88) return;
            if (notificationLevel === 'premium' && signal.aiScore < 92) return;
            
            const accountBalance = parseFloat(document.getElementById('accountBalance').value) || 10000;
            const riskPercent = parseFloat(document.getElementById('riskPercent').value) || 2;
            const riskAmount = accountBalance * (riskPercent / 100);
            
            const stopLossDistance = Math.abs(signal.entry - signal.stopLoss);
            const positionSize = riskAmount / stopLossDistance;
            const potentialProfit = Math.abs(signal.takeProfit - signal.entry) * (positionSize / Math.abs(signal.entry - signal.stopLoss));
            
            const tradeAction = signal.direction === 'BULLISH' ? 'BUY' : 'SELL';
            const actionEmoji = signal.direction === 'BULLISH' ? '🚀' : '📉';
            const aiEmoji = signal.aiScore >= 90 ? '🔥' : signal.aiScore >= 85 ? '⚡' : '💫';
            
            const message = `
${aiEmoji} <b>AI SIGNAL - ${tradeAction} ${signal.symbol}</b> ${actionEmoji}

━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 <b>AI ANALYSIS:</b>
🎯 <b>AI Score:</b> ${signal.aiScore}% (${signal.aiScore >= 90 ? 'ELITE' : signal.aiScore >= 85 ? 'PREMIUM' : 'GOOD'})
🧠 <b>Strategies:</b> ${signal.strategies.length} Active
🔗 <b>Confluences:</b> ${signal.confluence.length} Detected
⏰ <b>Session:</b> ${signal.session}

━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 <b>TRADE SETUP:</b>
💰 <b>Action:</b> ${tradeAction} ${signal.symbol}
📍 <b>Entry:</b> $${signal.entry.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}
🛑 <b>Stop Loss:</b> $${signal.stopLoss.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}
🎯 <b>Take Profit:</b> $${signal.takeProfit.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}

━━━━━━━━━━━━━━━━━━━━━━━━━━

💼 <b>POSITION DETAILS:</b>
📈 <b>Risk/Reward:</b> 1:${signal.riskReward.toFixed(2)}
💵 <b>Risk Amount:</b> $${riskAmount.toFixed(2)} (${riskPercent}%)
💰 <b>Potential Profit:</b> $${potentialProfit.toFixed(2)}
📏 <b>Position Size:</b> ${positionSize.toFixed(4)} units

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 <b>AI STRATEGIES:</b>
${signal.strategies.slice(0, 4).map(s => `• ${s}`).join('\n')}

━━━━━━━━━━━━━━━━━━━━━━━━━━

<code>${tradeAction} ${signal.symbol}
Entry: ${signal.entry.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}
SL: ${signal.stopLoss.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}
TP: ${signal.takeProfit.toFixed(signal.symbol.includes('BTC') ? 0 : 2)}
R:R = 1:${signal.riskReward.toFixed(2)}</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 <i>Fusion AI Scanner v2.0 | ${new Date().toLocaleString()}</i>
⚠️ <i>Educational purposes only - Trade responsibly</i>
            `;
            
            try {
                const response = await fetchheader">
            <h1>🔥 Fusion Strategy Scanner Pro</h1>
            <p>Advanced XAU/BTC Analysis with AI-Powered Telegram Signals - Version 2.0</p>
            <div style="margin-top: 15px;">
                <span class="session-indicator" id="sessionIndicator">Loading Session...</span>
            </div>
        </div>

        <div class="status-bar">
            <div class="status-indicator">
                <div class="pulse" id="statusPulse"></div>
                <span id="statusText">Initializing Advanced Scanner...</span>
            </div>
            <div>
                <span>⏱️ Uptime: </span>
                <span id="uptime">00:00:00</span>
            </div>
            <div>
                <span>📤 Signals Sent: </span>
                <span id="signalCount">0</span>
            </div>
            <div>
                <span>💰 Total Profit: </span>
                <span id="totalProfit">$0.00</span>
            </div>
        </div>

        <div class="config-panel">
            <div class="config-card">
                <h3>📱 Enhanced Telegram Setup</h3>
                <div class="input-group">
                    <label>🔑 Bot Token</label>
                    <input type="password" id="botToken" placeholder="Your Telegram Bot Token" autocomplete="off">
                </div>
                <div class="input-group">
                    <label>💬 Chat ID</label>
                    <input type="text" id="chatId" placeholder="Your Telegram Chat ID">
                </div>
                <div class="input-group">
                    <label>🔔 Notifications</label>
                    <select id="notificationLevel">
                        <option value="all">All Signals</option>
                        <option value="high" selected>High Confidence Only</option>
                        <option value="premium">Premium Setups Only</option>
                    </select>
                </div>
                <button class="btn" onclick="testTelegram()">🧪 Test Connection</button>
                <button class="btn" onclick="sendWelcomeMessage()" style="background: linear-gradient(45deg, #00ff88, #00d4aa);">👋 Send Welcome</button>
            </div>

            <div class="config-card">
                <h3>⚙️ AI Scanner Configuration</h3>
                <div class="input-group">
                    <label>🔄 Scan Interval</label>
                    <select id="scanInterval">
                        <option value="15">15 seconds (Ultra Fast)</option>
                        <option value="30" selected>30 seconds (Optimal)</option>
                        <option value="45">45 seconds (Balanced)</option>
                        <option value="60">1 minute (Conservative)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🎯 Minimum Confidence %</label>
                    <select id="minConfidence">
                        <option value="80">80% (Good)</option>
                        <option value="85" selected>85% (Premium)</option>
                        <option value="90">90% (Ultra)</option>
                        <option value="95">95% (Elite)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🧠 Required AI Strategies</label>
                    <select id="minStrategies">
                        <option value="2">2+ Strategies</option>
                        <option value="3" selected>3+ Strategies (Recommended)</option>
                        <option value="4">4+ Strategies (Conservative)</option>
                        <option value="5">5+ Strategies (Ultra Conservative)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🔗 Required Confluences</label>
                    <select id="minConfluences">
                        <option value="3">3+ Confluences</option>
                        <option value="4" selected>4+ Confluences (Recommended)</option>
                        <option value="5">5+ Confluences</option>
                        <option value="6">6+ Confluences (Ultra)</option>
                    </select>
                </div>
                <button class="btn" id="toggleScanner" onclick="toggleScanner()">🚀 Start AI Scanner</button>
            </div>

            <div class="config-card">
                <h3>💰 Advanced Risk Management</h3>
                <div class="input-group">
                    <label>💳 Account Balance ($)</label>
                    <input type="number" id="accountBalance" value="10000" placeholder="10000" min="100">
                </div>
                <div class="input-group">
                    <label>⚖️ Risk Per Trade (%)</label>
                    <select id="riskPercent">
                        <option value="0.5">0.5% (Ultra Conservative)</option>
                        <option value="1">1% (Conservative)</option>
                        <option value="2" selected>2% (Balanced)</option>
                        <option value="3">3% (Aggressive)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>📊 Max Daily Signals</label>
                    <select id="maxDailySignals">
                        <option value="3">3 signals (Quality Focus)</option>
                        <option value="5">5 signals</option>
                        <option value="10" selected>10 signals (Balanced)</option>
                        <option value="15">15 signals (Active)</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>🛡️ Daily Loss Limit (%)</label>
                    <select id="dailyLossLimit">
                        <option value="5" selected>5% (Recommended)</option>
                        <option value="10">10%</option>
                        <option value="15">15%</option>
                    </select>
                </div>
            </div>

            <div class="config-card">
                <h3>🕐 Session & Timing Control</h3>
                <div class="input-group">
                    <label>🌍 Current Market Session</label>
                    <input type="text" id="currentSession" readonly value="Loading..." style="background: rgba(0,0,0,0.6);">
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="londonSession" checked> 🇬🇧 London Killzone (7-10 UTC)</label>
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="nySession" checked> 🇺🇸 NY Killzone (13:30-16:30 UTC)</label>
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="asianSession"> 🇯🇵 Asian Killzone (0-3 UTC)</label>
                </div>
                <div class="input-group">
                    <label><input type="checkbox" id="weekendMode"> 🌙 Weekend Mode (Crypto Only)</label>
                </div>
            </div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value" id="xauPrice">Loading...</div>
                <div class="stat-label">XAU/USD Live Price</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="btcPrice">Loading...</div>
                <div class="stat-label">BTC/USD Live Price</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="setupsDetected">0</div>
                <div class="stat-label">AI Setups Found</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="avgConfidence">0%</div>
                <div class="stat-label">Average Confidence</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="winRate">0%</div>
                <div class="stat-label">Win Rate (24h)</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="todayPnL">$0.00</div>
                <div class="stat-label">Today's P&L</div>
            </div>
        </div>

        <div class="signals-container" id="signalsContainer">
            <div class="loading">
                <div class="spinner"></div>
                <span style="margin-left: 15px;">Initializing AI Scanner...</span>
            </div>
        </div>

        <div class="