```json
{
  "id": "c78f48e0833c893d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287353,
  "host_pid": "9e6742732c60:1",
  "hash": "4065a84b9324f37da8c1a2b21214485e2d4dbf0360baf8c327a5029d3d7aa202",
  "cid": "QmV14065a84b9324f37da8c1a2b21214485e2d4dbf03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287353,
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
      "evaluated_at": 1760287353
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
  "sig": "639fd6931dec9c66dbc6335ad8cfb0e1ed37d42f65e20b9ee8df79164adce01b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594239738
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 28307188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760284979, 'matching_hash': '98c544a6e0691c0b'}}}raud_detected': True, 'risk_score': 95, 'details': {'routing_number': '676666915', 'validation_error': 'Invalid routing number checksum'}}}