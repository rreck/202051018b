```json
{
  "id": "c0d642a1eeb8648b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291232,
  "host_pid": "9e6742732c60:1",
  "hash": "d76c88a1f5fdb21729f876f94d7c76e2ca69efe6e7f3591c443c9188dc8589a3",
  "cid": "QmV1d76c88a1f5fdb21729f876f94d7c76e2ca69efe6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291232,
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
      "evaluated_at": 1760291232
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
  "sig": "9ea1db6d5f39a91f896cf5e1b96eb3f11c6cf2ed887ccf80bb4cedb922fde8f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020823686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 10572980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285764, 'matching_hash': '810bf9913cbceac2'}}}