```json
{
  "id": "5a5573e795f5cc8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289025,
  "host_pid": "9e6742732c60:1",
  "hash": "2c424f73d00cca4b55e67b91171fd569d9fb18c97c2e77dbbe8cf49be400e030",
  "cid": "QmV12c424f73d00cca4b55e67b91171fd569d9fb18c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289025,
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
      "evaluated_at": 1760289025
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
  "sig": "062d3ec2c1a7d4c8aa8f3bbde6a2d00601a14ae25f76337f7247c140fe510c90"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465682795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 47108105, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760284979, 'matching_hash': 'c9bd5d9b74477b1c'}}}