```json
{
  "id": "03ab15950005064b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288247,
  "host_pid": "9e6742732c60:1",
  "hash": "d498b8e4fc319208a7ed47d02bd82619e4d2e90e620c9a2238ad9b26436c2771",
  "cid": "QmV1d498b8e4fc319208a7ed47d02bd82619e4d2e90e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288247,
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
      "evaluated_at": 1760288247
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
  "sig": "b395e9e750ff1461337d3462b02854c2612fb29b87d1a3cf949ed7ed4a13b4d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240153207
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 21750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285764, 'matching_hash': '9e24c0ed91a48db3'}}}