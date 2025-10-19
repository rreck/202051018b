```json
{
  "id": "2f1dc97ca9a41766",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286413,
  "host_pid": "9e6742732c60:1",
  "hash": "d6d5dda117b18ef55c13917abc19ff504f02e6c64ee0c9e8820d43a939867c33",
  "cid": "QmV1d6d5dda117b18ef55c13917abc19ff504f02e6c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286413,
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
      "evaluated_at": 1760286413
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
  "sig": "5c50c36c3742dccc3de848e128c27fd91bfae5bed05c003e85f76755b23f2aea"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}