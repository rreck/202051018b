```json
{
  "id": "c6665353129031db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292892,
  "host_pid": "9e6742732c60:1",
  "hash": "a02fd0d4e566687dad68b262e7760f4eee06fb49f2eab1f380e087358c0e0ebe",
  "cid": "QmV1a02fd0d4e566687dad68b262e7760f4eee06fb49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292892,
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
      "evaluated_at": 1760292892
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
  "sig": "894c407bee37f8218129465c0d6cd2efe7a8f57a370aa2efaa29add12c2ec90d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246900677
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 283, 'threshold': 50, 'total_amount': 122941426, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 282, 'first_seen': 1760284979, 'matching_hash': '3c9e668125e5b467'}}}