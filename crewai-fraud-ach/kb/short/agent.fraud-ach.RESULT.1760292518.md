```json
{
  "id": "9332e0b43fbd1734",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292518,
  "host_pid": "9e6742732c60:1",
  "hash": "ac886fd94d03600c505deebc283a7bf2964a06bdf84b12546ba629e46c2fdf2a",
  "cid": "QmV1ac886fd94d03600c505deebc283a7bf2964a06bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292518,
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
      "evaluated_at": 1760292518
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
  "sig": "1b409d50776696ca63d3885552f5f8f7414f501926b605aa6be243119e35328f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025895266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 56496100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}