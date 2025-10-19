```json
{
  "id": "e0ead6fd5f00dce8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285236,
  "host_pid": "9e6742732c60:1",
  "hash": "2257ad872970c5c0318ea9568addc8586630232c5121345fa5b86e384ec15c65",
  "cid": "QmV12257ad872970c5c0318ea9568addc8586630232c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285236,
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
      "evaluated_at": 1760285236
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
  "sig": "289dbc5ff1d3a611e239312a288fd4268687aebe3c9aca6462f8a732a5240c50"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009594239738
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760284979, 'matching_hash': '98c544a6e0691c0b'}}}