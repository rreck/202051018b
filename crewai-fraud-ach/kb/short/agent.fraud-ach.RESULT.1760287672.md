```json
{
  "id": "535a626f040e5107",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287672,
  "host_pid": "9e6742732c60:1",
  "hash": "accc26d9e426fd08c06fc87598c46ea063df8066a59292e92e68d3286cafaffb",
  "cid": "QmV1accc26d9e426fd08c06fc87598c46ea063df8066",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287672,
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
      "evaluated_at": 1760287672
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
  "sig": "c75fa9a8cb00fdeae0d6cf9e9b983e8f8c04d66b8f4038acf3312dcb7477efc8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105152922139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 13598096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '36c7f170a3aff02c'}}}