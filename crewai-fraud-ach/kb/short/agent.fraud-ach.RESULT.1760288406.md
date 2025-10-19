```json
{
  "id": "5957367fd9debbc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288406,
  "host_pid": "9e6742732c60:1",
  "hash": "23b209c6061de9ba550c075d3cbf994951c3acb7efa9754420ff536a2267c273",
  "cid": "QmV123b209c6061de9ba550c075d3cbf994951c3acb7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288406,
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
      "evaluated_at": 1760288406
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
  "sig": "19497a9f7ab2c2e25e8a23127a5e95cdec63ca8519adb9250d7465ee6c9deeb4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025325708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 29647276, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': '23dd43a9dda0a05d'}}}