```json
{
  "id": "08f82d6d3a6312de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288170,
  "host_pid": "9e6742732c60:1",
  "hash": "4d69ba5cdda6a41102d212666fffd1adcc763f9e500ae0ee0718fccb418eaad4",
  "cid": "QmV14d69ba5cdda6a41102d212666fffd1adcc763f9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288170,
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
      "evaluated_at": 1760288170
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
  "sig": "7811a3b3435fca8536743ee3ef58d2b1a7b7ead586b8164239b87cbabede334e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024511809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 14903645, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': '174f6230f942e53f'}}}