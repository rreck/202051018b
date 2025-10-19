```json
{
  "id": "291e0176cf27c043",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291931,
  "host_pid": "9e6742732c60:1",
  "hash": "29efcdbf0a4925669bbaa71d7694e2b895ae862a1a8795f13cd059872f9fc064",
  "cid": "QmV129efcdbf0a4925669bbaa71d7694e2b895ae862a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291931,
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
      "evaluated_at": 1760291931
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
  "sig": "edc816e1774abfbf5c7b589c4276df7160893459d5f6f85c253619d7c635b16b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460644681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 63474918, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285764, 'matching_hash': '02c671505c0a8698'}}}