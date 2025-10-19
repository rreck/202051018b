```json
{
  "id": "0747168f7ee76f35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290116,
  "host_pid": "9e6742732c60:1",
  "hash": "e4d38517e0b0c78d39d2145a917301cf9fb7668e38045d97bfe4b4829cdf145e",
  "cid": "QmV1e4d38517e0b0c78d39d2145a917301cf9fb7668e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290116,
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
      "evaluated_at": 1760290116
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
  "sig": "3d49eb574be03b2c592668209b716aa90c3e66fe86d82d658534942a8498b4af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028270724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': 'c4ee7f0f971d402b'}}}een': 1760285763, 'matching_hash': 'cc2974580ec11a3c'}}}