```json
{
  "id": "30f8dbf427050bdc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288115,
  "host_pid": "9e6742732c60:1",
  "hash": "95bc0811d251442c463fa5ebcc7950f9710fe75f4e4196f1434b3aabf7ec24e6",
  "cid": "QmV195bc0811d251442c463fa5ebcc7950f9710fe75f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288115,
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
      "evaluated_at": 1760288115
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
  "sig": "b08c3c3c1565a769ff2f1abde17c04efb9f994c4539f0f0d47c0ddf970e0c0de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 39045358, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}