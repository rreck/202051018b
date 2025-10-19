```json
{
  "id": "4bb759760e0f68cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285840,
  "host_pid": "9e6742732c60:1",
  "hash": "e8e76998b44065e6fc07711f459cd23b92081eccc3c5d00f75b092b9cd1c72b7",
  "cid": "QmV1e8e76998b44065e6fc07711f459cd23b92081ecc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285840,
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
      "evaluated_at": 1760285840
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
  "sig": "ecc103fb0a0ed820ea5b5784bc98ecdc05a1a9526a51d0a8aa48a2bfb7449892"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009599553408
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285763, 'matching_hash': '67e91645ed6012ef'}}}