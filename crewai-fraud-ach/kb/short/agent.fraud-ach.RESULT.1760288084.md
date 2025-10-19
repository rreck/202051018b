```json
{
  "id": "c24177b30546d3ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288084,
  "host_pid": "9e6742732c60:1",
  "hash": "90d5b6c85af0686b4cd594d95d051c3e10e6e781833e897d7f6e0fd13ee1bd8b",
  "cid": "QmV190d5b6c85af0686b4cd594d95d051c3e10e6e781",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288084,
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
      "evaluated_at": 1760288084
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
  "sig": "7399405299142d1d0c34738154f639bf635fdf64152b0144f29c523b33b8971d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025341279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 33730290, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': 'e2ff1695635a899d'}}}