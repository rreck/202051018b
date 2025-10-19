```json
{
  "id": "5ff88748c588d73b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290346,
  "host_pid": "9e6742732c60:1",
  "hash": "9df89bee89f7f6b7f6b0554e77216aebb775a476eb8ee477a22cf238b5ead2f0",
  "cid": "QmV19df89bee89f7f6b7f6b0554e77216aebb775a476",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290346,
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
      "evaluated_at": 1760290346
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
  "sig": "d7b33dbc833467afeec173a7f03e6d52e7abaa3d5668cd78ff6376cd56cd41bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026865262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 72481668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': 'acc989ae5f5d7052'}}}