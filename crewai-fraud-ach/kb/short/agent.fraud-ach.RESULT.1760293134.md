```json
{
  "id": "4f017c8be03346ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293134,
  "host_pid": "9e6742732c60:1",
  "hash": "0920845fbd2e47c1cc8dc14485ef8426bfddcdd5e3bc3710c921f211ff711097",
  "cid": "QmV10920845fbd2e47c1cc8dc14485ef8426bfddcdd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293134,
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
      "evaluated_at": 1760293134
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
  "sig": "574c6a296db9dbbf9cf441a244506d5cc19add20bb23555c2cae1b801f82c0c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023759733
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 48856248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': 'cdd972b8484ef71b'}}}