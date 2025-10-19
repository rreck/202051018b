```json
{
  "id": "85cccea42aa3b2d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289221,
  "host_pid": "9e6742732c60:1",
  "hash": "1ddbf4ada24088706ddedfd4135b5d1ce322c6b611eaa44ddcdc930851675090",
  "cid": "QmV11ddbf4ada24088706ddedfd4135b5d1ce322c6b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289221,
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
      "evaluated_at": 1760289221
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
  "sig": "90fe79d6fdf1aa1e212d0b2ea5d71a39ee74db8d6f2c8725ab45ec252b3ac6c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 30326166, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}