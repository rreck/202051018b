```json
{
  "id": "1bc367dd242aaac0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293092,
  "host_pid": "9e6742732c60:1",
  "hash": "650c83865678f7e30d15836faeb79372a090c2c87a90fe4b1e12c53c80dc8d87",
  "cid": "QmV1650c83865678f7e30d15836faeb79372a090c2c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293092,
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
      "evaluated_at": 1760293092
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
  "sig": "37b7afb3e7a4a83ab5c42c4d36c0e98e8224e94e38ad4a8bef6e030c7b427343"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151102645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 86728174, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '9dd268c0fa996698'}}}