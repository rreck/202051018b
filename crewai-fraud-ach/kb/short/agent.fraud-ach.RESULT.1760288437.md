```json
{
  "id": "6b21de1f507944a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288437,
  "host_pid": "9e6742732c60:1",
  "hash": "db4e129f4789f69d94d45574afc9f63c278d21200b9846fd96bd47d421a86f33",
  "cid": "QmV1db4e129f4789f69d94d45574afc9f63c278d2120",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288437,
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
      "evaluated_at": 1760288437
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
  "sig": "dcf4948576238dbd7c466226db7198af96cc99b6102a684d22d6513de7ebc1af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469526930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 10581354, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}