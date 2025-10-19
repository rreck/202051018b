```json
{
  "id": "8399a875cc11d5f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292710,
  "host_pid": "9e6742732c60:1",
  "hash": "07a1e4b62896871ed7ce17ae4ef24f25c04e7ceec7f63876f4c6bc9f2f7574b1",
  "cid": "QmV107a1e4b62896871ed7ce17ae4ef24f25c04e7cee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292710,
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
      "evaluated_at": 1760292710
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
  "sig": "ed37f5e4a370d39ff8c9f6b06577850e90da4d2b3ecced40f1207fee15b8ee93"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029513246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 10282356, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285764, 'matching_hash': '556e5d87a3998e0a'}}}