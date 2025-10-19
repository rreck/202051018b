```json
{
  "id": "30b3033680b846b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292617,
  "host_pid": "9e6742732c60:1",
  "hash": "d45a5119a418b14e0867f36ae0e4f2ac9524f7d2a97991136916a6ff30a85ed5",
  "cid": "QmV1d45a5119a418b14e0867f36ae0e4f2ac9524f7d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292617,
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
      "evaluated_at": 1760292617
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
  "sig": "a5a1031c619363f6c8be8984ecc90e71ec8eff236b45f3a55c725859aad78068"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 11481924, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}