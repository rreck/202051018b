```json
{
  "id": "57ef63f66cfe35bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290091,
  "host_pid": "9e6742732c60:1",
  "hash": "35ebb9ab6f793df071d0c337a2076a65e7b3c4b81d95534691643044d6494850",
  "cid": "QmV135ebb9ab6f793df071d0c337a2076a65e7b3c4b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290091,
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
      "evaluated_at": 1760290091
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
  "sig": "39048c2392cb1862cac83e2d61854cf09dde06be451e16e86a8faaa7c96d5a31"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034624068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 20199096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': 'e9c21d379839efb6'}}}