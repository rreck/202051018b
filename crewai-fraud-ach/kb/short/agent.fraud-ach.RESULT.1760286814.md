```json
{
  "id": "20a5684ac2e19262",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286814,
  "host_pid": "9e6742732c60:1",
  "hash": "cb429cc61dcefb766d99542fb4d82196fede5f845000d691e7d85346775efddf",
  "cid": "QmV1cb429cc61dcefb766d99542fb4d82196fede5f84",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286814,
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
      "evaluated_at": 1760286814
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
  "sig": "8961cb4316147395180803a3ba3d5abcaf1966b481f1ccf9fceaf513185b9978"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000020288859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18416358, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '0e6f21190a149d49'}}}760284979, 'matching_hash': 'a7fb9dc83800d725'}}}