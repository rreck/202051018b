```json
{
  "id": "1116dee9fb7b05a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290247,
  "host_pid": "9e6742732c60:1",
  "hash": "34c0c227d4fd399495dc1711a341f11687b6eb8f86190c9a94c0bd112d073eee",
  "cid": "QmV134c0c227d4fd399495dc1711a341f11687b6eb8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290247,
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
      "evaluated_at": 1760290247
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
  "sig": "c384f225abfbc94926e826030b3334e72e8373bc2b6a2a76122d065d44ccf395"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027918613
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 16499840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285764, 'matching_hash': 'c11d1385920c0a28'}}}