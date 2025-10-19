```json
{
  "id": "8b490f32d4c4e92a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291080,
  "host_pid": "9e6742732c60:1",
  "hash": "ef3923634fcf87cc6d9708b765d378341fefd338119b42981ffc1756c5c5778f",
  "cid": "QmV1ef3923634fcf87cc6d9708b765d378341fefd338",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291080,
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
      "evaluated_at": 1760291080
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
  "sig": "84fc039114b811e27c290e67ce5f04c718eba336b311773552c5da6392835af2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 28527598, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}