```json
{
  "id": "134bf6a99c7ed7e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288463,
  "host_pid": "9e6742732c60:1",
  "hash": "e2415ed4d37988406b415b4e3a1d4dd49d1681f93d40ed41337b04259a7cf212",
  "cid": "QmV1e2415ed4d37988406b415b4e3a1d4dd49d1681f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288463,
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
      "evaluated_at": 1760288463
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
  "sig": "4a06ea7578f316ba52ac0c660cfb42171c0acf5940d0d53a5fb7931608c2ec2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465310802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 35157598, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '86dc5261411570c1'}}}