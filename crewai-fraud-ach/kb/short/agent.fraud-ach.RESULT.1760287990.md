```json
{
  "id": "fe10869ee65fb55e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287990,
  "host_pid": "9e6742732c60:1",
  "hash": "588ea451763c5c441ea95a166deeabaed70bc079286894bfd254d75a2067450c",
  "cid": "QmV1588ea451763c5c441ea95a166deeabaed70bc079",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287990,
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
      "evaluated_at": 1760287990
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
  "sig": "e01431cd76f65b3f5e70c3130c058046a2afc23f76203d2426e310ac73b16564"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460007503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 14067609, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': '17a9441d6a1d37be'}}}