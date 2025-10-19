```json
{
  "id": "79a79e1b985a5f34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289946,
  "host_pid": "9e6742732c60:1",
  "hash": "001961ff2ee7f93128b25b22663bad0d4be24e1448ab567f0bd2a395ee8ce192",
  "cid": "QmV1001961ff2ee7f93128b25b22663bad0d4be24e14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289946,
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
      "evaluated_at": 1760289946
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
  "sig": "cd5ffb1b27971044e51da5e3fc3c0abf15b55f4727e4103751fda32020c8d100"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153371756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 57201610, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285764, 'matching_hash': 'f6b71775dc53ea2e'}}}