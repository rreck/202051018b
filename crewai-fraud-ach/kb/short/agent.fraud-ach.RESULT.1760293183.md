```json
{
  "id": "7d1b3ab2ccab865a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293183,
  "host_pid": "9e6742732c60:1",
  "hash": "affe7eecc14afb12c7656402ca8dc3e21d075ef9f1426b50fdf713cd096e9022",
  "cid": "QmV1affe7eecc14afb12c7656402ca8dc3e21d075ef9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293183,
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
      "evaluated_at": 1760293183
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
  "sig": "f8d0b04756c7a3b5de4fa3b1f783b4a75e45634e0ab73c94bebdb814c7a22a62"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247969582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 289, 'threshold': 50, 'total_amount': 142995177, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 288, 'first_seen': 1760284979, 'matching_hash': '259c183eb9552f9c'}}}