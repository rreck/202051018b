```json
{
  "id": "d120516fded78ec6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289159,
  "host_pid": "9e6742732c60:1",
  "hash": "bcbb13748170330e3e75246b3c834ba14dfebe3be039d0e359e27d38c2752c18",
  "cid": "QmV1bcbb13748170330e3e75246b3c834ba14dfebe3b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289159,
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
      "evaluated_at": 1760289159
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
  "sig": "179c5c596915759f58d3edf9f0d933cef4f3b872ae38a05618855bfcf5a61848"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599876575
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 35903920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': '0131e24faef32fc6'}}}