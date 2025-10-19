```json
{
  "id": "36b82fee0d9fb122",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285897,
  "host_pid": "9e6742732c60:1",
  "hash": "dc6a39a837b5c766a27f325d21eb1ef4af0774f68ce67d71eaaa72201fc5ac15",
  "cid": "QmV1dc6a39a837b5c766a27f325d21eb1ef4af0774f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285897,
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
      "evaluated_at": 1760285897
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
  "sig": "2e7c7ab3e617f2019fbe0f06601318f0d93d9608f75a0ef973e5da47d9b51f61"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009597421131
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285765, 'matching_hash': 'ee859bd02c19b1f0'}}}