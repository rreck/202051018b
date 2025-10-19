```json
{
  "id": "ff88f1e5ab059646",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291053,
  "host_pid": "9e6742732c60:1",
  "hash": "72b9a89faa97944a29e757d8e7637e1dfe09cb2d493a34ee3eefb22df49fc3a1",
  "cid": "QmV172b9a89faa97944a29e757d8e7637e1dfe09cb2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291053,
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
      "evaluated_at": 1760291053
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
  "sig": "f68b687ae29f5a4d81e5b118c1f0e890b1ed9acf1e4c4b787bb31068e5798212"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033919598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 62566894, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '1dbf667d29bdf8b7'}}}