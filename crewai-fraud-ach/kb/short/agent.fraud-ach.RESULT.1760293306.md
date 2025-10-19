```json
{
  "id": "375d560a8247d4ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293306,
  "host_pid": "9e6742732c60:1",
  "hash": "b9b25d9cc0163c6cc0c9fc275445e775ddfe9f895ddb4aaf18d815de8e1e4e58",
  "cid": "QmV1b9b25d9cc0163c6cc0c9fc275445e775ddfe9f89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293306,
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
      "evaluated_at": 1760293306
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
  "sig": "205ca4de7bb974f5465aebb6cf09d4e323878523072d895585990b4a2e681031"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024544859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 104698224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '21e0fdbcd06f2d49'}}}