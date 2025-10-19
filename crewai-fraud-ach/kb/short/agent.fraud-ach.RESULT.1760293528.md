```json
{
  "id": "8341c1311673a58c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293528,
  "host_pid": "9e6742732c60:1",
  "hash": "3ec8568c873c4ce6ffeafbe69163a259c13d4e9e328650438f71a62f0b28c09a",
  "cid": "QmV13ec8568c873c4ce6ffeafbe69163a259c13d4e9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293528,
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
      "evaluated_at": 1760293528
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
  "sig": "13935b27baf448eb5af2a0d6d63c03efd986b583d4305ffd5830395e796a5178"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271648434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 52074660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}