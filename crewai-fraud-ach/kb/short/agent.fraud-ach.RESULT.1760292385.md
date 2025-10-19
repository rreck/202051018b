```json
{
  "id": "f50bf18174ec51be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292385,
  "host_pid": "9e6742732c60:1",
  "hash": "7b736ca9558e9558f2c79363681577d8a4094068b85cdcfbd0c2f894b1f2e6ab",
  "cid": "QmV17b736ca9558e9558f2c79363681577d8a4094068",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292385,
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
      "evaluated_at": 1760292385
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
  "sig": "7dc72e895df0f64bc3d20e131440bc93bf3e4896286e316cfac96aad31031749"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021011137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 65292500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285764, 'matching_hash': '3868aeea45d72d6f'}}}