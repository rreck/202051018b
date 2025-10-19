```json
{
  "id": "7cc2f8914dfd5c53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290951,
  "host_pid": "9e6742732c60:1",
  "hash": "199c00de0174af31c06892e86aa4121a00efc9a7a679ba6f67e5dbb140d4f27b",
  "cid": "QmV1199c00de0174af31c06892e86aa4121a00efc9a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290951,
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
      "evaluated_at": 1760290951
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
  "sig": "76ad5fae58b387bf010e6e58691fdfce80e46808ce3772bc12355ff023e6f74f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020048209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 13554265, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': '08bd6998776e568a'}}}