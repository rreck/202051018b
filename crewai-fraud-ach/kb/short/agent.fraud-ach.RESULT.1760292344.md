```json
{
  "id": "ae94be9a8def0129",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292344,
  "host_pid": "9e6742732c60:1",
  "hash": "2625f9624add609b7b850c8b480285bc08da3661551226c6d930af9e5a72f103",
  "cid": "QmV12625f9624add609b7b850c8b480285bc08da3661",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292344,
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
      "evaluated_at": 1760292344
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
  "sig": "8beb49d2cbe8dcbe7047f317e9c0316c2fe8479fa7cdb890b12716e35ab87231"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039495479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 79471080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}