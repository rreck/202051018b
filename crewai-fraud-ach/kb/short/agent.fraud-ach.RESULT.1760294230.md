```json
{
  "id": "66aeb6ce4eeecba2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294230,
  "host_pid": "9e6742732c60:1",
  "hash": "df8505162955e7fefed6286a1389cbb5853646d5692cc778fd63ce88285630b5",
  "cid": "QmV1df8505162955e7fefed6286a1389cbb5853646d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294230,
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
      "evaluated_at": 1760294230
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
  "sig": "90510ad971989e635b62aee9aa35f0a91e674912424b2b7ddcf63df1706a76b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150046055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 91980486, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': 'b44312efb353b904'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}