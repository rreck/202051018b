```json
{
  "id": "a7e92696ecea12b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291104,
  "host_pid": "9e6742732c60:1",
  "hash": "85e2cf1482141651f9e041771b09627ce7b4207763cb5c7818e984ea5413e367",
  "cid": "QmV185e2cf1482141651f9e041771b09627ce7b42077",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291104,
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
      "evaluated_at": 1760291104
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
  "sig": "a628910fa7ddf7824df9296cfad248b24dcd988ef16135dc7e713c734a5bce3d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240945799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 11415452, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}