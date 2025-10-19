```json
{
  "id": "f7a9be10c46360d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290821,
  "host_pid": "9e6742732c60:1",
  "hash": "b78c895ce3c6206c7490babdaba61a9902c6d3493f573ca059110c70e79626b5",
  "cid": "QmV1b78c895ce3c6206c7490babdaba61a9902c6d349",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290821,
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
      "evaluated_at": 1760290821
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
  "sig": "dda78ee71c47878c19aa08521caf834f778025269910224bd3d2c1277c92770c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598774484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 31543520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285764, 'matching_hash': 'dadabb4a69349ebb'}}}