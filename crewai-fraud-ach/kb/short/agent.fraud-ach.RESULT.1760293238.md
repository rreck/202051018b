```json
{
  "id": "3f0521f4bbf2c960",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293238,
  "host_pid": "9e6742732c60:1",
  "hash": "a59041f96991e1076a33f46b128373c04a13fc262c4ce07bc9f8689fe6eb47fc",
  "cid": "QmV1a59041f96991e1076a33f46b128373c04a13fc26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293238,
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
      "evaluated_at": 1760293238
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
  "sig": "e4bb120707a73a12d2978a444967822b3e9a04148058f428d152a40456f478b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464452578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 20609698, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '0a8d6c8cd4d67655'}}}