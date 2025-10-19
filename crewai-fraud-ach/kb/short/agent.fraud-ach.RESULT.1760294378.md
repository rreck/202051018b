```json
{
  "id": "e7570724ead0c9c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294378,
  "host_pid": "9e6742732c60:1",
  "hash": "5a93e9c800c1c036f996fddba7f2c469d040f0265086b7b7abe225ec418020a9",
  "cid": "QmV15a93e9c800c1c036f996fddba7f2c469d040f026",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294378,
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
      "evaluated_at": 1760294378
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
  "sig": "1cff6aef9e09f067e4d5862529b7d1d489208c4bd19a5234283f53e1835b393e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469479183
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 31660830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '2b83b0aed5f7590d'}}}}