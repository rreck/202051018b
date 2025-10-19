```json
{
  "id": "e3dba2db16d2b74b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289364,
  "host_pid": "9e6742732c60:1",
  "hash": "53d6b5b5a4580b27b1d26016093f46f9ff33a461b01dcccc9c7e350b70bfa1a0",
  "cid": "QmV153d6b5b5a4580b27b1d26016093f46f9ff33a461",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289364,
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
      "evaluated_at": 1760289364
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
  "sig": "0a1aa42caa64b57ad1eb3f06dc47306fc034584ccf4fa572b86b5bc5351ba388"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274458495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 55201289, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285764, 'matching_hash': '191d9163e8e6657e'}}}