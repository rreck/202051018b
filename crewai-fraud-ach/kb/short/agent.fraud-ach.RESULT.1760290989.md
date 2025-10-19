```json
{
  "id": "cb337faa2c12fede",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290989,
  "host_pid": "9e6742732c60:1",
  "hash": "2dcae5b249ef1bee3d9bf6c7e1653f3d21304c1c0f12e214ce33ab15926e4d29",
  "cid": "QmV12dcae5b249ef1bee3d9bf6c7e1653f3d21304c1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290989,
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
      "evaluated_at": 1760290989
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
  "sig": "03fad453f2d485b43b1f2a210d2d602e6eb955364a6b2beae02a91d048ce341d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031291734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 55854136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': 'b88361d419e7152d'}}}