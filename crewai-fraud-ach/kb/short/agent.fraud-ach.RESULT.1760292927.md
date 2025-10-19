```json
{
  "id": "72531621bb191e8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292927,
  "host_pid": "9e6742732c60:1",
  "hash": "24124c7d1763718baf114868203a50aed20122e1b327e1ba9c1c6149317db1c0",
  "cid": "QmV124124c7d1763718baf114868203a50aed20122e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292927,
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
      "evaluated_at": 1760292927
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "2d8e8569b483417f3500fd59758fc182323973e23ed91f9f1586fa5df06179e3"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 372851334846795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 102318944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': 'e24b6b5408d67f01'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}