```json
{
  "id": "1c905046ee64c7e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291250,
  "host_pid": "9e6742732c60:1",
  "hash": "54aa1de27973dfed0e50cf9bc50966aef70f5a0ea5692055f86c9e16cd823a45",
  "cid": "QmV154aa1de27973dfed0e50cf9bc50966aef70f5a0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291250,
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
      "evaluated_at": 1760291250
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
  "sig": "6ed96d0717874af1866b62f36f884dbbdd1a788ab48dc80876b8d44ad2cea7e8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 42500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}