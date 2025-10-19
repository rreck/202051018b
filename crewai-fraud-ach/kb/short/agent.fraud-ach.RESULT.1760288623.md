```json
{
  "id": "d04ce6af4b72804b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288623,
  "host_pid": "9e6742732c60:1",
  "hash": "91a3cc5fdbba484a803fdf815ea75325a5128fee78a8b18687d042d029a073d8",
  "cid": "QmV191a3cc5fdbba484a803fdf815ea75325a5128fee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288623,
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
      "evaluated_at": 1760288624
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
  "sig": "bda2af54340062d8dc215b8db8fc9b628a68d45765ecdb3f51698d80dd1464ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462273667
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 44202213, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': 'db56bbc4ded669a9'}}}