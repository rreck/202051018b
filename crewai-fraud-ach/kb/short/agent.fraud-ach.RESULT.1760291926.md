```json
{
  "id": "9f8e97b139f230ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291926,
  "host_pid": "9e6742732c60:1",
  "hash": "e5d59774ece1c0159de85deb18b02ecb906f76c6f6297515a14e2d88ea934124",
  "cid": "QmV1e5d59774ece1c0159de85deb18b02ecb906f76c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291926,
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
      "evaluated_at": 1760291926
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
  "sig": "4f5fd479148d1bb5f82bf98f041ed97ce3e84179966c883e59b16988979bc561"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 262, 'threshold': 50, 'total_amount': 83668128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 261, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}