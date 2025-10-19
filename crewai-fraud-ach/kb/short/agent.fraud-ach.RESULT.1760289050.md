```json
{
  "id": "2a1651406cf30504",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289050,
  "host_pid": "9e6742732c60:1",
  "hash": "c9aba2e7586b1f13da55a7283a5fa7e463c0258301d78ec8d4aff47d97aad4d7",
  "cid": "QmV1c9aba2e7586b1f13da55a7283a5fa7e463c02583",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289050,
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
      "evaluated_at": 1760289050
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
  "sig": "6b2226740fc6b2457cdb3a70b326f322db8684c0a31870e00a4e097618c00cbe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032979175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 36688736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '92afbef802abc12c'}}}