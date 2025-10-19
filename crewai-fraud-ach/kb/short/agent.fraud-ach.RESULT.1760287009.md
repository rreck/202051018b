```json
{
  "id": "4f2898def6ac9e37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287009,
  "host_pid": "9e6742732c60:1",
  "hash": "262c6f2ab95da477be8d012db66e16246a1e9c81623c3fdecf8bf975a7c5fced",
  "cid": "QmV1262c6f2ab95da477be8d012db66e16246a1e9c81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287009,
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
      "evaluated_at": 1760287009
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
  "sig": "c69d359976e293b131c12f701e0c7f43f509038a0ba8b8ba7364b700678a33f9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105154437530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15571170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': '1df4316d53c749d8'}}}