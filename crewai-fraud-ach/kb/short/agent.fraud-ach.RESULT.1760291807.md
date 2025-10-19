```json
{
  "id": "1905ea400ca34062",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291807,
  "host_pid": "9e6742732c60:1",
  "hash": "e0756e17e652b41e05421eca2709c0004651b7d8ab5a4144db61e78eb5a55016",
  "cid": "QmV1e0756e17e652b41e05421eca2709c0004651b7d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291807,
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
      "evaluated_at": 1760291807
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
  "sig": "2f12f2e58e20dd4d207c84a40fc367949009b169d5414367167d0ee95ba40ae8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598844081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 36045144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': 'ecb0c176cd8f032c'}}}