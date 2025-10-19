```json
{
  "id": "97824d257bdbdca8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291027,
  "host_pid": "9e6742732c60:1",
  "hash": "0445a4fb2f8c552de974dede26374c476fb8f8695f830d78e7366ae9f3efd4b4",
  "cid": "QmV10445a4fb2f8c552de974dede26374c476fb8f869",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291027,
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
      "evaluated_at": 1760291027
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
  "sig": "3e4b77152f4f65ad6350b39e63426d7fdb1a14ad0ac3b6e156a71d1977571e54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462094881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 78673650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': '1dac8a668721a731'}}}