```json
{
  "id": "89ee7351936eaa06",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293050,
  "host_pid": "9e6742732c60:1",
  "hash": "6c5405d077c88c206767356d8262ff538e236ca6cd38e9e97c8224bd80a2962c",
  "cid": "QmV16c5405d077c88c206767356d8262ff538e236ca6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293050,
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
      "evaluated_at": 1760293050
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
  "sig": "5ef64e45a1e8608253728e0687fa867b4301b1623a8d43f58cb985a9a509eb9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153937190
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 101789730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': '8cf441fb6328957e'}}}