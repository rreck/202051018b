```json
{
  "id": "ffe23722f2bdb3ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286331,
  "host_pid": "9e6742732c60:1",
  "hash": "0354ed25ec57a51c857dcd952656bbfc988b8ede92c16f336c972831836a0c10",
  "cid": "QmV10354ed25ec57a51c857dcd952656bbfc988b8ede",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286331,
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
      "evaluated_at": 1760286331
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
  "sig": "369b247f2d45f0127fd554739ca87ae1707b13f60f0c37646222aa708af8dc61"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155862167
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': '207d73478b089b6e'}}}, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': 'd907a2a28cc997b7'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}