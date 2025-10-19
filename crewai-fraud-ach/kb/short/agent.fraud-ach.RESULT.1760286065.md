```json
{
  "id": "c095100323dd3611",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286065,
  "host_pid": "9e6742732c60:1",
  "hash": "91c2ede2ac9a441d51bf1e2f6ad2981574b4dad8c7c72b900300c404287fc9db",
  "cid": "QmV191c2ede2ac9a441d51bf1e2f6ad2981574b4dad8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286065,
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
      "evaluated_at": 1760286065
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
  "sig": "854412bdc90e3fd30de9f5030417e16aeafbdefa26044a8fb8dc5119ae273564"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249454336
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': '6b4cd9d1923f5d4e'}}}