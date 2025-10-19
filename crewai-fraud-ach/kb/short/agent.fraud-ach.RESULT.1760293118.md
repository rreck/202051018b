```json
{
  "id": "b026b2ed3d1eadc5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293118,
  "host_pid": "9e6742732c60:1",
  "hash": "6517aef2b3aebc2b0a7b47972bb4f85e37bab06771077540fac52520034735f8",
  "cid": "QmV16517aef2b3aebc2b0a7b47972bb4f85e37bab067",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293118,
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
      "evaluated_at": 1760293118
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
  "sig": "558622fe7917b9e78ce69b1f5ab960bc4b0537d123f1d19653133e671d9a5d1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247162231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 58539772, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '92769f469bceb512'}}}