```json
{
  "id": "fa1c2a2d3dd1acb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285828,
  "host_pid": "9e6742732c60:1",
  "hash": "1462295f3626dc5835fc9bc310733108c4e6c22688b96238e4a4682c7ee3a0af",
  "cid": "QmV11462295f3626dc5835fc9bc310733108c4e6c226",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285828,
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
      "evaluated_at": 1760285828
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
  "sig": "915437222f8ab427118d9ea70fa275d7707023c59d9909b605afb53f9069450d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000038917834
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285765, 'matching_hash': '760f57350f86dbe3'}}}