```json
{
  "id": "2d546a39f083403b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287008,
  "host_pid": "9e6742732c60:1",
  "hash": "aa5d77e7c10f9197abbb4fc8566b5d57736a17394dded2f093ae66c83ce31006",
  "cid": "QmV1aa5d77e7c10f9197abbb4fc8566b5d57736a1739",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287008,
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
      "evaluated_at": 1760287008
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
  "sig": "dcd8e470673a289ac7e27a63dc6cdf6e44cd14c30f0e37dd5039baddc0a33d05"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244516225
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': '305c81c4ba1c9c62'}}}, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': '7792cb8eb05ccf8f'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}