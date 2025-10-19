```json
{
  "id": "9f0e670849fa2324",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286985,
  "host_pid": "9e6742732c60:1",
  "hash": "e2418e8a84d605a26ee951fe31c2e65a8937398f129a3d96693aeb1d21b27294",
  "cid": "QmV1e2418e8a84d605a26ee951fe31c2e65a8937398f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286985,
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
      "evaluated_at": 1760286985
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
  "sig": "e74b1aaa7656eb658ab2060379c549f651de27eb2dbad03d840e0e80ddf7a245"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000023745358
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285764, 'matching_hash': '29c890c1b3276ef0'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}