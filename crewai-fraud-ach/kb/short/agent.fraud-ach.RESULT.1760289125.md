```json
{
  "id": "a79f37862de05b94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289125,
  "host_pid": "9e6742732c60:1",
  "hash": "d20f4bdffd12142b179865297a0ab6b353f342f6ffa46763779f8cb76b7e36bd",
  "cid": "QmV1d20f4bdffd12142b179865297a0ab6b353f342f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289125,
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
      "evaluated_at": 1760289125
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
  "sig": "3f3a7cf50728cfa1b5d877baae3d2542e5bd895e459e6b11f95fe3c07436fd8f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271976362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 46048248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285764, 'matching_hash': 'fe2a7bcd9137a402'}}}maly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5663035}}}