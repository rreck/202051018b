```json
{
  "id": "bd43671ddd1ec003",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290902,
  "host_pid": "9e6742732c60:1",
  "hash": "a4e171bd5a15094cd85b72e2df3d20bf0da8e60ea82b49e24bc1f56842d5d32d",
  "cid": "QmV1a4e171bd5a15094cd85b72e2df3d20bf0da8e60e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290902,
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
      "evaluated_at": 1760290903
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
  "sig": "c44e939ffbad7508190967616dcf063035cf43bd2239ce15a051e91c8ebdb3d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 80259174, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}