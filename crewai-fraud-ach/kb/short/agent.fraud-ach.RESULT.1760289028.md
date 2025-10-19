```json
{
  "id": "2beee378c3f0e758",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289028,
  "host_pid": "9e6742732c60:1",
  "hash": "2e7bf3e58338cb92c37da7281835105c16dfc39a525afae464eb6cb35fb5e357",
  "cid": "QmV12e7bf3e58338cb92c37da7281835105c16dfc39a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289028,
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
      "evaluated_at": 1760289028
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
  "sig": "57b093b97946ca553b62e4071a8d0015842d64b379b05dfb066c2f918b6dded4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593077739
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 30351840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': 'dc5b0e0c6a053908'}}}