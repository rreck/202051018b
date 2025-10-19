```json
{
  "id": "dd3ce62b7ae76e87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290782,
  "host_pid": "9e6742732c60:1",
  "hash": "25d1aed4b2145376d50e9488e8c3dd723c19e7732bb19ad6fc0a31df78be7853",
  "cid": "QmV125d1aed4b2145376d50e9488e8c3dd723c19e773",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290782,
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
      "evaluated_at": 1760290782
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
  "sig": "d22db3060e57672961e70e9c1fc4b1aa4b8740a66e0c74936c205d305e91cab7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032365153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 63026805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': 'db9686895aceb522'}}}