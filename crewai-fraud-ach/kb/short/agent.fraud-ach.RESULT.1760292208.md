```json
{
  "id": "103c274be15e3a44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292208,
  "host_pid": "9e6742732c60:1",
  "hash": "db81f771424079eaca371c3c71a92812e2c165f2d3f7ea7a480a7c3254f95406",
  "cid": "QmV1db81f771424079eaca371c3c71a92812e2c165f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292208,
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
      "evaluated_at": 1760292208
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
  "sig": "8aea130e1ff72263ff384259973905381f3f188b3e968665fd5b940a0908f904"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276764543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 62976384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285765, 'matching_hash': '861ebf9054cc2433'}}}