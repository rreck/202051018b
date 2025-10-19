```json
{
  "id": "3c63f8d34bbfb039",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291181,
  "host_pid": "9e6742732c60:1",
  "hash": "62b09a51dc4c0ee2e666a3ae22e1bd89a7f129d128a70c19f701750f71b058ab",
  "cid": "QmV162b09a51dc4c0ee2e666a3ae22e1bd89a7f129d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291181,
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
      "evaluated_at": 1760291181
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
  "sig": "beeff37c37b629bdefd22ac2eb875f2d69a6172cc3ecb028d39e4a291ffdcac3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273476886
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 51848355, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': 'e52038f69d26fe5a'}}}