```json
{
  "id": "41436f8c41fd966a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290230,
  "host_pid": "9e6742732c60:1",
  "hash": "617c620071615b1e1ef2d696a3d0264ab05199147e6571f94f98d741e02740af",
  "cid": "QmV1617c620071615b1e1ef2d696a3d0264ab0519914",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290230,
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
      "evaluated_at": 1760290230
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
  "sig": "e4e6dbfdf89bf5afa03daa444b70f090a5627c1b57d234bc7abb44e8ade35ffa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039510138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 16272625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '4238a333ed8712d2'}}}