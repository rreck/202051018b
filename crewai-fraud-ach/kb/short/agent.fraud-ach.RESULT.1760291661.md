```json
{
  "id": "b9d98d9467ffdf24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291661,
  "host_pid": "9e6742732c60:1",
  "hash": "b7d6e1dc7d71b223b18a9d6cebea0407ec894543ba6a0e38119999949f7f4a0a",
  "cid": "QmV1b7d6e1dc7d71b223b18a9d6cebea0407ec894543",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291661,
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
      "evaluated_at": 1760291661
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
  "sig": "565ffe64dc4d1148e6f4da0a076a055461009d5175c1936fd1a8cb824b4a9a2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 89465760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}