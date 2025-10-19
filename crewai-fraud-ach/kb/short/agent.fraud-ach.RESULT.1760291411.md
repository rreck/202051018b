```json
{
  "id": "ce64320af9879cd2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291411,
  "host_pid": "9e6742732c60:1",
  "hash": "eec3962a62e4bf59e89e3839f42abef891f0b9de3d1bace50ca68cf38e651a13",
  "cid": "QmV1eec3962a62e4bf59e89e3839f42abef891f0b9de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291411,
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
      "evaluated_at": 1760291411
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
  "sig": "02a540451ec5487ba18b9903d668f41c58e8d5ab1c7aead743f65c6c072c20c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467134805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 47335830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': 'bc3c56d4b0e7489d'}}}