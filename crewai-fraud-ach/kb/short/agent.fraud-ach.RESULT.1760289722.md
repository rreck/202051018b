```json
{
  "id": "2b6d15d0e8c60988",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289722,
  "host_pid": "9e6742732c60:1",
  "hash": "13f97f69478418a3048991acbee5a012dc96ed0cb51bdacaf8c86620eb6ded5c",
  "cid": "QmV113f97f69478418a3048991acbee5a012dc96ed0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289722,
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
      "evaluated_at": 1760289722
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
  "sig": "a1c1dba7828e8bb5ade06b0b9ea345077f5ad46e88b9f93ecdfd572e2ece8466"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243367348
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 42549848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': 'a37b6eb1b4e3b31b'}}}