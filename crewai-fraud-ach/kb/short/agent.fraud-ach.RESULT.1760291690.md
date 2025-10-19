```json
{
  "id": "46d6e289a5f54394",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291690,
  "host_pid": "9e6742732c60:1",
  "hash": "54d661e60a8b0ebbee75e2c10e0c0cbc3a4abc3283a066bd982339be27d42c58",
  "cid": "QmV154d661e60a8b0ebbee75e2c10e0c0cbc3a4abc32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291690,
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
      "evaluated_at": 1760291690
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
  "sig": "e8f5e3a880007819f859321231c72f8613848e7378bf0ba4b9e2052380d44799"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023218255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '1151ecc015fd8f1a'}}}een': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}