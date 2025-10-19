```json
{
  "id": "660200f8a69abfa5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287433,
  "host_pid": "9e6742732c60:1",
  "hash": "8dd926da367fe233b0fb042a8c47b437b734c8fb51aba780956c54bc19010752",
  "cid": "QmV18dd926da367fe233b0fb042a8c47b437b734c8fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287433,
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
      "evaluated_at": 1760287433
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
  "sig": "c4b78fbcedf1c906eab30f72a3fd8883345036324ef8e0d86cb5a5a8efa46ecc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000034782199
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285763, 'matching_hash': '89ad1f50f76a063c'}}}een': 1760285764, 'matching_hash': '7eb9a0fe320f28ac'}}}