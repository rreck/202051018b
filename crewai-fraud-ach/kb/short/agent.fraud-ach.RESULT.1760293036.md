```json
{
  "id": "8a103d72c88c23b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293036,
  "host_pid": "9e6742732c60:1",
  "hash": "f6fa6cdbf2f2dc7a3cb3dfcd08c737e1385b22dbc30c77239fca893345263439",
  "cid": "QmV1f6fa6cdbf2f2dc7a3cb3dfcd08c737e1385b22db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293036,
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
      "evaluated_at": 1760293036
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
  "sig": "00d44af9e2afe657bc7a669d4b2b99da6fd4e37e0bfbf88d8c31c50e4240b340"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275777124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 57919260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'd1e6afcf07f21c4a'}}}