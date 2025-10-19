```json
{
  "id": "c231eb670f00c860",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291371,
  "host_pid": "9e6742732c60:1",
  "hash": "6f3abf19764fa7d0d1936093ff9411a1ad98f0e59b40f9e8c157d65d75f8940e",
  "cid": "QmV16f3abf19764fa7d0d1936093ff9411a1ad98f0e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291371,
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
      "evaluated_at": 1760291371
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
  "sig": "2417e2eae26ac4110fd73225348979d7250d74f5d3d18d2dcf2fcd3eaf5345f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152206156
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 42529974, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285764, 'matching_hash': '90dfebdd1b129ec8'}}}