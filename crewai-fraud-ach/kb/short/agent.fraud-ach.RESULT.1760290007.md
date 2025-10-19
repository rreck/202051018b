```json
{
  "id": "bf56f0e889768019",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290007,
  "host_pid": "9e6742732c60:1",
  "hash": "f33fa93450931dcc890fb093092117b5e31d7e7803df225ccd2f5d6ee74194eb",
  "cid": "QmV1f33fa93450931dcc890fb093092117b5e31d7e78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290007,
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
      "evaluated_at": 1760290007
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
  "sig": "3f786d2a84737b01fa638579c193799bc745986b6de335823e3d779d2c995ba6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020626056
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 13900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': 'ca4ea9492786d8a3'}}}