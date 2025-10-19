```json
{
  "id": "37052289371497d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292011,
  "host_pid": "9e6742732c60:1",
  "hash": "8f957ef6371392461fa0353c9b8536ffa7c2ae4a50621e70138f947a8c0d69bd",
  "cid": "QmV18f957ef6371392461fa0353c9b8536ffa7c2ae4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292011,
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
      "evaluated_at": 1760292011
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
  "sig": "47e1bfa7dea390567a660bbe995227d2eb72a79e56c6ec7dfa2fa0fc0aae4b17"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028475138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 62491200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': 'fd3dd6a8db70ef91'}}}