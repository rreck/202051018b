```json
{
  "id": "6df0bfabb62f5c81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292447,
  "host_pid": "9e6742732c60:1",
  "hash": "2c353bf798cb2f156606c1fed8c8c93aff392f21f84f156abcb3cfac0183a38a",
  "cid": "QmV12c353bf798cb2f156606c1fed8c8c93aff392f21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292447,
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
      "evaluated_at": 1760292447
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
  "sig": "f39b876a8e0a53516b52faa73026d0a9faca259148755563a8862f2c7e74a9ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156237747
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 15419448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'b60e159429465bd2'}}}