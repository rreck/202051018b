```json
{
  "id": "91c4be18aceefe38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293657,
  "host_pid": "9e6742732c60:1",
  "hash": "a50c444ac3f9728a40be6b79d5adf3032b2f9be7901c9b3742f87299788d7523",
  "cid": "QmV1a50c444ac3f9728a40be6b79d5adf3032b2f9be7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293657,
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
      "evaluated_at": 1760293657
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
  "sig": "fec2a00da482d0816c00d2d852dad6f0c6707ba7f4a915a963707d83a602a281"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242172457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 105070910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '180325de6151a8c9'}}}