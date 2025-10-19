```json
{
  "id": "63d183db13c3b04f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292178,
  "host_pid": "9e6742732c60:1",
  "hash": "93979953451fdbbfc2880d72f80ef12dddf2230e7460ab5643fe5a4027f7f4f0",
  "cid": "QmV193979953451fdbbfc2880d72f80ef12dddf2230e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292178,
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
      "evaluated_at": 1760292178
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
  "sig": "70a321cd3f846aa53190bb45eada7e5f7e1cec2f27a9f0905f69ec77cf1449cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466107420
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 77745408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'b2544ae352aa282b'}}}