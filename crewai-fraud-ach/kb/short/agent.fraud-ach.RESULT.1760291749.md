```json
{
  "id": "fb0348d732d0af42",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291749,
  "host_pid": "9e6742732c60:1",
  "hash": "376d6c6e3a5406567b0b0430d1bbde01f368124eb03e7fb823f3fef79f5a9a70",
  "cid": "QmV1376d6c6e3a5406567b0b0430d1bbde01f368124e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291749,
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
      "evaluated_at": 1760291749
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
  "sig": "dc0880f41999d4c900b85500f258382d3b10f67457bdb6d812cece368af002fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151773289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 89518884, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '7b1e6accdb666d6e'}}}