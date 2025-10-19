```json
{
  "id": "991a1afe154e6a41",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287223,
  "host_pid": "9e6742732c60:1",
  "hash": "5a57078b53b1558009f3622403d273ea6172eaf0c97db36c7986e9820fab39b7",
  "cid": "QmV15a57078b53b1558009f3622403d273ea6172eaf0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287223,
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
      "evaluated_at": 1760287223
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
  "sig": "b41f01a19118d703b009f57986ead67870093b2f4c5bf8c98654631ff948fa82"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 10915008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}