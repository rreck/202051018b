```json
{
  "id": "25fe398f929e26bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289060,
  "host_pid": "9e6742732c60:1",
  "hash": "17d9043f82963819086a67883b1daf483f98fecb7f808b201898f9887e57d969",
  "cid": "QmV117d9043f82963819086a67883b1daf483f98fecb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289060,
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
      "evaluated_at": 1760289060
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
  "sig": "79d88e30a87b57f416c6930e444fb04ebf7ca7c3ad9d117819e26df0930ab1de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245742893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 40958512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '17d6d8b38d025182'}}}