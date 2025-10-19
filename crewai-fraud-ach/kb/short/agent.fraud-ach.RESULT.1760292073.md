```json
{
  "id": "c48847199eacab08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292073,
  "host_pid": "9e6742732c60:1",
  "hash": "e288131e8fe945565de24f06c60ee2df8f3504ca5e4756e913fa790f008d96ff",
  "cid": "QmV1e288131e8fe945565de24f06c60ee2df8f3504ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292073,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760292073
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "9725efee69fc92cccea8bbfcdd437665a79de50bd8a3527aa2fd3b37a52af0a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 60148872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}