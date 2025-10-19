```json
{
  "id": "17c296946c8d7f62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287013,
  "host_pid": "9e6742732c60:1",
  "hash": "df87a91bf6988e70541393df7e73f67018a809b7125d53d04fa665df7c256ed3",
  "cid": "QmV1df87a91bf6988e70541393df7e73f67018a809b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287013,
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
      "evaluated_at": 1760287013
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "9288333b0115853d4f9c7787370234cd27a24e7f663f4386c373ca4e32fdad59"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 650095542347097
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285764, 'matching_hash': 'ccbd48c11c0f622e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '650095545', 'validation_error': 'Invalid routing number checksum'}}}