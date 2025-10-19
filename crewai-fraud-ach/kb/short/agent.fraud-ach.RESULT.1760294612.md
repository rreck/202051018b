```json
{
  "id": "095eb429212c2049",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294612,
  "host_pid": "9e6742732c60:1",
  "hash": "9c64229c8478d169c97534effe0faf8045e4239f03331ed34505c9711faee06d",
  "cid": "QmV19c64229c8478d169c97534effe0faf8045e4239f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294612,
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
      "evaluated_at": 1760294612
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
  "sig": "512d84ff6cd8589b08cc6b3a278d16dd22e7360928dec7001e1671904575bef5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030656036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 317, 'threshold': 50, 'total_amount': 90205837, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 316, 'first_seen': 1760284979, 'matching_hash': '54d3add09935598e'}}}