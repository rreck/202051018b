```json
{
  "id": "3f8a8ed79f232b6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287378,
  "host_pid": "9e6742732c60:1",
  "hash": "768f4cca298c8b00af3b4ee89f476be605833386d6df4e83727479ccefe4a8b9",
  "cid": "QmV1768f4cca298c8b00af3b4ee89f476be605833386",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287378,
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
      "evaluated_at": 1760287378
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "83f45fea9ba37186259125b3951a45e7a554d7a94a1cd7731bb083b99bcd0b9e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462772191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 11878922, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285763, 'matching_hash': '3cc4f4a3442921e3'}}}