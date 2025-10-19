```json
{
  "id": "6303869353b91ee3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291651,
  "host_pid": "9e6742732c60:1",
  "hash": "a32afb3b29f8b0ca14afa3a19af185655c02c7cdef85719825bd3b79c4f8e52c",
  "cid": "QmV1a32afb3b29f8b0ca14afa3a19af185655c02c7cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291651,
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
      "evaluated_at": 1760291651
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
  "sig": "e783c9dc51caa67172fa715de32d10445ae48bb7770fa64a965e1187b980b749"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464999191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 22864860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '0f07ea7feb264441'}}}