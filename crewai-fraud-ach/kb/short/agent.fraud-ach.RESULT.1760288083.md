```json
{
  "id": "7f74fba9f6849262",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288083,
  "host_pid": "9e6742732c60:1",
  "hash": "943f5af421934eb934b7c57298a1c17f8e1c92dedfde9319a89f2bf4071c7ddc",
  "cid": "QmV1943f5af421934eb934b7c57298a1c17f8e1c92de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288083,
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
      "evaluated_at": 1760288083
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
  "sig": "016cda0d6e60033b6eb996807ea62e19ab8d7195c7621a34a677a6880916c2db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026169646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 24438788, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285764, 'matching_hash': '09339571c5d51c89'}}}