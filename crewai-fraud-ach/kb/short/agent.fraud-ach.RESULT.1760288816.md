```json
{
  "id": "644f1c5b086d8daa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288816,
  "host_pid": "9e6742732c60:1",
  "hash": "bd173e993328fa0b857a45cbcb93c84df6a5d876ce353aeeb10f1525d56535a6",
  "cid": "QmV1bd173e993328fa0b857a45cbcb93c84df6a5d876",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288816,
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
      "evaluated_at": 1760288816
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
  "sig": "b5bf7a70cf3ed4b0447e2c6d9b4850b487bc495e4c8b0e487acc3460a9dbcb21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466146132
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 41667255, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': '20fb82cc575104fa'}}}