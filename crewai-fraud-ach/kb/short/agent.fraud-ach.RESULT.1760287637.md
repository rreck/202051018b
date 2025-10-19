```json
{
  "id": "2d7442855546aebd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287637,
  "host_pid": "9e6742732c60:1",
  "hash": "0185353d63d319b2afc77d19fcb12359df870eef3f120a0bd7e5cc510e2adca1",
  "cid": "QmV10185353d63d319b2afc77d19fcb12359df870eef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287637,
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
      "evaluated_at": 1760287637
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
  "sig": "4beb2e294e9cbbc8530897270dbb530d7961e928f1f6f4b1225511bc07389728"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 121000245808112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 20832980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': 'd8dffc30f620e6a0'}}}}}}