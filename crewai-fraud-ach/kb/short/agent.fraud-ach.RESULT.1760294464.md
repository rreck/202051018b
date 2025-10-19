```json
{
  "id": "e62656258eecd2c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294464,
  "host_pid": "9e6742732c60:1",
  "hash": "3c84178d0499bdc19e27d5f4b2e5423647823e691d40711af2d71e65579843a1",
  "cid": "QmV13c84178d0499bdc19e27d5f4b2e5423647823e69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294464,
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
      "evaluated_at": 1760294464
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
  "sig": "aebd41c02b58f7bc080918f5ed725d86aa69417e1b03bbf5d75833563f35f4e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027147487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 118953352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': 'f2056111b893f4fa'}}}