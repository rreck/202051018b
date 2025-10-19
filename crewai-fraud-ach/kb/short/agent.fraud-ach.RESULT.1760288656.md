```json
{
  "id": "09196d01c7a19363",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288656,
  "host_pid": "9e6742732c60:1",
  "hash": "aa86891c3754a479aa6b1fca68f2428802b60610fdbe570ced2899fb988b9205",
  "cid": "QmV1aa86891c3754a479aa6b1fca68f2428802b60610",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288656,
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
      "evaluated_at": 1760288656
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
  "sig": "2ae32ed641a6187fb7f5e820b6829edfcc797da16998e7f51316adc0c131737e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153776491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '94746339473c09ed'}}}een': 1760285763, 'matching_hash': 'bdea4d686a9b26f8'}}}