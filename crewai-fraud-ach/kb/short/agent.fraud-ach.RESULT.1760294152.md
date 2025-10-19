```json
{
  "id": "5629b513bf6b2330",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294152,
  "host_pid": "9e6742732c60:1",
  "hash": "d3ee615af36309f2db81441c614f013b890aebf1886a18e3bc0fc2fbfb1bc49a",
  "cid": "QmV1d3ee615af36309f2db81441c614f013b890aebf1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294152,
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
      "evaluated_at": 1760294152
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
  "sig": "4542c520a909b1ef7ebc3e87ffd816775e60f7c12852061fe665ca2e62edfc08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 73833536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}