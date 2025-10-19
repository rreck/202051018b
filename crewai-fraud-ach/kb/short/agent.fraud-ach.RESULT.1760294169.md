```json
{
  "id": "aba9b818aecac9c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294169,
  "host_pid": "9e6742732c60:1",
  "hash": "57310c2b258337047b9c3b815696dcfb56886632c972cfb75306265c4101476c",
  "cid": "QmV157310c2b258337047b9c3b815696dcfb56886632",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294169,
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
      "evaluated_at": 1760294169
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
  "sig": "77d98be8734f8fd63a8395c99efd617f3b4390cb79089cce89c4afef03da28f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032979175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 76325674, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '92afbef802abc12c'}}}