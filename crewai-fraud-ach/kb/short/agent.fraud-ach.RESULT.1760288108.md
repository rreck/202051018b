```json
{
  "id": "b7ad590536d53604",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288108,
  "host_pid": "9e6742732c60:1",
  "hash": "3a624795ec0c699193874bb46aeb1d9d3d1764911e36e35a6127b68ee272f88f",
  "cid": "QmV13a624795ec0c699193874bb46aeb1d9d3d176491",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288108,
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
      "evaluated_at": 1760288108
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
  "sig": "fff4c437da4dd44e712d085e9a2717406d2ce366822d9a4da7787aaf4404e347"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034886670
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 11356475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': 'cbf6d0e6528ee173'}}}