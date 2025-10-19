```json
{
  "id": "4146294ce754300b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291285,
  "host_pid": "9e6742732c60:1",
  "hash": "c2116a27e05a721c8c3021edb7750f9af3d18c6cff34c20c5449af6e466f981b",
  "cid": "QmV1c2116a27e05a721c8c3021edb7750f9af3d18c6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291285,
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
      "evaluated_at": 1760291285
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
  "sig": "8affacbf985e917e6802a0994c842f45671e253722c99edb90fdf5efc495ac32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246932907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 77287896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'b5767c7cd6e7c742'}}}