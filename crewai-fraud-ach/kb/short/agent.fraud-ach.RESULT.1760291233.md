```json
{
  "id": "a344ddc1452b5d18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291233,
  "host_pid": "9e6742732c60:1",
  "hash": "6cfad3746cf68e96f219d011776fdd1dde02ffba65eb31eaaae8df7f665c4dea",
  "cid": "QmV16cfad3746cf68e96f219d011776fdd1dde02ffba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291233,
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
      "evaluated_at": 1760291233
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
  "sig": "d3d5000834fc1b6923e21d08dee9abdeb0dd80e6adcc350ad490be3d69c29ca9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461912165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 59690230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'd770463353c2594b'}}}