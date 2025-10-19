```json
{
  "id": "4a0d0de5a9d18a14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286702,
  "host_pid": "9e6742732c60:1",
  "hash": "3c2c97264264a63d42e2e5dcf0422c29821e6a8037b0f8ce337b9b9b5a34d5a4",
  "cid": "QmV13c2c97264264a63d42e2e5dcf0422c29821e6a80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286702,
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
      "evaluated_at": 1760286702
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "6072aa39efe0d13b54dbed17ed8e95055b1d8a3043b1c58fe3f40091ef05e18a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14651518, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}