```json
{
  "id": "eeb51dd0363b5bfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287963,
  "host_pid": "9e6742732c60:1",
  "hash": "36e9896642f2ebf2ca76db6a0a9888ffc761ea4ea68f6c1153983f45dd19aa5f",
  "cid": "QmV136e9896642f2ebf2ca76db6a0a9888ffc761ea4e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287963,
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
      "evaluated_at": 1760287963
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
  "sig": "c17d0e07165eb990e4ddea3dfde75755e4fc148a69c6a8b756f4fef48d59a872"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245693870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 20061366, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': '3f6bcdf181d34e46'}}}