```json
{
  "id": "dd5adfbb1c62f645",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286499,
  "host_pid": "9e6742732c60:1",
  "hash": "7e9cacfe1918a110ab48bd1df399f53a06bf6c615e2bdbfc333f4b0e061c5869",
  "cid": "QmV17e9cacfe1918a110ab48bd1df399f53a06bf6c61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286499,
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
      "evaluated_at": 1760286499
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
  "sig": "1891e0b4518bb4b841b03e6ee3bf4217793d75619e858c09108c2fab190be3af"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12106665, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}