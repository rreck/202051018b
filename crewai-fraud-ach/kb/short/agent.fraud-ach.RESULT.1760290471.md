```json
{
  "id": "49f0927c7748170a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290471,
  "host_pid": "9e6742732c60:1",
  "hash": "c057b5404fd55065bb64ebd3974dcc10837ebd741b4b7238191410f5c0adf8d6",
  "cid": "QmV1c057b5404fd55065bb64ebd3974dcc10837ebd74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290471,
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
      "evaluated_at": 1760290471
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
  "sig": "227b7bd08c83ef9c40ccc2d3a9925b61f75c46c1f0bac4489db997d25a233b41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246900677
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 98613794, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760284979, 'matching_hash': '3c9e668125e5b467'}}}