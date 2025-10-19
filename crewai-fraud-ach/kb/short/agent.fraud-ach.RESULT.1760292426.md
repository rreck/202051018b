```json
{
  "id": "f4bf765e1722b3a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292426,
  "host_pid": "9e6742732c60:1",
  "hash": "852d30296abdcf18a3ae7e60644f63f1715cc405f74a483e63c80a1768017e0d",
  "cid": "QmV1852d30296abdcf18a3ae7e60644f63f1715cc405",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292426,
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
      "evaluated_at": 1760292426
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
  "sig": "117b74e8e30425f5649278cf35c6671bd594b0995ad04eb24041215a0ec09f1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022148998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 54767182, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': 'cc8f74c02d21ef44'}}}