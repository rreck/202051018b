```json
{
  "id": "502c8feff0e97cde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288336,
  "host_pid": "9e6742732c60:1",
  "hash": "55f7a276b61fd90ff001d8586594035b7894c7a7c4ed4bb24db2b735fca8f279",
  "cid": "QmV155f7a276b61fd90ff001d8586594035b7894c7a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288336,
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
      "evaluated_at": 1760288336
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
  "sig": "b415313a68d0c868c64916bb2bce5cb51d0eb41cee582bfe132a00ff8420da7f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 13267260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}