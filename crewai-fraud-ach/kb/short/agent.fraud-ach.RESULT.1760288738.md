```json
{
  "id": "e625dd3b4e55d03b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288738,
  "host_pid": "9e6742732c60:1",
  "hash": "26ba1e80169414bf55f9e94ba85696d466ec3852055bbb6bc23f046a0c59632e",
  "cid": "QmV126ba1e80169414bf55f9e94ba85696d466ec3852",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288738,
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
      "evaluated_at": 1760288738
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
  "sig": "758ec4c6da57ada0c31a0f180dbecf7822c2517bf457c1d4e17c131b41fb9938"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026265735
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 35912976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': 'e94388ee515b2db1'}}}