```json
{
  "id": "7fc0c455cc75f4fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287165,
  "host_pid": "9e6742732c60:1",
  "hash": "813036b2550630dc9a1d2ff28c19f39dcfd1e2453718736e2140f2675e526a84",
  "cid": "QmV1813036b2550630dc9a1d2ff28c19f39dcfd1e245",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287165,
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
      "evaluated_at": 1760287165
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
  "sig": "16a555977e404ba2bd7f24ac48d571bde42a673321a642db17468e7ee8398c5b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13012600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}