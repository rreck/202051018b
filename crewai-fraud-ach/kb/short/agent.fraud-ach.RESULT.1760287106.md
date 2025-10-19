```json
{
  "id": "e7497980eb7516fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287106,
  "host_pid": "9e6742732c60:1",
  "hash": "3fc8bdddd65669ebe070730669fbdb21ea89d89dbd15c2a91db96adc77dbe5bf",
  "cid": "QmV13fc8bdddd65669ebe070730669fbdb21ea89d89d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287106,
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
      "evaluated_at": 1760287106
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "3221554ff1f4ce05bff4ad3a172b5d36c89d8f07dc58abd77f9bb95ecf0198cb"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 121000249844926
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 252172896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285765, 'matching_hash': '4f8c06dc9d4c212b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5253602}}}