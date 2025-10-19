```json
{
  "id": "b714a184a32df51c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291712,
  "host_pid": "9e6742732c60:1",
  "hash": "3cc0300a9efbfc9e76acb5191ed316e5f34779f4a1df35b10fa525c674a0335f",
  "cid": "QmV13cc0300a9efbfc9e76acb5191ed316e5f34779f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291712,
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
      "evaluated_at": 1760291712
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
  "sig": "53aeda6f6a549571d7b485ec12e94141906e48a5f713ef8fa71f8682388ac33c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028366239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 24638082, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': 'fc3cc28fddce4cc6'}}}