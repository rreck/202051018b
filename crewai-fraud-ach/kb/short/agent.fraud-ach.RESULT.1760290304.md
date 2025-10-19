```json
{
  "id": "6e2836acec0bad90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290304,
  "host_pid": "9e6742732c60:1",
  "hash": "d367b09c5434cfeecfda75e820c265f506b4126dd1f583948e7cd1745436baec",
  "cid": "QmV1d367b09c5434cfeecfda75e820c265f506b4126d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290304,
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
      "evaluated_at": 1760290304
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
  "sig": "bdbee2d637006d19b72c08881667dc0fb7737c7c38b32b67153be6d660e875c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022696777
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 71601054, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': 'bb01014ea9b32f36'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5956409}}}um'}}}