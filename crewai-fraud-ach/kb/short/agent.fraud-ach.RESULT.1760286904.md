```json
{
  "id": "9a7b878fbd0ef2e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286904,
  "host_pid": "9e6742732c60:1",
  "hash": "7944b6a11bc8ebe621ee6f695a9fdc0f702b0d04c3216efe0598fdfbeaa1925d",
  "cid": "QmV17944b6a11bc8ebe621ee6f695a9fdc0f702b0d04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286904,
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
      "evaluated_at": 1760286904
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "cae48e04e5615ac26c1a23e9a1822898361ba4d3644567897174b6f510d02172"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13928028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}