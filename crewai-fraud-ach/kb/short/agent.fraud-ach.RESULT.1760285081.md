```json
{
  "id": "d17db78ae12a220e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285081,
  "host_pid": "9e6742732c60:1",
  "hash": "aa69481cdce52f0fa6631ba5bd43b1342262d1d3b59f2cba6f85b73b9b44028f",
  "cid": "QmV1aa69481cdce52f0fa6631ba5bd43b1342262d1d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285081,
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
      "evaluated_at": 1760285081
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
  "sig": "81b84ee1eae162d2e68e4677977ce28c94bc68989df94de5f11f2f16e6c4e8df"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009594873577
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760284979, 'matching_hash': '5add1f4a09a12b51'}}}