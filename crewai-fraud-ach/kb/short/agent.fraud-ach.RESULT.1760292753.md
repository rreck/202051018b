```json
{
  "id": "9196931ea1b6330a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292753,
  "host_pid": "9e6742732c60:1",
  "hash": "d2c27c16d632c8f0335330c51a371183bd44402337d32e78c841943d520a5f93",
  "cid": "QmV1d2c27c16d632c8f0335330c51a371183bd444023",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292753,
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
      "evaluated_at": 1760292753
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
  "sig": "163c9ad5509987d9695ce58be439687f7b73c63087772ed396171e90783de0ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020048209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 16963620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '08bd6998776e568a'}}}