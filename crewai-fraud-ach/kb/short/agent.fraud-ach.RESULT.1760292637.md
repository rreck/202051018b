```json
{
  "id": "4e8c586ec9eaf328",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292637,
  "host_pid": "9e6742732c60:1",
  "hash": "08aa3e066e6acbff01836b9d63eba32d5be26f58d37093a23a21e6b9a1c5a4ab",
  "cid": "QmV108aa3e066e6acbff01836b9d63eba32d5be26f58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292637,
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
      "evaluated_at": 1760292637
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
  "sig": "7229bba6eb8ed14453c7db1392b9e02bcc33da90c85eca1658a908dfa4a2ad3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463831807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 36415550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'ac2384e4a351cc1b'}}}