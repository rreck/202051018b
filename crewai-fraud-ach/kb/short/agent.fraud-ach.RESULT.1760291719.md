```json
{
  "id": "4ed47ccb975f68ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291719,
  "host_pid": "9e6742732c60:1",
  "hash": "1ee11e1b9c45240ae6783bc5fdc0a0b821ddf0ad965275f320ca0e62f25cf494",
  "cid": "QmV11ee11e1b9c45240ae6783bc5fdc0a0b821ddf0ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291719,
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
      "evaluated_at": 1760291719
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
  "sig": "693d5e3a5f7f032e143e65187eca85d85486c83297378dc461432fdd669ef4d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023496704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 61368593, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': 'f379baac52e28232'}}}