```json
{
  "id": "700bb70c254c6af4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292173,
  "host_pid": "9e6742732c60:1",
  "hash": "3b558e9b228ec8581ebdaf91341b9d2442b727696401e91451577cf697716b5d",
  "cid": "QmV13b558e9b228ec8581ebdaf91341b9d2442b72769",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292173,
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
      "evaluated_at": 1760292173
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
  "sig": "88f4f09a9eadf07720bab138523374fb420e6f16b72dd1f70c147b46b09e4695"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275498951
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 36515136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'a1e1622f9da312c5'}}}