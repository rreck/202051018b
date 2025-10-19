```json
{
  "id": "eeddb882dda4c4e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289503,
  "host_pid": "9e6742732c60:1",
  "hash": "7585658668f83874a5876446added8230945c028209b812923ae2a2673b622c1",
  "cid": "QmV17585658668f83874a5876446added8230945c028",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289503,
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
      "evaluated_at": 1760289503
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
  "sig": "f5fe799c7deec23a01f7f4c7d76fdb2649d829e1bcb8b693250b8dfd55bb3a35"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469615703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 23813375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '33adc30ff3203421'}}}